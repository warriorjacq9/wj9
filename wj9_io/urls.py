from django.urls import path,re_path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name="wj9_io"
urlpatterns=[
    path("", views.index, name='index'),
    re_path(r"^favicon\.ico$", RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'), permanent=True)),
    path("products/new_product/", views.new_product, name="new_product"),
    path("products/", views.products, name="products"),
    path("products/<int:product_id>", views.product, name="product")
]