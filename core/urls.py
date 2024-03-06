
from django.contrib import admin
from django.urls import path, include
from apps.sitios.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('sitios/', include('apps.sitios.urls')),

]
