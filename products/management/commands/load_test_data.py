from django.core.management.base import BaseCommand
from products.models import Brand, Tag, Subtag, Product

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

default_tag = [
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

default_subtag = [
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