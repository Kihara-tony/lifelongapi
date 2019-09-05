from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import ServicesViewSet,BusinessViewSet,HousingViewSet

urlpatterns=[
    url('^$',views.housing,name = 'housing'),
    url(r'^services/', views.services, name='services'),
    url(r'^business/',views.business,name='business'),

# To add data

    url(r'addhousing/',views.addhousing,name = 'addhousing'),
    url(r'addservices/',views.addservices,name = 'addservices'),
    url(r'addbusiness/',views.addbusiness,name = 'addbusiness'),

# To help in get request from the database by the user

    url('services/', ServicesViewSet.as_view({'get':'list','post':'create'})),
    url('business/', BusinessViewSet.as_view({'get':'list','post':'create'})),
    url('housing/', HousingViewSet.as_view({'get':'list','post':'create'})),
    
# To help in posting updating and deleting of data

    url('services/<int:pk>', ServicesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url('business/<int:pk>', BusinessViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url('housing/<int:pk>', HousingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]