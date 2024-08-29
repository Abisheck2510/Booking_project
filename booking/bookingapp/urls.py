from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/book/', views.book, name='book'),
    path('home/book/details/', views.booking_detail, name='details'),
    path('home/book/list/', views.booking_list, name='booking_list'),
    path('home/book/update/<int:id>/', views.booking_detail, name='update_booking'),
    path('home/book/delete/<int:id>/', views.delete_booking, name='delete_booking'),
]
