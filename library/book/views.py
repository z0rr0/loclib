from django.conf import settings
from django.db.models import Q
from django.utils.translation import gettext as _
from django.views.generic import DetailView, ListView

from .models import Book


class BookListView(ListView):
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = settings.BOOKS_PER_PAGE
    template_name = 'book/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        search = self.request.GET.get('search')
        tag = self.kwargs.get('tag')
        if search:
            info = _('Search result for keyword')
            context['info'] = f'{info} "{search}"'
        elif tag:
            info = _('Search by tag')
            context['info'] = f'{info} "{tag}"'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search is not None:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(path__icontains=search) |
                Q(tags__name__iexact=search)
            )
        tag = self.kwargs.get('tag')
        if tag is not None:
            queryset = queryset.filter(tags__name__iexact=tag)
        return queryset


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    context_object_name = 'post'
    template_name = 'book/detail.html'
