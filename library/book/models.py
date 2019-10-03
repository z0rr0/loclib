import json

from django.db import models
from django.utils.translation import gettext_lazy as _


class JSONField(models.TextField):
    description = _("JSON")

    def get_internal_type(self):
        return "JSONField"

    def from_db_value(self, value, expression, connection):
        return json.loads(value) if value else value

    def to_python(self, value):
        value = super().to_python(value)
        return json.dumps(value) if value else value


class CreatedUpdatedModel(models.Model):
    created = models.DateTimeField(_('created'), auto_now_add=True, blank=True)
    updated = models.DateTimeField(_('updated'), auto_now=True, blank=True)

    class Meta:
        abstract = True


class NamedModel(CreatedUpdatedModel):
    name = models.CharField(_('name'), max_length=1024)
    url = models.URLField(_('url'), max_length=4096, blank=True, null=True)
    comment = models.TextField(_('comment'), blank=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Author(NamedModel):
    class Meta(NamedModel.Meta):
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class Publisher(NamedModel):
    class Meta(NamedModel.Meta):
        verbose_name = _('publisher')
        verbose_name_plural = _('publishers')


class Tag(CreatedUpdatedModel):
    name = models.CharField(_('name'), max_length=64, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self) -> str:
        return self.name


class Book(CreatedUpdatedModel):

    LANG_RU = 'russian'
    LANG_EN = 'english'
    LANGUAGE_CHOICES = (
        (LANG_RU, _(LANG_RU.title())),
        (LANG_EN, _(LANG_EN.title())),
    )

    title = models.CharField(_('title'), max_length=4096)
    path = models.FilePathField(_('path'), max_length=4096, unique=True)
    language = models.CharField(_('language'), max_length=32, choices=LANGUAGE_CHOICES, default=LANG_RU)
    metadata = JSONField(_('metadata'), blank=True)
    isbn10 = models.CharField(_('ISBN-10'), max_length=32, blank=True)
    isbn13 = models.CharField(_('ISBN-13'), max_length=64, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL)
    publication = models.DateField(_('publication'), null=True, blank=True)
    comment = models.TextField(_('comment'), blank=True)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('title',)
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def __str__(self) -> str:
        return self.title
