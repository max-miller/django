from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),

    ]

# path("recs/<str:edition_name>",views.letter, name="letter"),