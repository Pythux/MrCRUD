from django.contrib import admin
from myapp.models import Post, MyUser
from guardian.admin import GuardedModelAdmin


# With object permissions support
class Gardian(GuardedModelAdmin):
    pass


admin.site.register(Post, Gardian)
admin.site.register(MyUser, Gardian)
