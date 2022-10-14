from django.urls import path
from fullapp import views

urlpatterns = [
    
    path('',views.index,name="index")
]