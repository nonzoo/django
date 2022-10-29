from django.db import models
from django.urls import reverse #to reference an object by its URL template name.

class Post(models.Model): #provides access to everything within django.db.models.Models
    title = models.CharField(max_length=200) #CharField, limited to 200 characters
    
    author = models.ForeignKey( #ForeignKey field, allows for a many-to-one relationship
        'auth.User', #One user can be the author of many blog posts but not reversible
        on_delete=models.CASCADE, #For all many-to-one relationships we must specify an on_delete option
    )

    body = models.TextField() #TextField, automatically expand as needed to fit the user’s text
    
    
    def __str__(self): #To provide a human-readable version of the model in the admin or Django shell
        return self.title

    def get_absolute_url(self): #Tells Django how to calculate the canonical URL for our model object
        return reverse('post_detail', kwargs={'pk': self.pk})

    

