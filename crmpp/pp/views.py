from django.http.response import HttpResponse
from django.shortcuts import render
from pp.models import Pp, Category

"""
data = {
    "pps": [
        {
            "id": 1,
            "title": "komple web gelistime",
            "image": "1.jpg",
            "is_active": True,
            "is_home": False,
            "description": "iyi bir kurs"
        },
        {
            "id": 2,
            "title": "Python kuru",
            "image": "2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "iyi bir kurs"
        },
        {
            "id": 3,
            "title": "Djangoe",
            "image": "3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "iyi bir kurs"
        }
    ]

}
"""


def index(request):
    context = {
        "pps": Pp.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "pp/index.html", context)


def pp(request):
    context = {
        "pps": Pp.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "pp/pps.html", context)


def pp_details(request, slug):
    pp = Pp.objects.get(slug=slug)
    return render(request, "pp/production-details.html", {
        "pp": pp
    })


def pps_by_category(request, slug):
    context = {
        "pps": Category.objects.get(slug=slug).pp_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "pp/index.html", context)
