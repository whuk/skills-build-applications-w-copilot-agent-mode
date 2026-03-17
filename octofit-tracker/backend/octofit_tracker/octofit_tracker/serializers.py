from bson import ObjectId
from rest_framework import serializers

from .models import Activity, Leaderboard, Team, User, Workout


class ObjectIdSafeModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
        return data


class TeamSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('id',)


class UserSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


class ActivitySerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ('id',)


class LeaderboardSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'
        read_only_fields = ('id',)


class WorkoutSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
        read_only_fields = ('id',)