from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email
        db.users.create_index([('email', 1)], unique=True)

        # Teams
        teams = [
            {'name': 'Marvel', 'members': ['ironman@marvel.com', 'spiderman@marvel.com', 'captain@marvel.com']},
            {'name': 'DC', 'members': ['batman@dc.com', 'wonderwoman@dc.com', 'flash@dc.com']}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Captain America', 'email': 'captain@marvel.com', 'team': 'Marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'team': 'DC'}
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {'user': 'ironman@marvel.com', 'type': 'run', 'distance': 5},
            {'user': 'spiderman@marvel.com', 'type': 'cycle', 'distance': 20},
            {'user': 'batman@dc.com', 'type': 'swim', 'distance': 2}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team': 'Marvel', 'points': 100},
            {'team': 'DC', 'points': 90}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user': 'wonderwoman@dc.com', 'workout': 'HIIT', 'duration': 30},
            {'user': 'flash@dc.com', 'workout': 'Cardio', 'duration': 45}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
