
from django.contrib import admin
from django.urls import path
from backend import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('register/', views.register.as_view(), name='register'),
    path('doctors_list/', views.get_doctors_list.as_view(), name='doctors_list'),
    path('cultivators_list/', views.get_cultivators_list.as_view(), name='cultivators_list'),
    path('patient_cultivators_list/', views.get_patient_cultivators_list.as_view(), name='cultivators_list'),
]
