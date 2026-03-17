from django.core.management.base import BaseCommand
from django.db import transaction

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    @transaction.atomic
    def handle(self, *args, **options):
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        marvel = Team.objects.create(
            name='marvel team',
            universe='Marvel',
            description='Earth\'s mightiest workout heroes.',
        )
        dc = Team.objects.create(
            name='dc team',
            universe='DC',
            description='League of justice and fitness.',
        )

        heroes = [
            {
                'name': 'Peter Parker',
                'email': 'spiderman@octofit.dev',
                'hero_alias': 'Spider-Man',
                'team': marvel,
                'activity': ('Web Swing Cardio', 45, 520),
                'workout': ('Spider Agility Circuit', 'high', 40, 'Focus on legs and core.'),
                'points': 980,
                'rank': 2,
            },
            {
                'name': 'Steve Rogers',
                'email': 'captain.america@octofit.dev',
                'hero_alias': 'Captain America',
                'team': marvel,
                'activity': ('Shield HIIT', 50, 610),
                'workout': ('Super Soldier Strength', 'high', 50, 'Upper body push and pull.'),
                'points': 1120,
                'rank': 1,
            },
            {
                'name': 'Bruce Wayne',
                'email': 'batman@octofit.dev',
                'hero_alias': 'Batman',
                'team': dc,
                'activity': ('Gotham Night Run', 60, 700),
                'workout': ('Bat Cave Conditioning', 'medium', 55, 'Conditioning and endurance.'),
                'points': 910,
                'rank': 3,
            },
            {
                'name': 'Diana Prince',
                'email': 'wonder.woman@octofit.dev',
                'hero_alias': 'Wonder Woman',
                'team': dc,
                'activity': ('Amazon Strength Training', 55, 650),
                'workout': ('Warrior Core Blast', 'high', 45, 'Core and stability.'),
                'points': 870,
                'rank': 4,
            },
        ]

        for hero in heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                hero_alias=hero['hero_alias'],
                team=hero['team'],
            )

            activity_type, duration_minutes, calories_burned = hero['activity']
            Activity.objects.create(
                user=user,
                activity_type=activity_type,
                duration_minutes=duration_minutes,
                calories_burned=calories_burned,
            )

            workout_name, intensity, target_minutes, notes = hero['workout']
            Workout.objects.create(
                user=user,
                workout_name=workout_name,
                intensity=intensity,
                target_minutes=target_minutes,
                notes=notes,
            )

            Leaderboard.objects.create(
                user=user,
                points=hero['points'],
                rank=hero['rank'],
            )

        self.stdout.write(self.style.SUCCESS('테스트 데이터 입력이 완료되었습니다.'))