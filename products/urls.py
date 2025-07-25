from django.urls import path
from .views import (ListCategoryView, CreateCategoryView, UpdateCategoryView,
                    DeleteCategoryView, ListProducView, CreateProductView,
                    UpdateProductView, DeleteProductView, DetailProducView
)



urlpatterns = [
    path("categories/", view=ListCategoryView.as_view(), name="category_list"),
    path("categories/create/", view=CreateCategoryView.as_view(), name="category_create"),
    path("category/update/<pk>/", view=UpdateCategoryView.as_view(), name="category_update"),
    path("category/delete/<pk>/", view=DeleteCategoryView.as_view(), name="category_delete"),

    # products
    path("", view=ListProducView.as_view(), name="product_list"),
    path("create/", view=CreateProductView.as_view(), name="product_create"),
    path("update/<pk>/", view=UpdateProductView.as_view(), name="product_update"),
    path("delete/<pk>", view=DeleteProductView.as_view(), name="product_delete"),
    path("<pk>", view=DetailProducView.as_view(), name="product_detail"),
]