from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category,Product

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаление всех продуктов и категорий...")
        Category.objects.all().delete()
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("БД очищена!"))

        self.stdout.write("Загрузка фикстур...")
        call_command('loaddata', 'categories')
        call_command('loaddata', 'products')
        self.stdout.write(self.style.SUCCESS("Фикстуры загружены!"))