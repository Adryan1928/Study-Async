from django.contrib import admin
from . import models

admin.site.register(models.Categoria)
admin.site.register(models.Flashcard)
admin.site.register(models.Desafio)
admin.site.register(models.FlashcardDesafio)
