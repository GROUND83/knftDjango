from fileinput import filename
from itertools import product
import sys
from django.db import models
from config.settings import MEDIA_ROOT
from cores import models as core_models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from django.utils.safestring import mark_safe
from imgpy import Img
from PIL import Image, ImageSequence
from io import BytesIO, StringIO

import os.path
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

# from .my_app_settings import THUMB_SIZE
def mainImage_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "profile_photos/{0}/{1}".format(instance.name, filename)


def thumImage_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "profile_photos/{0}/{1}".format(instance.name, filename)


# Create your models here.
class Author(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "작가"
        verbose_name_plural = "작가모음"
        ordering = ["name"]

    name = models.CharField(max_length=50, null=True, verbose_name="작가명", unique=True)
    authDes = models.CharField(
        max_length=50, null=True, verbose_name="작가설명", unique=False
    )
    avator = models.ForeignKey(
        "files.File", related_name="files", on_delete=models.CASCADE, null=True
    )

    desTitle = models.CharField(
        max_length=50, null=True, verbose_name="작가 타이틀", unique=False
    )
    description  = models.TextField (blank=True, null=True,verbose_name="작가 컨텐츠",)
   
    discord = models.CharField(
        max_length=50, null=True, verbose_name="discord", unique=False, blank=True
    )
    facebook = models.CharField(
        max_length=50, null=True, verbose_name="facebook", unique=False, blank=True
    )
    instargram = models.CharField(
        max_length=50, null=True, verbose_name="instargram", unique=False, blank=True
    )
    twitter = models.CharField(
        max_length=50, null=True, verbose_name="twitter", unique=False, blank=True
    )
    show = models.BooleanField(default=True, verbose_name="노출")
    products = models.ManyToManyField(
        "products.Product", null=True, blank=True, related_name="product"
    )

    def __str__(self):
        return f"{self.name}"
