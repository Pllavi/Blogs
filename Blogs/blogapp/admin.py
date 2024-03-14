from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Subscription)
admin.site.register(Plans)

# for configuration of Category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    # class Media:
    #     js = ('https://cdn.tiny.cloud/1/{lt3gio120kbmqaw6rqlapi5gox6pkxwstap15wtckoqfrkhy}/tinymce/5/tinymce.min.js','js/script.js')



    # class Media:
    #     js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)