from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpResponse, FileResponse, HttpResponseForbidden
from app.config import SITE
from . import models

# Create your views here.
def Home(req):
    Post = models.Post.objects.filter(published=True).order_by("-publish_date")
    desc = SITE.Description

    posts = 0
    for p in Post:
        posts += 1
    return render(req, 'index.html', {'SITE': SITE, 'posts': Post, 'count': posts, 'title': 'Home', 'desc': desc})


def About(req):
    return render(req, 'about.html', {'SITE': SITE, 'title': 'About Us'})


def Files(req):
    if req.GET['file']:
        file = req.GET['file']
        try:
            f = open(file, 'rb')
            return FileResponse(f)
        except FileNotFoundError:
            return PAGE_404(req, file)
        except Exception as e:
            f = open('log.txt', 'w')
            f.write(f'\n[Blog/Error] `{e}`')
            f.close()

def Media(req):
    if req.GET['file']:
        file = req.GET['file']
        try:
            f = open(file, 'rb')
            return FileResponse(f)
        except FileNotFoundError:
            return PAGE_404(req, file)
        except Exception as e:
            f = open('log.txt', 'w')
            f.write(f'\n[Blog/Error] `{e}`')
            f.close()

def SearchPosts(req):
    desc = SITE.Description
    if req.GET['q']:
        q = req.GET['q']
    else:
        q = ''
    Post = models.Post.objects.filter(title__startswith=q) | models.Post.objects.filter(title__endswith=q)
    posts = 0
    for p in Post:
        posts += 1
    return render(req, 'index.html', {'SITE': SITE, 'posts': Post, 'field_text': q, 'count': posts, 'desc': desc})

def DetailsPosts(req, slug):
    Post = models.Post.objects.filter(slug=slug)
    posts = 0
    for p in Post:
        posts += 1
    if posts == 1:
        Post = Post[0]
        desc = Post.meta_description
        title = Post.title
    else:
        Post = []
        desc = SITE.Description
        title = 'Not Found'
    return render(req, 'details.html', {'SITE': SITE, 'title': title, 'posts': posts, 'post': Post, 'desc': desc})

def richTextField(req):
    return render(req, 'richtext.html', {'SITE': SITE, 'title': 'Rich Text Editor'})
def MediaUrl(req):
    return render(req, 'mug.html', {'SITE': SITE, 'title': 'Media URL Genarator'})
def PAGE_404(req, url):
    raise Http404(f'Your requested url `{url}` not found in the server !')