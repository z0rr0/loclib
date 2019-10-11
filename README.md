# LocLlib

Local Library is web interface for personal electronic books.

It is usefull if you have many e-books and want:

1. search some books by category (tags)
1. search all books by an author
1. search all books by a publisher
1. add notes/images/links/files for a book

## Prepare database

```sh
cd library
python manage.py migrate
python manage.py createsuperuser
```

## Usage

Run local dev web-server:

```sh
cd library
python manage.py runserver
```