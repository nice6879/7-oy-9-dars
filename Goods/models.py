from django.db import models
from django.contrib.auth.models import User
from random import sample
import string

class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='banners/'),
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    generate_code = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name:str = models.CharField(max_length=255)
    quantity:int = models.PositiveIntegerField(default=1)
    price:float = models.DecimalField(max_digits=8, decimal_places=2)
    category:Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description:str = models.TextField()

    def __str__(self):
        return self.name

class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='product-img')

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    shopping_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.author.username

class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    status = models.SmallIntegerField(
        choices=(
            (1, 'Tayyorlanmoqda'),
            (2, 'Yo`lda'),
            (3, 'Yetib borgan'),
            (4, 'Qabul qilingan'),
            (5, 'Qaytarilgan'),
        )
    )

    def __str__(self):
        return self.full_name


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}, {self.product.name}"
    


class Borrower(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term = models.PositiveIntegerField(help_text="Term in months")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"Loan {self.id} for {self.borrower}"

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=[('Cash', 'Cash'), ('Bank Transfer', 'Bank Transfer'), ('Online', 'Online')])

    def __str__(self):
        return f"Payment {self.id} for Loan {self.loan.id}"

class LoanOfficer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

