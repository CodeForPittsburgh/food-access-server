from django.core.management.base import BaseCommand, CommandError
from ._load_csv import parse_csv

class Command(BaseCommand):
    help = 'Loads Local Institutional Data'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str,
                            help='File name to be loaded into models.')

    def handle(self, *args, **kwargs):
        try:
            parse_csv(kwargs['file_name'])
            self.stdout.write(
                self.style.SUCCESS('Successfully loaded the data')
            )

        except Exception as e:
            raise e
