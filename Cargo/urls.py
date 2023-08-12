from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='home'),
    path ('reviews', views.AddReviews.as_view(), name='addreviews'),
    path ('reports', views.reports, name='reports'),
    path ('<int:pk>/', views.get_video, name='watch_video'),
    path ('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path ('users_reviews', views.reviews, name='reviews'),
    path ('services', views.services, name='products')
]