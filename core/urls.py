from django.urls import path

from core.views import home


app_name = 'certification'


urlpatterns = [
    path('', home, name='home'),
]