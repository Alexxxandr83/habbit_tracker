from habbit_tracker_app.models import Habit
from habbit_tracker_app.pagination import HabitPaginator
from habbit_tracker_app.serializers import HabitSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class HabitCreateView(generics.CreateAPIView):
    """View to create a habit"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListView(generics.ListAPIView):
    """View to get a list of user's habits"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    """View to get a list of public habits"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitRetrieveView(generics.RetrieveAPIView):
    """View to get a singe habit by id"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateView(generics.UpdateAPIView):
    """View to edite a singe habit by id"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyView(generics.DestroyAPIView):
    """View to delete a singe habit by id"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
