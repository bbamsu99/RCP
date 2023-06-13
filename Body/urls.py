from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.categories_page),
    path('tag/<str:slug>/', views.tag_page)

]
