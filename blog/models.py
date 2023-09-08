from django.db import models
from hitcount.models import HitCount, HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField

import readtime


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(default="blog-post.jpg", upload_to="post_pics")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("blog:blog_home")
