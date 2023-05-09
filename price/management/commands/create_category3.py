from django.core.management import BaseCommand

from price.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        crss = ['Oil', 'Wood']

        for i in crss:
            category = Category.objects.create(
                category_name=i,
                bank_fee=5,
                tax=10,
                profit=2

            )
            category.save()
