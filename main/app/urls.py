from django.urls import path
from . import views
from django.conf import settings
from app import views
 
urlpatterns = [
    path('cust', views.getCust),
    # path('', views.stripe_webhook, name='stripe_webhook'),
    # path('post/', views.postFood),
]