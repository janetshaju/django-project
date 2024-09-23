import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from myapp.models import Book, Category

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Get or create the category instance
                category_name = row['category']
                category, created = Category.objects.get_or_create(name=category_name)

                # Convert the published_date to the correct format
                published_date_str = row['published_date']
                try:
                    # Try parsing as DD/MM/YYYY
                    published_date = datetime.strptime(published_date_str, "%d/%m/%Y").date()
                except ValueError:
                    try:
                        # If that fails, try parsing as MM/DD/YYYY
                        published_date = datetime.strptime(published_date_str, "%m/%d/%Y").date()
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f"Invalid date format for '{published_date_str}'"))
                        continue  # Skip this record if the date format is invalid

                # Create the book record
                Book.objects.create(
                    title=row['title'],
                    authors=row['authors'],
                    publisher=row['publisher'],
                    published_date=published_date,  # Use the converted date
                    category=category,  # Use the Category instance
                    distribution_expense=row['distribution_expense']
                )

                # Output success message for each book imported
                self.stdout.write(self.style.SUCCESS(f"Book '{row['title']}' imported successfully."))
