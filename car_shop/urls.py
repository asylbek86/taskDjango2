from django.urls import path
from . import views



urlpatterns = [
    path('cars/', views.car_list_view, name="cars"),
    path('cars/<int:id>/', views.car_detail_view, name="car_detail"),
    path('car_create/', views.car_create_view, name="car_create"),
    path('cars/<int:id>/update/', views.update_object_view, name="car_update"),
    path('cars/<int:id>/delete/', views.delete_object_view, name="car_delete"),
    path('cars/<int:id>/comment/', views.CarCommentView.as_view(), name="car_comment"),
]