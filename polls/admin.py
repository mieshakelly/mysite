from django.contrib import admin

from .models import Question
from .models import Client
from .models import Choice

admin.site.register(Question)
admin.site.register(Client)
admin.site.register(Choice)
