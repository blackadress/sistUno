from django.contrib import admin

from .models import Cuenta_usuario, Entidad_bancaria, Usuario

# Register your models here.

admin.site.register(Cuenta_usuario)
admin.site.register(Entidad_bancaria)
admin.site.register(Usuario)