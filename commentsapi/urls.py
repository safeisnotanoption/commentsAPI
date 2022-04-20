from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
    path('articles/<int:article_id>/comments/', views.CommentList.as_view()),
    path('articles/<int:article_id>/comments/<int:pk>/', views.CommentDetail.as_view()),
    path('articles/<int:article_id>/comments/<int:pk>/get_children', views.CommentsChildrenList.as_view()),
]
