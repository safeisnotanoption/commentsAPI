from rest_framework import generics
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return self.queryset.filter(article__pk=article_id, depth__lt=0)

    def perform_create(self, serializer):
        article_id = self.kwargs['article_id']
        serializer.save(article_id=article_id)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentsChildrenList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        parent_id = self.kwargs['pk']
        return Comment.objects.filter(depth=parent_id)
