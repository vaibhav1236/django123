from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [

    path('', views.index, name="Index"),
    path('home/', views.home, name='Home'),
    path('Contact/', views.contact, name='Contact'),
    path('Services/', views.services, name='service'),
    path('Gul/', views.Gul, name='Gul'),
    path('Milk/', views.Milk, name='Milk'),
    path('Agree/', views.Agree, name='Agree'),
    path('about/', views.about, name='About'),
]
