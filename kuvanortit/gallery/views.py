from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Picture, PictureFolder
from django.db.models import Q
from .forms import UploadForm, AddFolder
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

class GalleryView(generic.ListView):
    model = Picture
    template_name = "gallery/index.html"
    context_object_name = "picture_list"
    paginate_by = 21

    def get_queryset(self):
        if self.request.user.is_authenticated:
            q = Picture.objects.filter(
                Q(private=False) | Q(folder__user=self.request.user)
            ).order_by("-pub_date")
        else:
            q = Picture.objects.filter(private=False).order_by("-pub_date")
        return q
    
   
class PictureDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Picture
    success_url = reverse_lazy("gallery:index")
    raise_exception = True
    
    def test_func(self):
        self.picture = get_object_or_404(Picture, pk=self.kwargs["pk"])
        return self.request.user == self.picture.folder.user

class FolderDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = PictureFolder
    success_url = reverse_lazy("gallery:index")
    raise_exception = True

    def test_func(self):
        self.folder = get_object_or_404(PictureFolder, pk=self.kwargs["pk"])
        return self.request.user == self.folder.user

class PictureEditView(UserPassesTestMixin, generic.UpdateView):
    model = Picture
    fields = ["title", "description", "tags", "private"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("gallery:index")

    def test_func(self):
        self.picture = get_object_or_404(Picture, pk=self.kwargs["pk"])
        return self.request.user == self.picture.folder.user
    

class UserListView(generic.ListView):
    model = User
    template_name = "gallery/user.html"
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs["user"])
        folder_list = PictureFolder.objects.filter(user=user)
        return user, folder_list


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user, folder_list = self.get_queryset()

        context['username'] = user
        context['folder_list'] = folder_list
        return context
    
class FolderListView(generic.ListView):
    model = PictureFolder
    template_name = "gallery/folder.html"
    
    def get_queryset(self):
        folder = get_object_or_404(PictureFolder, pk=self.kwargs["pk"])
        if self.request.user.is_authenticated:
            picture_list = Picture.objects.filter(
                Q(folder=folder),
                Q(private=False) | Q(folder__user=self.request.user)
            ).order_by("-pub_date")
        else:
            picture_list = Picture.objects.filter(private=False, folder=folder)
        return folder, picture_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        folder, picture_list = self.get_queryset()

        context['folder'] = folder
        context['picture_list'] = picture_list
        return context
    
def create_folder(request):
    if request.method == 'POST':
        form = AddFolder(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('gallery:index')
    else:
        form = AddFolder()
    return render(request, 'gallery/create_folder.html', {'form' : form})



def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.user.pk, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:index')
    else:
        if request.user.is_authenticated:
            if not PictureFolder.objects.filter(user=request.user):
                PictureFolder(title='Default', user=request.user).save()
        form = UploadForm(request.user.pk)
    return render(request, 'gallery/upload.html', {'form' : form})


def success(request):
    return render(request, 'gallery/success.html', {})

class SearchResultsView(generic.ListView):
    model = Picture
    template_name = 'gallery/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if self.request.user.is_authenticated:
            object_list = Picture.objects.filter(
                Q(private=False) | Q(folder__user=self.request.user),
                Q(title__icontains=query) | Q(tags__icontains=query) | Q(description__icontains=query)
            )
        else:
            object_list = Picture.objects.filter(
                Q(private=False),
                Q(title__icontains=query) | Q(tags__icontains=query) | Q(description__icontains=query)
            )
        return object_list
