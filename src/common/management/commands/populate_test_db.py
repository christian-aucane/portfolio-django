from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from fake_data.generate_fake_data import generate_fake_data
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Populate the test database with fake data and create a superuser.'

    def handle(self, *args, **options):
        # Make and run migrations
        try:
            call_command('makemigrations', interactive=False)
            call_command('migrate', interactive=False)
        except CommandError as e:
            self.stdout.write(self.style.ERROR(f'Error during migration: {e}'))
            return

        # Generate fake data
        generate_fake_data()
        self.stdout.write(self.style.SUCCESS('Fake data generated successfully.\n'))

        # Create superuser
        User.objects.create_superuser(username='admin', password='admin', email='admin@test.com')
        self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        self.stdout.write(self.style.SUCCESS('Username: admin'))
        self.stdout.write(self.style.SUCCESS('Password: admin\n'))

        self.stdout.write(self.style.SUCCESS('Test database populated successfully.'))