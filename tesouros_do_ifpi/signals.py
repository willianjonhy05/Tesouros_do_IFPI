from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario, Voto, Categoria


@receiver(post_save, sender=Usuario)
def criar_votos_iniciais(sender, instance, created, **kwargs):

    if instance.concorda_termos:

        # evita duplicação
        votos_existentes = Voto.objects.filter(usuario=instance).exists()

        if not votos_existentes:

            categorias = Categoria.objects.all()

            votos = [
                Voto(usuario=instance, categoria=categoria)
                for categoria in categorias
            ]

            Voto.objects.bulk_create(votos)