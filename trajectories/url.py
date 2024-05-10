from django.urls import path
from trajectories.views import TrajectoriesApiView, LastLocationApiView

urlpatterns_trajectories = [
    path('v1/trajectories/<int:taxi_id>/<str:date>', TrajectoriesApiView.as_view()),
    path('v1/trajectories/', LastLocationApiView.as_view()),
]