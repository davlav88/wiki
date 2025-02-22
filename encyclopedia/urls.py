from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.wiki, name="wiki" ),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit", views.edit, name="edit"),
    path("random_pick", views.random_pick, name="random_pick")
]
