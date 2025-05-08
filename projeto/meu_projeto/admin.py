from django.contrib import admin
from .models import Usuario, Professor, Disciplina, Ambiente
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    list_display = ['username','biografia']
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais',{
            'fields': ('telefone','biografia','idade')
            }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações adicionais',{
            'fields': ('telefone','biografia','usuario'),
        }),
    )



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Ambiente)