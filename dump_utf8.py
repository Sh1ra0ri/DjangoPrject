# dump_utf8.py
from django.core.management import call_command
from io import StringIO


def dump_model(model, filename):
    output = StringIO()
    call_command('dumpdata', model, indent=2, stdout=output)
    data = output.getvalue()

    with open(filename, 'w', encoding='utf-8', newline='\n') as f:
        f.write(data)
    print(f"Сохранено: {filename}")


dump_model('catalog.Category', 'catalog/fixtures/categories.json')
dump_model('catalog.Product', 'catalog/fixtures/products.json')