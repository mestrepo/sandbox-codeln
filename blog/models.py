from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """
    custom model manager for Post model.
    retrieves all posts with published status.
    """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    objects = models.Manager()  # the default manager
    published = PublishedManager()  # customer manager for published posts

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # field for the post title
    title = models.CharField(max_length=250)

    # field to build beautiful, SEO-friendly URLs for blog posts
    # prevent multiple posts from having the same slug for the same date
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    #  post written by
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='blog_posts')

    # body of the post
    body = models.TextField()

    # when post was published
    publish = models.DateTimeField(default=timezone.now)

    # when post was created
    created = models.DateTimeField(auto_now_add=True)

    # last time the post was updated
    updated = models.DateTimeField(auto_now=True)

    # field to show the status of a post
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        # sort results by the publish field in descending order
        ordering = ('-publish',)

    # default human-readable representation of the object
    # used in many places such as the administration site
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """build the canonical URL for Post objects"""
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.strftime('%m'),
                self.publish.strftime('%d'),
                self.slug
            ]
        )
