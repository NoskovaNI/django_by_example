from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# This includes the data models of the application; all Django
# applications need to have a models.py file, but this file can be left empty.


class PublishedManager(models.Manager):
    def set_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,  # This is field for URL
                            unique_for_date='publish')  # must be unique in one day
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    object = models.Manager()  # the default manager
    published = PublishedManager()  # custom manager

    class Meta:
        ordering = ('-publish',)  # sort result by publish date

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

