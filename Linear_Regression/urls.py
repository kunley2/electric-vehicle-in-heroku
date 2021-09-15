from django.urls import path
from . import views


urlpatterns = [
    path('linear/', views.home,name='linear'),
    path('linear/output/',views.output, name='output')
    ]
