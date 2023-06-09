from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r"tables", views.BookingViewSet)


urlpatterns = [
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("booking/", include(router.urls)),
    path("api-token-auth/", obtain_auth_token),
    path("auth/", include("djoser.urls")),
]
