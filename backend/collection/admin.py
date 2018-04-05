from django.contrib import admin

from collection.models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Serving)
admin.site.register(AlaCarteDish)
admin.site.register(BuffetMenu)
admin.site.register(OccursAt)
admin.site.register(Review)