from django.urls import path

from .views import BookDetailView, BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('<int:pk>', BookDetailView.as_view(), name='detail'),
    path('tag/<slug:tag>', BookListView.as_view(), name='tag_filter'),
]
