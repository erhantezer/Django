from django.db import models

#! DATABASE e verilerin kayıt edilmesi ve burada istenilen verilerin oluşturulması için yapılır sadece kayıt bölümü görülür get post  update işlemleri için views yazılır delete için otomatik admin de oluşturuluyor ama view de biz oluşturmalıyız template yani reactte bu verilerin görünmesi gerekir end pointler için


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)  #? otomatik - tire çeker endpointte de görülebilir

    class Meta:
        verbose_name = "Producttt" #? db içinde iken içine girersek Add Producttt yazacaktır Change Producttt
        verbose_name_plural = "Productttsss" #? çoğul olarak istersek databese te bu isimle görürüz db adı böyle olur hemen pProduct class altına bak django adminde
        
    def __str__(self):
        return self.name
    