from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hero_alias = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    performed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f'{self.user.name} - {self.activity_type}'


class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard_entry')
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f'{self.user.name} #{self.rank} ({self.points})'


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    workout_name = models.CharField(max_length=100)
    intensity = models.CharField(max_length=20)
    target_minutes = models.PositiveIntegerField()
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f'{self.user.name} - {self.workout_name}'