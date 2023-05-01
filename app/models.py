from django.db import models, migrations
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()
class Tag(models.Model):
    name  = models.CharField(max_length=50, unique=True)
    about_tag = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=255, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modefied = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    thumbnail = models.FileField(upload_to='thumbnails', unique=True, null=True)

    class Meta:
        ordering = ['-publish_date']
    def __str__(self):
        return self.title
class Media(models.Model):
    file = models.FileField(upload_to='media/', unique=True)
    def __str__(self):
        return self.file.name