from graphene import ObjectType, relay

from graphene_django.types import DjangoObjectType
from cookbook.ingredients.models import Category, Ingredient
from graphene_django.filter import DjangoFilterConnectionField

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ["name", "ingredients"]
        interfaces = (relay.Node, )

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name'  : ['exact', 'icontains', 'istartswith'],
            'notes' : ['exact', 'icontains'],
            'category' : ['exact'],
            'category__name' : ['exact']
        }
        interfaces = (relay.Node, )

class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)

class Mutation(ObjectType):
    pass