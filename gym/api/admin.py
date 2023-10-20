from django.contrib import admin
from .models import Gym, Trainer, Client, WorkoutSession

# Register your models here.
@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['Name','Address']

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['Name','Specialization','Gym']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['Name','Age']

@admin.register(WorkoutSession)
class WorkoutSession(admin.ModelAdmin):
    list_display = ['Client','Trainer','Date', 'Duration']