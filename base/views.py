from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import (
    Advocate,
    Company,
)

from .serializers import (
    AdvocateModelSerializer,
    CompanyModelSerializer,
)


# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data=data)


@api_view(['GET', 'POST'])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if not query:
            query = ''
        
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateModelSerializer(advocates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        print(request.data)
        new_advocate = Advocate.objects.create(
            username=request.data['username'], 
            bio=request.data['bio'],
        )
        serializer = AdvocateModelSerializer(new_advocate, many=False)
        return Response(serializer.data)


class AdvocateDetail(APIView):
    def get_advocate(self, username):
        try:
            return Advocate.objects.get(username=username) 
        except Advocate.DoesNotExist:
            raise Response("User doesn't exist by this name!")
    
    def get(self, request, username, format=None):
        advocate = self.get_advocate(username)
        serializer = AdvocateModelSerializer(advocate, many=False)
        return Response(data=serializer.data)
    
    def put(self, request, username, format=None):
        advocate = self.get_advocate(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        
        advocate.save()
        
        serializer = AdvocateModelSerializer(advocate, many=False)
        
        return Response(serializer.data)

    def delete(self, request, username, format=None):
        advocate = self.get_advocate(username)
        advocate.delete()
        
        return Response("User deleted successfully!")
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def advocate_detail(request, username):
#     advocate = Advocate.objects.get(username=username)
    
#     if request.method == 'GET':
#         serializer = AdvocateModelSerializer(advocate, many=False)
#         return Response(data=serializer.data)
    
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
        
#         advocate.save()
        
#         serializer = AdvocateModelSerializer(advocate, many=False)
        
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()
        
#         return Response("User deleted successfully!")

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanyModelSerializer(companies, many=True)
    return Response(serializer.data)
    
