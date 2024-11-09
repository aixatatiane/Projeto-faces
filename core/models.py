from PIL import Image
from django.db import models
from django.contrib.auth.models import User

class Face(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    ocupacao = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_falecimento = models.DateField(blank=True, null=True)
    imagem = models.ImageField(upload_to='uploads/')
    postado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Face"
        verbose_name_plural = "Faces"

    def __str__(self) -> str:
        return self.nome
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Abre a imagem
        img = Image.open(self.imagem.path)

        # Define o tamanho desejado
        size = (800, 800)

        # Cria uma nova imagem quadrada com fundo branco
        new_img = Image.new("RGB", size, (255, 255, 255))  # fundo branco

        # Redimensiona a imagem mantendo a proporção
        img.thumbnail(size, Image.LANCZOS)

        # Calcula a posição para centralizar a imagem na nova imagem quadrada
        img_width, img_height = img.size
        x = (size[0] - img_width) // 2
        y = (size[1] - img_height) // 2

        # Coloca a imagem redimensionada na nova imagem quadrada
        new_img.paste(img, (x, y))

        # Salva a nova imagem
        new_img.save(self.imagem.path)
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.imagem.path)
    #     base_height = 300

    #     w_percent = (base_height / float(img.height))
    #     new_width = int((float(img.width) * float(w_percent)))
    #     img = img.resize((new_width, base_height), Image.LANCZOS)

    #     img.save(self.imagem.path)