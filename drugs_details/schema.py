
import  graphene
from graphene_django import DjangoObjectType
from .models import Drug


class DrugType(DjangoObjectType):
    class Meta:
        model = Drug
        fields = [ "id", "name", "description", "sku", "price", "image"]
    

class Query(graphene.ObjectType):
  # Queries for the Drug model
  drugs = graphene.List(DrugType)

  def resolve_drugs(self, info, **kwargs):
    return Drug.objects.all()



"""Creating Mutation for Modifying the database"""

""" create Drug """
class CreateDrug(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        sku = graphene.String()
        price = graphene.Int()
        image = graphene.String()
    
    ok = graphene.Boolean()
    drug = graphene.Field(DrugType)

    def mutate(self, info, name, description, sku, price, image):
        drug = Drug(
            name=name, 
            description=description,
            sku=sku,
            price=price,
            image=image
        )
        drug.save()
        return CreateDrug(ok=True,  drug=drug)

""" updating the drugs in the database """
class UpdateDrug(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        description = graphene.String()
        sku = graphene.String()
        price = graphene.Int()
        image = graphene.String()

    ok = graphene.Boolean()
    drug = graphene.Field(DrugType)

    def mutate(self, info, id, name, description, sku, price, image):
        drug = Drug.objects.get(id=id)
        drug.name = name
        drug.description = description
        drug.sku = sku
        drug.price = price
        drug.image = image

        drug.save()
        return UpdateDrug(ok=True,  drug=drug)


""" Deleting Drug by its Id """
class DeleteDrug(graphene.Mutation):
  class Arguments:
    id = graphene.String()

  ok = graphene.Boolean()

  def mutate(self, info, id):
    drug = Drug.objects.get(id=id)
    drug.delete()
    return DeleteDrug(ok=True)



class Mutation(graphene.ObjectType):
  create_drug = CreateDrug.Field()
  update_drug = UpdateDrug.Field()
  delete_drug = DeleteDrug.Field()






schema = graphene.Schema(query=Query, mutation=Mutation)