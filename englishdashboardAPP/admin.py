from django.contrib import admin
from .models import Expressao
# Register your models here.


class ExpressaoAdmin(admin.ModelAdmin):
    list_display = ('name','meaning','exemple', 'foto', 'data' , 'usuario'  )
    search_fields = ('name',)
    list_per_page = 5
    list_filter = ('usuario',)
    ordering = ('name',)

    # permite editar o campo direto
    # list_editable = ('foto',)
    
admin.site.register(Expressao,ExpressaoAdmin )