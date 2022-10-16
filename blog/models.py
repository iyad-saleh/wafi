from django.db import models
from django.utils import timezone
from django.conf import settings
# from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title




class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    body = RichTextUploadingField() # CKEditor Rich Text Field
    tags = TaggableManager()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
