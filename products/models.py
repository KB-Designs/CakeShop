from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # ✅ change from CharField → ForeignKey
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    ICING_CHOICES = [
        ('whipping cream', 'Whipping Cream'),
        ('butter icing', 'Butter Icing'),
        ('fondant', 'Fondant'),
        ('butter cream', 'Butter Cream'),
        ('fresh cream', 'Fresh Cream'),
    ]

    EGG_CHOICES = [
        ('with_eggs', 'With Eggs'),
        ('eggless', 'Eggless'),
    ]

    product = models.ForeignKey(Product, related_name="variants", on_delete=models.CASCADE)
    size = models.CharField(max_length=50)   # e.g., "1kg", "2kg"
    price = models.DecimalField(max_digits=10, decimal_places=2)

    icing = models.CharField(
        max_length=50,
        choices=ICING_CHOICES,
        default='whipping cream'
    )
    egg_option = models.CharField(
        max_length=20,
        choices=EGG_CHOICES,
        default='with_eggs'
    )

    def __str__(self):
        return f"{self.product.name} - {self.size} ({self.icing}, {self.egg_option})"