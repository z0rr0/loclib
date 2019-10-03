# Generated by Django 2.2.6 on 2019-10-01 21:56

import book.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('name', models.CharField(max_length=1024, verbose_name='name')),
                ('url', models.URLField(blank=True, max_length=4096, null=True, verbose_name='url')),
                ('comment', models.TextField(blank=True, verbose_name='comment')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('name', models.CharField(max_length=1024, verbose_name='name')),
                ('url', models.URLField(blank=True, max_length=4096, null=True, verbose_name='url')),
                ('comment', models.TextField(blank=True, verbose_name='comment')),
            ],
            options={
                'verbose_name': 'publisher',
                'verbose_name_plural': 'publishers',
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('title', models.CharField(max_length=4096, verbose_name='title')),
                ('path', models.FilePathField(max_length=4096, unique=True, verbose_name='path')),
                ('language', models.CharField(choices=[('russian', 'Russian'), ('english', 'English')], default='russian', max_length=32, verbose_name='language')),
                ('metadata', book.models.JSONField(blank=True, verbose_name='metadata')),
                ('isbn10', models.CharField(blank=True, max_length=32, verbose_name='ISBN-10')),
                ('isbn13', models.CharField(blank=True, max_length=64, verbose_name='ISBN-13')),
                ('publication', models.DateField(blank=True, null=True, verbose_name='publication')),
                ('comment', models.TextField(blank=True, verbose_name='comment')),
                ('authors', models.ManyToManyField(to='book.Author')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Publisher')),
                ('tags', models.ManyToManyField(to='book.Tag')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'ordering': ('title',),
            },
        ),
    ]