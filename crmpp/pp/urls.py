from django.urls import path
from . import views

# http://127.0.0.1:8000/            => homepage
# http://127.0.0.1:8000/index       => homeage
# http://127.0.0.1:8000/pp          => pp
# http://127.0.0.1:8000/pp/5        => pp-details


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("pps", views.pp, name="pps"),
    path("category/<slug:slug>", views.pps_by_category, name="pps_by_category"),
    path("pp/<slug:slug>", views.pp_details, name="production_details"),
]
