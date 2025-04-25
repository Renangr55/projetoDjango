from django.contrib import admin
from .models import Usuario, Professor, Disciplina, Ambiente
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UsuarioAdmin(UserAdmin):
    list_display = ['username','biografia']
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos',{'fields': ('telefone','biografia','idade')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos',{'fields': ('telefone','biografia','idade')})
    )



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Ambiente)