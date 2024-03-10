from django.shortcuts import render
from .models import PopularPlaces


# Create your views here.
def index(request):

    # pp1 = PopularPlaces()
    # pp1.name = "Mumbai"
    # pp1.price = 750
    # pp1.img = "1.png"
    # pp1.desc = "The City That Never Sleeps!"
    # pp1.reviews = 455
    # pp1.days = 4

    # pp2 = PopularPlaces()
    # pp2.name = "Goa"
    # pp2.price = 550
    # pp2.img = "4.png"
    # pp2.desc = "A tiny emerald on the west coast of India!"
    # pp2.reviews = 2206
    # pp2.days = 5

    # pp3 = PopularPlaces()
    # pp3.name = "Bengaluru"
    # pp3.price = 800
    # pp3.img = "3.png"
    # pp3.desc = "The Garden City with Silicon Valley!"
    # pp3.reviews = 399
    # pp3.days = 4

    # pps = [pp1, pp2, pp3]

    # All the above code is static content, instead we are using database to fetch the data and display it on the website
    places = PopularPlaces.objects.all()

    return render(request, "index.html", {"places": places})
