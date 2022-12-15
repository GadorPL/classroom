from django.urls import path
from .views import home_view

app_name = 'classroom'
# domain.com/classroom/

urlpatterns = [
    path('', home_view, name='home') #path expects a function
]

