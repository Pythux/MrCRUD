from django.contrib import admin
from myapp.models import Post
from guardian.admin import GuardedModelAdmin


# With object permissions support
class PostAdmin(GuardedModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
