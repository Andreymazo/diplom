from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from django.contrib.auth.models import AbstractUser

from config import settings

NULLABLE = {'blank': True, 'null': True}


tax = 10
bank_comission = 2
author_our_comission = 20

def create_seller( seller):
    print('seller', seller)
    if not seller:
        return seller
    return seller

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self,  password, seller, **extra_fields):#email,
        """
        Create and save a User with the given email and password.
        """
        # if not email:
        #     raise ValueError(_('The Email must be set'))
        # email = self.normalize_email(email)
        seller = self.create_seller(seller)
        user = self.model(seller, **extra_fields)#email=email,
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,  password, **extra_fields):#email,
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(password, **extra_fields)#email,


class CustomUser(AbstractUser):
    STATUS_SELLER = True
    STATUS_NOSELLER = False
    STATUSES = (
        (STATUS_SELLER, 'SELLER'),
        (STATUS_NOSELLER, 'NOSELLER')
    )
    username = None
    email = models.EmailField(_('емэйл '), unique=True)
    seller = models.BooleanField(choices=STATUSES, verbose_name='Продавец', default=STATUS_SELLER)  # verbose_name='Продавец'
    print('seller ---------------- ----------------')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Категория продукта")
    bank_fee = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)],
                                   **NULLABLE)  # DecimalField(decimal_places=2, max_digits=20,
    # default=0.00)  # IntegerField(validators=[MinValueValidator(0)])
    tax = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)],
                              **NULLABLE)  # DecimalField(decimal_places=2, max_digits=20,
    # default=0.00)  # IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    profit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)],
                                 **NULLABLE)  # DecimalField(decimal_places=2, max_digits=20,
    # default=0.00)  # IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])

    def __str__(self):
        return f'{self.category_name}'


#################################Аналогично кастомному креэйту, классметод работает https://django.fun/ru/docs/django/4.1/ref/models/instances/
# from django.db import models

# class ProductManager(models.Manager):
#     def create_product(self, product_name: int, category_id: int, user_id: int, price_value: int, product_description: str):
#         product = self.create(
#             user_id=user_id,
#             product_name=product_name,
#             category_id=category_id,
#             price_value=price_value,
#             product_description=product_description
#         )
#
#         ######################################
#         product.price_value = product.price_value + product.price_value / 100 * tax # Category.objects.all().get(category_id=product.objects.all().get(category_id), tax=product.category.tax)
# #         ##########################################

#         product.save()  ## В базу заносится на 10%(tax) больше, чем креатим
#


class Product(models.Model):
    # objects = ProductManager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="category", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, verbose_name='Наименование')
    product_description = models.CharField(max_length=200, verbose_name=" Описание", **NULLABLE)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    price_value = models.IntegerField(
        validators=[MinValueValidator(0)])  # DecimalField(decimal_places=2, max_digits=20,default=0.00, **NULLABLE)  #

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

        permissions = [
            ("add_Product", "Can add Product"),
        ]

    def __str__(self):
        return self.product_name

    # @classmethod
    # def create_product(cls, user_id, category_id, product_name, price_value):
    #     product = Product.objects.create_product(
    #             product_name=product_name,
    #             user_id=user_id,
    #             category_id=category_id,
    #             price_value=price_value*tax/100,
    #     )
    #     product.save()
    #     print('test2')


# product = Product.objects.create_product(
#         user_id=1,
#         product_name='Iriska',
#         category_id=1,
#         price_value=10,
# )