from rest_framework.response import Response
from rest_framework.decorators import api_view
from nomad.models import Vendor
from .serializers import VendorSerializer


@api_view(['GET'])
def getData(request):
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addVendor(request):
    serializer = VendorSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

