from django.shortcuts import render,redirect
# Create your views here.
from .models import Services,Business,Housing
from .forms import BusinessForm, ServicesForm, HousingForm,CommentForm
from .serializers import ServicesSerialiser,BusinessSerialiser,HousingSerialiser

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework_gis.filters import Filter
from rest_framework_gis.filters import InBBoxFilter

class ServicesViewSet(viewsets.ModelViewSet):

    queryset = Services.objects.all()
    serializer_class = ServicesSerialiser
    filter_backends = [InBBoxFilter,DjangoFilterBackend]
    bbox_filter_field = 'location'
    bbox_filter_include_overlapping = True
    filterset_fields = ['id','category','city']
    # permission_classes = (IsAuthenticated) 

    
    def get(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            return Response(ServicesSerialiser(a_request).data)
        except Services.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data
        serializer = ServicesSerialiser(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


    def put(self, request, pk):
        saved_services = get_object_or_404(Services.objects.all(), pk=pk)
        data = request.data.get('name')
        serialiser = ServicesSerialiser(instance=saved_services, data=data, partial=True)
        if serialiser.is_valid(raise_exception=True):
            service_saved = serialiser.save()
        return Response({"success": "Service '{}' updated successfully".format(service_saved.name)})
            
    def delete(self, request, pk):
    # Get object with this pk
        services = get_object_or_404(Services.objects.all(), pk=pk)
        services.delete()
        return Response({"message": "Services with id `{}` has been deleted.".format(pk)},status=204)
            
class BusinessViewSet(viewsets.ModelViewSet):

    queryset = Business.objects.all()
    serializer_class = BusinessSerialiser
    filter_backends = [InBBoxFilter,DjangoFilterBackend]
    bbox_filter_field = 'location'
    bbox_filter_include_overlapping = True
    filterset_fields = ['id','category','city']
    # permission_classes = (IsAuthenticated) 
    def get(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            return Response(BusinessSerialiser(a_request).data)
        except Business.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    def post(self, request):
        business = request.data.get('name')

        # Create an article from the above data
        serialiser = BusinessSerialiser(data=name)
        if serialiser.is_valid(raise_exception=True):
            business_saved = serialiser.save()
        return Response({"success": "Business '{}' created successfully".format(business_saved.name)})

    def put(self, request, pk):
        saved_businesses = get_object_or_404(Business.objects.all(), pk=pk)
        data = request.data.get('name')
        serialiser = BusinessSerialiser(instance=saved_businesses, data=data, partial=True)
        if serialiser.is_valid(raise_exception=True):
            business_saved = serialiser.save()
        return Response({"success": "house '{}' updated successfully".format(business_saved.name)})
            
    def delete(self, request, pk):
    # Get object with this pk
        business = get_object_or_404(Business.objects.all(), pk=pk)
        business.delete()
        return Response({"message": "Business with id `{}` has been deleted.".format(pk)},status=204)
            
class HousingViewSet(viewsets.ModelViewSet):

    queryset = Housing.objects.all()
    serializer_class = HousingSerialiser
    filter_backends = [InBBoxFilter,DjangoFilterBackend]
    bbox_filter_field = 'location'
    bbox_filter_include_overlapping = True
    filterset_fields = ['id','category','city']
    # permission_classes = (IsAuthenticated) 
    def get(self, request, *args, **kwargs):
        try:
            a_request = self.queryset.get(pk=kwargs["pk"])
            return Response(HousingSerialiser(a_request).data)
        except Housing.DoesNotExist:
            return Response(
                data={
                    "message": "Request with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    def post(self, request):
        house = request.data.get('name')
        # Create an article from the above data
        serialiser = HousingSerialiser(data=name)
        if serialiser.is_valid(raise_exception=True):
            house_saved = serialiser.save()
        return Response({"success": "House '{}' created successfully".format(house_saved.name)})

    
    def put(self, request, pk):
        saved_houses = get_object_or_404(Housing.objects.all(), pk=pk)
        data = request.data.get('name')
        serialiser = HousingSerialiser(instance=saved_houses, data=data, partial=True)
        if serialiser.is_valid(raise_exception=True):
            house_saved = serialiser.save()
        return Response({"success": "house '{}' updated successfully".format(house_saved.name)})

            
    def delete(self, request, pk):
    # Get object with this pk
        house = get_object_or_404(Housing.objects.all(), pk=pk)
        house.delete()
        return Response({"message": "House with id `{}` has been deleted.".format(pk)},status=204)

            
def business(request):
    business=Business.objects.all()
    return render(request,'business.html',{'business':business})

def addbusiness(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.save(commit=False)
            n.admin = request.user
            request.user.save()
            n.save()
        return redirect('business')
    else:
        form = BusinessForm()
    return render(request,'addbusiness.html', {'form': form})


def housing(request):
    housing=Housing.objects.all()
    return render(request,'housing.html',{'housing':housing})
def addhousing(request):
    if request.method == 'POST':
        form = HousingForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.save(commit=False)
            n.admin = request.user
            request.user.save()
            n.save()
        return redirect('housing')
    else:
        form = HousingForm()
    return render(request,'addhousing.html', {'form': form})


def services(request):
    services=Services.objects.all()
    return render(request,'services.html',{'services':services})
def addservices(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.save(commit=False)
            n.admin = request.user
            request.user.save()
            n.save()
        return redirect('services')
    else:
        form = ServicesForm()
    return render(request,'addservices.html', {'form': form})

def comment(request):
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comms = comment.save(commit=False)
            comms.user = request.user
            comms.save()
        return redirect('services','business','housing', request.user.profile)
def about(request):
    return render(request,'aboutus.html')