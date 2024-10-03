from django.urls import path
from . import views



urlpatterns = [
    path('cars/', views.CarListView.as_view(), name="cars"),
    path('cars/<int:id>/', views.CarDetailView.as_view(), name="cars_detail"),
    path('car_create/', views.CreateCarView.as_view(), name="car_create"),
    path('cars/<int:id>/update/', views.CarUpdateView.as_view(), name="car_update"),
    path('cars/<int:id>/delete/', views.CarDeleteView.as_view(), name="car_delete"),
    path('cars/<int:id>/comment/', views.CarCommentView.as_view(), name="car_comment"),
]