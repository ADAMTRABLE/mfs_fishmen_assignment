from django.urls import path
from . import views
urlpatterns = [
    path('fish/', views.ArrivalCreateListView.as_view(),name='fish'),
    path('fish/<int:arrival_id>/',views.ArrivalDetailView.as_view(), name='news'),
    path('fish/<int:arrival_id>/pay/', views.PaymentCreateListView.as_view(), name='payment'),
]
