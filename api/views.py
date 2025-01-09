from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import IpoInfo
from .serializers import IpoInfoSerializer

# Create your views here.
class IndexView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
    
@permission_classes([AllowAny])    
class IPOInfoView(APIView):
    def get(self, request):
        ipo_info = IpoInfo.objects.all()
        serializer = IpoInfoSerializer(ipo_info, many=True)
        return Response(serializer.data)