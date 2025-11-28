from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('contact/', views.contact, name='contactpage'),
    path('courses/', views.courses, name='coursespage'),
    path('blog/', views.blog, name='blogpage'),
]