from django.contrib import admin
# from django.utils.translation import gettext_lazy as _

from .models import Author, Publisher, Book, Tag, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'homepage', 'created']
    search_fields = ('name',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'homepage', 'created']
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ('title', 'path')


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'created']
    search_fields = ('message',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
