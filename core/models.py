from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Convenio(models.Model):
    
    ESTADOS = [
        ("Vigente", "Vigente"),
        ("Finalizado", "Finalizado"),
        ("Suspendido", "Suspendido"),
    ]
    TIPOS_ACUERDO = [
        ("Convenio Marco", "Convenio Marco"),
        ("Convenio Específico", "Convenio Específico"),
        ("Memorándum de Entendimiento", "Memorándum de Entendimiento"),
        ("Carta de Intención", "Carta de Intención"),
        ("Protocolo", "Protocolo"),
        ("Acuerdo de Cooperación", "Acuerdo de Cooperación"),
        ("Otro", "Otro"),
    ]
    TEMAS = [
        ("Comercio", "Comercio"),
        ("Turismo", "Turismo"),
        ("Cultura", "Cultura"),
        ("Educación", "Educación"),
        ("Ambiente", "Ambiente"),
        ("Salud", "Salud"),
        ("Energía", "Energía"),
        ("Ciencia y Tecnología", "Ciencia y Tecnología"),
        ("Cooperación Institucional", "Cooperación Institucional"),
        ("Otro", "Otro"),
    ]
    
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    
    actores = models.ManyToManyField(Actor, related_name="convenios")
    
    
    pais = models.CharField(max_length=100)
    
    
    tipo_acuerdo = models.CharField(
    max_length=40,
    choices=TIPOS_ACUERDO
    )
    
    tema = models.CharField(
    max_length=40,
    choices=TEMAS
)
    
    fecha_firma = models.DateField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS
    )

    descripcion = models.TextField(blank=True)

    enlace_documento = models.URLField(
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f"{self.provincia} - {self.pais} ({self.fecha_firma.year})"