from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('finches/', views.FinchList.as_view(), name="finch-list"),
    path('finches/new/', views.FinchCreate.as_view(), name="finch_create"),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finch_update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finch_delete"),
    path('finches/<int:pk>/pictures/new/', views.PictureCreate.as_view(), name="picture_create"),
    path('albums/<int:pk>/<int:picture_pk>/', views.AlbumPictureAssoc.as_view(), name="album_picture_assoc"),
    
]