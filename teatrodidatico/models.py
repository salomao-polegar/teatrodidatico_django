from django.db import models
from django.utils.html import escape


CLASSIFICACAO = [
        ('0', "Livre"),
        ('10', "Recomendado para maiores de 10 anos"),
        ('12', "Recomendado para maiores de 12 anos"),
        ('14', "Recomendado para maiores de 14 anos"),
        ('16', "Recomendado para maiores de 16 anos"),
        ('18', "Recomendado para maiores de 18 anos"),
    ]

class Espetaculo(models.Model):
    """
        Espetáculos teatrais do grupo
    """    
    nome = models.CharField(max_length=100)
    sinopse = models.TextField() 
    atores = models.CharField(max_length=100)
    direcao = models.CharField(max_length=100, verbose_name="Direção")
    trilha_sonora = models.CharField(max_length=100, blank=True, null=True)
    confeccao = models.CharField(max_length=100, verbose_name="Confecção")
    duracao = models.CharField(max_length=30, verbose_name="Duração")
    classificacao = models.CharField(max_length=2, choices=CLASSIFICACAO, verbose_name="Classificação indicatica")
    agradecimentos = models.TextField(blank=True)
    foto_principal = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True, null=True)
    video = models.CharField(max_length=200, verbose_name="Vídeo (link do youtube)", blank=True, null=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

    def image_tag(self):
        return u'<img src="%s" />' % escape(self.foto_principa.url)
    image_tag.short_description = 'Imagem Principal'
    image_tag.allow_tags = True

class Agenda(models.Model):
    """ 
    Agenda de eventos do grupo.
    """
    titulo = models.CharField(max_length=100, verbose_name="Título")
    espetaculo = models.ForeignKey(Espetaculo, on_delete=models.PROTECT, blank=True, null=True)
    data = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    valor = models.CharField(max_length=50)
    duracao = models.CharField(max_length=10, verbose_name="Duração")
    idade = models.CharField(max_length=20, choices=CLASSIFICACAO, blank=True, null=True)
    data_inicial = models.DateField()
    data_final = models.DateField()    
    inscricao = models.CharField(max_length=200, verbose_name="Link para inscrição, se houver", blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Evento(models.Model):
    """
    Eventos que o grupo participou, para integração com o currículo
    """
    nome = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Curriculo(models.Model):
    """ 
    Currículo do grupo, dividido entre os eventos (festivais, mostras, feiras) que o grupo participou e os prêmios que o grupo recebeu.
    """
    TIPOS = [
        ('1', 'Currículo'),
        ('2', "Premio"),
    ]

    data = models.DateField()
    descricao = models.TextField(verbose_name="Descrição")
    tipo = models.CharField(max_length=1, choices=TIPOS, verbose_name="Tipo")
    premio = models.CharField(max_length=100, verbose_name="Prêmio", blank=True, null=True)
    evento =  models.ForeignKey(Evento, on_delete=models.PROTECT, blank=True, null=True)
    espetaculo = models.ForeignKey(Espetaculo, on_delete=models.PROTECT, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        if self.tipo == '1':
            return self.descricao
        if self.tipo == '2':
            return self.premio
        return ""
    
class Fotos(models.Model):
    """ 
    Fotos dos espetáculos.
    """
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/')
    espetaculo = models.ForeignKey(Espetaculo, on_delete=models.PROTECT)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.foto)

class Integrantes(models.Model):
    """ 
    Integrantes do grupo.
    """
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

class Cursos(models.Model):
    """
    Cursos ministrados pelo grupo
    """
    MODALIDADES = [
        ("P","Atividade presencial"),
        ("O","Atividade online")
    ]
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    modalidade = models.CharField(max_length=200, choices=MODALIDADES)
    programacao = models.TextField()
    data_inscricao_inicial = models.DateField()
    data_inscricao_final = models.DateField()
    foto_principal = models.ImageField(upload_to='fotos/%d/%m/%Y/')
    local = models.CharField(max_length=200, null=True, blank=True)
    observacoes = models.CharField(max_length=200, null=True, blank=True)
    ativo = models.BooleanField(default=True)


class ProgramaCurso(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)


class Textos(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=200, null=True, blank=True)
    resumo = models.TextField()
    arquivo = models.FileField(upload_to='files/%d/%m/%Y/')
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
