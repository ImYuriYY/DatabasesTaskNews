from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=200)
    publishers = models.ManyToManyField('Publisher')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'





class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
            return f'{self.name}'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'






class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_date = models.DateField(blank=True, default=date.today)


    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
