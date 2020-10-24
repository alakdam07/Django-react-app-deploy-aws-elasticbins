from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview" ),
    path('article-lists/', views.articleList, name="article-list" ),
    path('article-detail/<str:pk>/', views.articleDetail, name="single-article"),
    path('article-create/', views.articleCreate, name="article-create"),
    path('article-update/<str:pk>/', views.articleUpdate, name="article-update"),
    path('article-delete/<str:pk>/', views.articleDelete, name="article-delete")
]
