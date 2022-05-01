from django.core.management.base import BaseCommand
from products.models import Brand, Category, Subcategory, Product

default_brand = [
    {
        "name": "Pepsico",
        "status": "Disponible",
    },
    {
        "name": "Coke",
        "status": "Disponible",
    },
    {
        "name": "Bimbo",
        "status": "Disponible",
    }
]

default_category = [
    {
        "name": "Plasticos",
        "status": "Disponible",
    },
    {
        "name": "Carton",
        "status": "Disponible",
    },
    {
        "name": "Papel",
        "status": "Disponible",
    }
]

default_subcategory = [
    {
        "name": "SubPlasticos",
        "status": "Disponible",
    },
    {
        "name": "SubCarton",
        "status": "Disponible",
    },
    {
        "name": "SubPapel",
        "status": "Disponible",
    }
]