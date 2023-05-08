import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from restaurant.forms import BookingForm
from restaurant.models import Booking, MenuCategory, MenuItem


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = Booking.objects.filter(
            booking_date=data["reservation_date"]
        ).filter()
        if exist:
            return HttpResponse(
                "{'error':1}", content_type="application/json"
            )
        Booking.objects.create(
            first_name=data["first_name"],
            reservation_date=data["reservation_date"],
            reservation_slot=data["reservation_slot"],
        )
        return redirect(reverse("bookings"))
    bookings = Booking.objects.all()
    print(bookings)
    return render(
        request, "bookings.html", {"bookings": bookings}
    )


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            print("=== valid form===")
            form.save()
            messages.add_message(request, 50, "Booking added")
            return redirect(book)
    context = {"form": form}
    return render(request, "book.html", context)


def menu(request):
    categories = MenuCategory.objects.all()
    return render(
        request, "list_menu.html", {"categories": categories}
    )


def menu_item_detail(request, pk=None):
    item = get_object_or_404(MenuItem, pk=pk)
    return render(
        request,
        "menu_item_detail.html",
        {"item": item},
    )
