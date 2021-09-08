from django.urls import path

from .views import add_weather, weather_list, summary_list, delete_summary


urlpatterns = [
    path('add/', add_weather, name='add-weather'),
    path('list/', weather_list, name='weather-list'),
    path('summary/list/', summary_list, name='summary-list'),
    path('summary/<int:summary_id>/delete/', delete_summary, name='delete-summary'),
] 