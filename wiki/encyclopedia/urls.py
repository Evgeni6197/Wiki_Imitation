from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('search',views.search, name='search'),
    path('new-page',views.new_page, name='new_page'),
    path('<str:entry_name>', views.entry, name='entry'),
    
]
