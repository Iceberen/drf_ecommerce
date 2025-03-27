from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.shop.views import (
    CategoriesView, ProductView, ProductsView, ProductsByCategoryView, ProductsBySellerView, ReviewViewSet
)


router_api = DefaultRouter()
router_api.register(
    r"products/(?P<post_id>\d+)/review",
    ReviewViewSet,
    basename="review"
)

urlpatterns = [
    path("categories/", CategoriesView.as_view()),
    path("categories/<slug:slug>/", ProductsByCategoryView.as_view()),
    path("sellers/<slug:slug>/", ProductsBySellerView.as_view()),
    path("products/", ProductsView.as_view()),
    path("products/<slug:slug>/", ProductView.as_view()),
    path("", include(router_api.urls)),
]
