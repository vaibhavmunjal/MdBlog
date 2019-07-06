from django.db import models
from django.urls import reverse
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/images", blank=True)
    height_field =  models.IntegerField(default=0)
    width_field =  models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog')

    def __str__(self):
        return str(self.title)

    def get_markdown(self):
        content = self.content
        mark_content = markdown(content)
        return mark_safe(mark_content)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_signal, sender=Post)
