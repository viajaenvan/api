from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)
    img_logo = models.ImageField(upload_to='brands/images/')
    create_date = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


