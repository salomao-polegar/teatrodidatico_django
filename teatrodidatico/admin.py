from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from teatrodidatico.models import *

# Registro dos modelos dentro de admin

# Classes

class FotosInline(admin.TabularInline): # Usada para mostrar todas as fotos do Espetáculo
    model = Fotos
    readonly_fields = ('image_preview',)
    fields = ('foto', 'image_preview',)
    extra=0
    def image_preview(self, obj):
        if obj.foto:
            return mark_safe(f'<img width="100" height="100" style="object-fit:contain" src="{obj.foto.url}"/>')
        else:
            return '(No image)'
    image_preview.short_description = "Prévia"

class ImagePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        try:
            img_html = mark_safe(f'<br><img width="100" height="100" style="object-fit:contain" src="{value.url}"/>')
        except AttributeError:
            img_html = mark_safe(f'')
        return f'{input_html}{img_html}'

class EspetaculoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Espetaculo
        fields = '__all__'
    foto_principal = forms.ImageField(widget=ImagePreviewWidget,)

class IntegranteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Integrantes
        fields = '__all__'
    foto = forms.ImageField(widget=ImagePreviewWidget,)

class ListandoEspetaculo(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativo') #Configura o display
    list_display_links = ('id', 'nome',) #Configura quais itens do display são links
    list_editable = ('ativo',) # Configura os campos editáveis
    search_fields = ('nome',) # configura os campos pesquisáveis
    list_per_page = 12 # 12 por página
    
    inlines = [
        FotosInline,
    ]
    #print ('\n\n\n\n'+inlines+'\n\n\n\n\n')
    form = EspetaculoForm



class ListandoAgenda(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data', 'ativo')
    list_display_links = ('id', 'titulo', 'data')
    list_editable = ('ativo',)
    search_fields = ('titulo',)
    list_per_page = 12

class ListandoEvento(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativo') 
    list_display_links = ('id', 'nome')
    list_editable = ('ativo',)
    search_fields = ('nome',)
    list_per_page = 12 

class ListandoCurriculo(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'premio', 'data', 'get_tipo', 'ativo')
    list_display_links = ('id', 'descricao', 'premio')
    list_editable = ('ativo',)
    search_fields = ('titulo',)
    list_per_page = 12 
    
    def get_tipo(self, obj):
        return obj.get_tipo_display()
    get_tipo.short_description = "Tipo" # Altera o título da coluna para esse campo

class ListandoIntegrantes(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo')
    list_display_links = ('nome', 'descricao')
    list_editable = ('ativo',)
    search_fields = ('nome',)
    list_per_page = 12

    form = IntegranteForm


class ProgramaCursoInline(admin.TabularInline): # Usada para mostrar todas as fotos
    model = ProgramaCurso
    fields = ('titulo', 'conteudo','ativo')
    extra=1

class TextosInline(admin.TabularInline): # Usada para mostrar todas as fotos
    model = Textos
    fields = ('nome', 'autor', 'resumo', 'arquivo', 'ativo')
    extra=1
   
    

class ListandoCursos(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ativo')
    list_display_links = ('nome', 'descricao')
    list_editable = ('ativo',)
    search_fields = ('nome',)
    list_per_page = 12

    inlines = [
        ProgramaCursoInline,
        TextosInline
    ]


    

# Registro das classes no admin do site

admin.site.register(Espetaculo, ListandoEspetaculo)
admin.site.register(Agenda, ListandoAgenda)
admin.site.register(Evento, ListandoEvento)
admin.site.register(Curriculo, ListandoCurriculo)
admin.site.register(Integrantes, ListandoIntegrantes)
admin.site.register(Cursos, ListandoCursos)