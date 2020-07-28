from django.contrib import admin

from . models import Feed, Feed_Like, Feed_Tag, Comment, Comments_Comment, Comments_Like, Tag
# Register your models here.

admin.site.register(Feed),
admin.site.register(Feed_Like),
admin.site.register(Feed_Tag),
admin.site.register(Comment),
admin.site.register(Comments_Comment),
admin.site.register(Comments_Like),
admin.site.register(Tag)
