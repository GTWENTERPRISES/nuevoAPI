from django.db import models
from django.core.validators import MinValueValidator, URLValidator, RegexValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

def validate_image_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError(
            'Por favor ingrese una URL válida'
        )

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ramo', 'Ramo'),
        ('obsequio', 'Obsequio'),
    ]

    name = models.CharField(
        max_length=200,
        verbose_name='Nombre',
        help_text='Ingrese el nombre del producto (mínimo 3 caracteres, solo letras, números y espacios)',
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]{3,}$',
                message='El nombre debe tener al menos 3 caracteres y solo puede contener letras, números y espacios'
            )
        ]
    )
    description = models.TextField(
        verbose_name='Descripción',
        help_text='Describa el producto detalladamente (mínimo 10 caracteres). Incluya materiales, colores, y detalles importantes',
        validators=[
            RegexValidator(
                regex=r'^.{10,}$',
                message='La descripción debe tener al menos 10 caracteres'
            )
        ]
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Precio',
        help_text='Ingrese el precio en dólares (ejemplo: 15.99). Debe ser mayor a 0',
        validators=[
            MinValueValidator(
                Decimal('0.01'),
                message='El precio debe ser mayor a 0'
            )
        ]
    )
    image_url = models.URLField(
        max_length=500,
        verbose_name='URL de la imagen',
        help_text='Ingrese la URL completa de la imagen del producto',
        validators=[validate_image_url]
    )
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES,
        verbose_name='Categoría',
        help_text='Seleccione la categoría del producto'
    )
    features = models.TextField(
        blank=True,
        null=True,
        verbose_name='Características',
        help_text='Ingrese las características del producto separadas por comas (máximo 10 características). Ejemplo: Tarjeta dedicatoria, Banda personalizada',
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s,()]{0,}$',
                message='Las características solo pueden contener letras, números, espacios, comas y paréntesis'
            )
        ]
    )

    def clean(self):
        # Validación adicional a nivel de modelo
        if self.features and len(self.features.split(',')) > 10:
            raise ValidationError({
                'features': 'No puede tener más de 10 características'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
