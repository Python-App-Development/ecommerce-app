from cgitb import lookup

from ecommerce.drf.serializer import AllProducts
from ecommerce.inventory import models
from rest_framework import permissions, viewsets

# Create your views here.


class AllProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"
