from django.contrib import admin

from .models import Candidate, Login, Registration, Election,Vote

# Register your models here.
admin.site.register(Registration)
admin.site.register(Login)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote)
