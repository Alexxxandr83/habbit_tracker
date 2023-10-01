from django.urls import path

from habbit_tracker_app.views import HabitListView, HabitCreateView, PublicHabitListView, HabitRetrieveView, HabitUpdateView, \
    HabitDestroyView

from habbit_tracker_app.apps import HabbitTrackerAppConfig

app_name = HabbitTrackerAppConfig.name

urlpatterns = [
    path('habits/', HabitListView.as_view(), name='habits_list'),
    path('habits/public/', PublicHabitListView.as_view(), name='public_habits_list'),
    path('habits/create/', HabitCreateView.as_view(), name='habits_create'),
    path('habits/<int:pk>/', HabitRetrieveView.as_view(), name='habit_view'),
    path('habits/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('habits/delete/<int:pk>/', HabitDestroyView.as_view(), name='habit_delete'),
]