

from django import forms

from django.shortcuts import render

from . import models

from django.contrib.auth.decorators import login_required

class PhotoForm(forms.ModelForm):

    class Meta:

        model = models.Photo

        fields = ['image', 'caption']


class BlogForm(forms.ModelForm):

    class Meta:

        model = models.Blog

        fields = ['title', 'content']

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)



@login_required

def blog_and_photo_upload(request):

    blog_form = forms.BlogForm()

    photo_form = forms.PhotoForm()

    if request.method == 'POST':

        blog_form = forms.BlogForm(request.POST)

        photo_form = forms.PhotoForm(request.POST, request.FILES)

        if all([blog_form.is_valid(), photo_form.is_valid()]):

            blog_form.save()

            photo_form.save()

        context = {

            'blog_form': blog_form,

            'photo_form': photo_form,

        }

    return render(request, 'blog/create_blog_post.html', context=context)
