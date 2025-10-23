import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
        ('uniform', 'Uniform'),
        ('t-shirt', 'T-Shirt'),
        ('socks', 'Socks'),
        ('merchandise', 'Merchandise'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=255)
    rating = models.FloatField(default=0)


    def __str__(self):
        return self.name

    @property
    def is_stock_available(self):
        return self.stock > 0

    def recalculate_rating(self):
        ratings = self.ratings.all()
        avg = sum(r.score for r in ratings) / ratings.count() if ratings.exists() else 0
        self.rating = avg
        self.save()

    def get_rating_count(self):
        return self.ratings.count()

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f'{self.user.username} rated {self.product.name}: {self.score}'



@receiver([post_save, post_delete], sender=Rating)
def update_product_rating(sender, instance, **kwargs):
    product = instance.product
    avg = product.ratings.aggregate(Avg('score'))['score__avg'] or 0
    product.rating = avg
    product.save(update_fields=['rating'])


'''
class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    stock = models.IntegerField()
'''