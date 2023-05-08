from django.test import Client, TestCase

from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(
            title="IceCream", price=80, inventory=100
        )

    def test_getall(self):
        response = self.client.get("restaurant/menu/")
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        print(f"=== {response}")
        print(f"=== {serializer}")
        self.assertEqual(response, serializer.data)

    def test_getone(self):
        item = Menu.objects.create(
            title="DishA", price=50, inventory=25
        )
        response = self.client.get(
            f"/restaurant/menu/{item.id}/"
        )
        serializer = MenuItemSerializer(item, many=False)
        self.assertEqual(response.data, serializer.data)
