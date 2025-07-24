from django.urls import path
from .views import (ListCategoryView, CreateCategoryView, UpdateCategoryView,
                    DeleteCategoryView
)



urlpatterns = [
    path("categories/", view=ListCategoryView.as_view(), name="category_list"),
    path("categories/create/", view=CreateCategoryView.as_view(), name="category_create"),
    path("category/update/<pk>/", view=UpdateCategoryView.as_view(), name="category_update"),
    path("category/delete/<pk>/", view=DeleteCategoryView.as_view(), name="category_delete"),
]