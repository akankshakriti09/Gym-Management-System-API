from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Creating Routing Object
router = DefaultRouter()

# Register ViewSet with Router
router.register('gyms', views.GymModelViewSet) 
router.register('trainers', views.TrainerModelViewSet)
router.register('clients',views.ClientModelViewSet) 
router.register('workouts',views.WorkoutSessionModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', obtain_auth_token)
]
