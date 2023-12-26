from django.contrib import admin
from usuario.models import usuario

@admin.register(usuario)

class usuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')