from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

# Book: a model representing a book, with a title, publish date, and an author (foreign key)
# Author: a model representing an author of a book, one author can have multiple books

class author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=200, default='Title Goes Here')
    publish_date = models.DateField(blank = True, null = True)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null = True, blank = True)
    due_date = models.DateTimeField(null = True, blank = True)
    checked_out = models.BooleanField(default = False)

    def check_out(self, borrower):
        self.checked_out = True
        self.user = borrower
        self.due_date = datetime.datetime.now() + datetime.timedelta(days=14)
        
    def check_in(self):
        self.checked_out = False
        self.user = None
        self.due_date = None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


#The new model can have the following fields:

# book: the book that the user checked out or checked in
# user: a text field containing the name of the user that checked out or checked in the book
# checkout: a boolean indicating whether the book was checked out or checked in
# timestamp: a datetime that records when the book was checked out or in

# class book_status(models.Model):
#     book = models.CharField(max_length=200, default='Title Goes Here')
    











