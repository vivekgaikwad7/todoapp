from django.urls import URLPattern, path 
from .import views 
Urlpatterns=[
    path('',views.index)
]

