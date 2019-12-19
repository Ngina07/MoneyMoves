from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.index,name='index'),
    path('list',views.project_list,name='list'),
    path('add', views.ProjectCreateView.as_view(),name = 'add'),
    path('<slug:project_slug>',views.project_detail, name = 'detail'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)