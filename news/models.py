from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    try:
        editor = Editor.objects.get(email = 'moha@gmail.com')
        print('Editor found')
    except DoesNotExist:
        print('Editor was not found')
