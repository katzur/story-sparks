from django.urls import path
from . import views

urlpatterns = [
    path("", views.Creators.as_view(), name="creators"),
    path("add/", views.AddCreator.as_view(), name="add_creator"),
    path(
        "update/<int:pk>",
        views.UpdateCreator.as_view(), name="update_creator"),
    path(
        "delete/<int:pk>",
        views.DeleteCreator.as_view(), name="delete_creator"),
]
