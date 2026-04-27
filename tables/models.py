from django.db import models

from common.models import BaseModel, DeletedModel


class TableType(models.TextChoices):
    STANDARD = 'standard'
    BADIIY = 'badiiy'
    ILMIY = 'ilmiy'


class Author(BaseModel, DeletedModel):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'tables_authors'
        ordering = ['-birth_date']


# id -> primary key-serial,title->varchar(255),description->text,author-varchar,type-> varchar
class Tables(BaseModel, DeletedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.ManyToManyField(
        Author,
        db_table='book_authors')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=TableType.choices, default=TableType.STANDARD)

    def __str__(self):
        return f'{self.title}'
from common.models import BaseModel, DeletedModel


class TableType(models.TextChoices):
    STANDARD = 'standard'
    BADIIY = 'badiiy'
    ILMIY = 'ilmiy'


class Author(BaseModel, DeletedModel):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name or ""} {self.last_name}'

    class Meta:
        db_table = 'tables_authors'
        ordering = ['-birth_date']


class Table(BaseModel, DeletedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.ManyToManyField(
        Author,
        db_table='tables_authors_rel'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(
        max_length=20,
        choices=TableType.choices,
        default=TableType.STANDARD
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tables'
        ordering = ['-created_time']

    class Meta:
        db_table = 'tables'
        ordering = ['-created_time']


# CRUD -> INSERT,SELECT,UPDATE,DELETE

"""
sql

insert into authors (first_name, last_name, birth_date) VALUES ("sasas", "sasasa", "2024-2-1");

SELECT * from authors;

UPDATE authors SET first_name = ?, last_name = ?, birth_date = ? where id = ?;

DELETE from authors where id = ?;
"""

"""
python manage.py shell

CRUD

python code -> ORM -> sql ogirib cursor.excute() (database ga yoziladi)
python code SELECT: -> ORM -> sql  cursor.excute()
python object  <- ORM <- sql
"""
