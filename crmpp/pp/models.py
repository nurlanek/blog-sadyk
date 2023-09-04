from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Pp(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pps")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    # slug = models.SlugField(null=True, blank=True, unique=True, db_index=True) alani doldurduktan sonra null=True yu False olarak degistirdik
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE) #ManyToOne
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
