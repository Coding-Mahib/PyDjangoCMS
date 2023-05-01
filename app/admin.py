from django.contrib import admin
from app.models import Post, Profile, Tag, Media

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "slug",
        "publish_date",
        "published",
        "thumbnail",
        "content",
    )
    list_filter = (
        "published",
        "publish_date"
    )
    list_editable = (
        "title",
        "slug",
        "publish_date",
        "published",
        "thumbnail",
        "content",
    )
    prepopulated_fields = {
        "slug": (
            "title",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True

admin.site.register(Media)