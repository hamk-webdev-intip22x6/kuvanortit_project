from django import forms
from .models import Picture, PictureFolder


class UploadForm(forms.ModelForm):
    def __init__(self, user_id=0, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields["folder"].queryset = PictureFolder.objects.filter(user=user_id)

    class Meta:
        model = Picture
        fields = ["title", "description", "tags", "image", "private", "folder"]


class AddFolder(forms.ModelForm):
    class Meta:
        model = PictureFolder
        fields = [
            "title",
            "description",
        ]
