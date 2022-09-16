from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("_search", views.search, name="search"),
    path("_new-page", views.new_page, name="new_page"),
    path("_edit-page", views.edit, name="edit"),
    path("_random-page", views.rand_page, name="random_page"),
    path("<str:entry_name>", views.entry, name="entry"),
]
