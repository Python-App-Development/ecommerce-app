from tkinter.tix import Tree
from unicodedata import name

import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecommerce.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "cat_slug%d" % n)
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    name = fake.lexify(text="prod_name_??????")
    slug = fake.lexify(text="cat_slug_??????")
    description = fake.text()
    is_active = True
    created_at = "2022-04-01 22:14:13.123456"
    updated_at = "2022-04-01 22:14:13.123456"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)


register(ProductFactory)
