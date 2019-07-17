import csv
from locations.models import FoodLocation
import os

DIR = os.path.dirname(os.path.realpath(__file__))
TEST_FILE = DIR + '/sample.csv'

BOOLEAN_FIELDS = (
    'sunday',
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'saturday',
    'snap',
    'wic',
    'fmnp',
    'fresh_produce'
)


def clean(field, value):
    if value in ('', 'NA'):
        return None
    if field in ('open_to_spec_group',):
        return value == 'OPEN'
    if field in BOOLEAN_FIELDS:
        return bool(value)
    return value


def parse_csv(file_name):
    with open(file_name, 'r') as f:
        dr = csv.DictReader(f)
        for row in dr:
            new_row = {}
            for field, value in [(f.lower(), v) for f,v in row.items()]:
                if '_time' in field and value != 'NA':  # hack fix for screwed-up times
                    value = value[0] + ':00' + value[1:]
                print(field, value)
                new_row[field] = clean(field,value)

            FoodLocation.objects.create(**new_row)


if __name__ == '__main__':
    parse_csv(TEST_FILE)
