# Source: https://qbox.io/blog/elasticsearch-python-django-database
from django.core.management.base import BaseCommand

# python manage.py sample
class Command(BaseCommand):
	title = "Unit"
	help = "Sample Only"
	def handle(self, *args, **options):
		print "Start"
		self.clear()
		self.make_data()
		print "END"
	def make_data(self):
		print "Hello World"

	def clear(self):
		print "Everything Clear?"