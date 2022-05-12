from django.urls import path, re_path
import os
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = "wj9_io"
urlpatterns = [
    path("", views.index, name='index'),
    path("products/new_product/", views.new_product, name="new_product"),
    path("products/", views.products, name="products"),
    path("products/<int:product_id>", views.product, name="product")
]
# Serving all static files.
for dir in os.listdir('static'):
    for file in os.listdir(os.path.join('static', dir)):
        # Pattern: static/*(dir)/*(file)
        urlpatterns.append(re_path(r"^{0}\.{1}$".format(file.split('.')[0],
                                                    file.split('.')[1]), \
                                                        RedirectView.as_view(url=staticfiles_storage.url(os.path.join(dir, file)), permanent=True)))