from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from new.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver y editar productos.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        Obtener lista de productos con filtro opcional por categoría
        """
        category = request.query_params.get('category', None)
        queryset = self.queryset
        
        if category:
            queryset = queryset.filter(category=category)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Crear un nuevo producto
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
