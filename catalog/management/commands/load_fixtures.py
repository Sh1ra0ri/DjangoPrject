from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        self.stdout.write("Удаление данных...")
        Product.objects.all().delete()
        Category.objects.all().delete()
