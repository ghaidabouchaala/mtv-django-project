from django.contrib import admin
from d_app.models import Topic,AccessRecord, Webpage
# Register your models here.


admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

