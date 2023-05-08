from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests_count = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_slot = models.SmallIntegerField(default=10)


class MenuCategory(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return f"{self.title}"


class MenuItem(models.Model):
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.SET_NULL,
        related_name="items",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
