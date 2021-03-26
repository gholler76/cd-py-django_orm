from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors is related name to Author

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.first_name + " " + self.last_name
