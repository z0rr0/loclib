from django.conf import settings
from django.db.models import Count

from .models import Tag


class BlogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # user staff flag
        request.is_staff_user = request.user.is_authenticated and request.user.is_staff

        # tags cloud
        request.tags = Tag.objects.values('name').annotate(count=Count('books__pk')).order_by('-count')

        # settings configuration params
        request.settings_params = {
            'github': settings.GITHUB_LINK,
            'title': settings.APP_TITLE,
            'lang': settings.LANGUAGE_CODE.split('-', 1)[0],
            # 'version': settings.VERSION,
            'version': 'v0.0.1',
        }
        response = self.get_response(request)
        return response
