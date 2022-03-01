from django.contrib import admin
from myapp.models import Book, Mobile, Cloth, Laptop, Shoes, Electronic

# Register your models here.

admin.site.register(Book)
admin.site.register(Mobile)
admin.site.register(Cloth)
admin.site.register(Laptop)
admin.site.register(Shoes)
admin.site.register(Electronic)

