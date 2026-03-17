from django.contrib import admin

from .models import Activity, Leaderboard, Team, User, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'universe')
    search_fields = ('name', 'universe')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hero_alias', 'team')
    search_fields = ('name', 'email', 'hero_alias')
    list_filter = ('team',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'performed_at')
    list_filter = ('activity_type',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'points', 'rank')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'workout_name', 'intensity', 'target_minutes')
    list_filter = ('intensity',)