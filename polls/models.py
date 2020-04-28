from django.db import models
from datetime import datetime

class Projects(models.Model):
    project=models.CharField('Projects',max_length=200)
    description=models.CharField('Description',max_length=600)

    def __str__(self):
        return self.project

class Pictures(models.Model):
    
    category_landscape = 1
    category_people = 2
    category_random = 3
    category_wall = 4
    category_project = 5
    presentation_choices = (
    ('slide','Slide'),
    ('picture', 'Picture'),
    ('project', 'Project'),
    ('album', 'Album'),
    )
    categories = (
        (category_landscape, 'Landscape'),
        (category_people, 'People'),
        (category_random, 'Random'),
        (category_wall, 'Wall'),
        (category_project, 'Project'),
    )
    image = models.ImageField(upload_to="",
        null=True,
        blank=True)
    category = models.SmallIntegerField('Category',
        choices=categories, default=category_wall)
    tags = models.CharField('Tags', max_length=200, blank=True)   
    project = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True, blank= True)
    presentation = models.CharField(max_length=10, choices=presentation_choices, default='no')
    pub_date = models.DateTimeField('Published Date', default=datetime.now)
    title=models.CharField('Title',max_length=200)
    text=models.TextField('Text', blank=True)
    
    class Admin:
        list_display = (
            'image',
            'pub_date',
            'title',
            'text',
            'category',
            'tags'
        )
    def __unicode__(self):
        return str(self.title)