from django.urls import path
from . import views
urlpatterns = [
path('', views.HomePageView.as_view(), name='home'),
path('phis/',  views.new_page,  name="my_function"),
]
