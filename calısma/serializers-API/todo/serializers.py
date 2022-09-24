
from rest_framework import serializers
from .models import Todo, Category
from django.utils.timezone import now

class TodoSerializers(serializers.ModelSerializer):
    days = serializers.SerializerMethodField() 
    category = serializers.StringRelatedField() #?  category nin isimle gelmesi için yaptık id ile gelmesin dedik
    class Meta:
        model = Todo
        fields = "__all__"
        
    #? get_sabit gelen buraya tanımlamak istediğimiz field yazdık. buradaki days  serializersmethodfield dan geldi   
    def get_days(self, obj):
        return  (now() - obj.createDate).days
    
    #? validate_buraya modeldeki field i ya (self, value) sabit
    def validate_task(self, value):
        if value.lower() == "python":
            raise serializers.ValidationError("python can not be our task")
        return
    
        
        
class CategorySerializers(serializers.ModelSerializer):
    #? related_name deki categorys i aldık
    categorys = TodoSerializers(many=True) #? tüm Todo geldi
    # categorys = serializers.StringRelatedField(many=True) #? sadece str methodu geldi
    # categorys= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #? id leri geldi
    class Meta:
        model = Category
        fields = "__all__"