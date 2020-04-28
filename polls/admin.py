from django.contrib import admin

from .models import Pictures, Projects

#admin.site.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title','image','presentation','category','pub_date')

admin.site.register(Pictures, PictureAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project','description')

admin.site.register(Projects, ProjectAdmin)