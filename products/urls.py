from django.urls import path, re_path
from .views import *


urlpatterns = [re_path(r'^products/$', AllProductsListView.as_view()),
    re_path(r'^categories/$', AllCategoriesListView.as_view()),
    re_path(r'^products/(?P<slug>\w+)/$', ProductDetailView.as_view()),
]