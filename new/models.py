from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ramo', 'Ramo'),
        ('obsequio', 'Obsequio'),
    ]

    name = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )
    description = models.TextField(
        verbose_name='Descripción'
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Precio'
    )
    image_url = models.URLField(
        max_length=500,
        verbose_name='URL de la imagen'
    )
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES,
        verbose_name='Categoría'
    )
    features = models.TextField(
        blank=True,
        null=True,
        verbose_name='Características',
        help_text='Ingrese las características separadas por comas'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
