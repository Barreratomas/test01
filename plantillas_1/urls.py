
# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(" ",views.simple, name="simple"),
#     path("dinamico/<str:name>",views.dinamico, name="dinamico"),    
    
# ]
   

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home), 
]
