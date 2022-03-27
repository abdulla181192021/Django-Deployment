
from django.contrib import admin
from django.urls import path
from classapp import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('classapp.urls'))
]
