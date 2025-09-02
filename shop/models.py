from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(
        upload_to="products/main/", blank=True, null=True
    )  # main image

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:detail", args=[self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/gallery/")
    alt = models.CharField(max_length=180, blank=True)

    def __str__(self):
        return f"{self.product.name} image"
