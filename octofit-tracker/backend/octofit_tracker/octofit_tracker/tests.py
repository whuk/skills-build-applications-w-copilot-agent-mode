import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Activity, Leaderboard, Team, User, Workout


class OctofitCollectionApiTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='marvel team',
            universe='Marvel',
            description='Earth\'s mightiest workout heroes.',
        )
        self.user = User.objects.create(
            name='Peter Parker',
            email='spiderman@octofit.dev',
            hero_alias='Spider-Man',
            team=self.team,
        )
        Activity.objects.create(
            user=self.user,
            activity_type='Web Swing Cardio',
            duration_minutes=45,
            calories_burned=520,
        )
        Leaderboard.objects.create(user=self.user, points=980, rank=2)
        Workout.objects.create(
            user=self.user,
            workout_name='Spider Agility Circuit',
            intensity='high',
            target_minutes=40,
            notes='Focus on legs and core.',
        )

    def test_api_root_returns_all_collection_links(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        payload = json.loads(response.content)
        self.assertIn('users', payload)
        self.assertIn('teams', payload)
        self.assertIn('activities', payload)
        self.assertIn('leaderboard', payload)
        self.assertIn('workouts', payload)

    def test_users_collection_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_teams_collection_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_activities_collection_endpoint(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_leaderboard_collection_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_workouts_collection_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)