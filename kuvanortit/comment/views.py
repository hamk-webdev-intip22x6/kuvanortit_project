from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic.edit import BaseFormView, CreateView

# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from .models import Post
from gallery.models import Picture
from django.views.generic import ListView, DeleteView


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["comment"]
        widgets = {"comment": forms.Textarea}


class PostView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    login_url = "/login/"
    form_class = PostForm
    model = Post
    template_name = "comment/post.html"

    def get_success_url(self):
        return reverse_lazy("comment:index", kwargs={"pk": self.kwargs["post_id"]})

    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        picture_id = self.kwargs["post_id"]
        form.instance.picture = get_object_or_404(Picture, pk=picture_id)
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        self.picture = get_object_or_404(Picture, pk=self.kwargs["post_id"])
        if self.picture.private == True:
            if self.request.user.is_authenticated:
                return self.request.user == self.picture.folder.user
            else:
                return False
        else:
            return True


class CommentListView(UserPassesTestMixin, ListView):
    template_name = "comment/index.html"
    context_object_name = "comment_list"
    raise_exception = True

    def get_queryset(self):
        picture = get_object_or_404(Picture, pk=self.kwargs["pk"])
        comments = Post.objects.filter(picture=picture).order_by("-date")
        return picture, comments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture, comments = self.get_queryset()
        context["picture"] = picture
        context["comment_list"] = comments
        return context

    def test_func(self):
        self.picture = get_object_or_404(Picture, pk=self.kwargs["pk"])
        if self.picture.private == True:
            if self.request.user.is_authenticated:
                return self.request.user == self.picture.folder.user
            else:
                return False
        else:
            return True


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    # success_url = "gallery:index"
    raise_exception = True

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Post, pk=pk)

    def get_success_url(self):
        post_id = self.kwargs.get("post_id")
        return reverse_lazy("comment:index", kwargs={"pk": post_id})
