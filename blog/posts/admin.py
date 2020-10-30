from django import forms
from django.contrib import admin
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    form = PostAdminForm

