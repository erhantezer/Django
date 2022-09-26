from django.db.models.signals import pre_save #? kaydetmeden önce signal versin
from django.dispatch import receiver #? kaydettikten sonra signal versin
from django.template.defaultfilters import slugify #? endpointler arasına - (tire) işareti koyar
from .models import Post
from .utils import get_random_code

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code())
        
        

