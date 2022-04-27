from django.urls import path
from . import views

app_name="wj9_io"
urlpatterns=[
    path("", views.index, name='index')
]