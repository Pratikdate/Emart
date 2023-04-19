from rest_framework import serializers
 
from .models import product_add




#MODEL Serialisers


class product_add_serialiser(serializers.ModelSerializer):
    
    class Meta:
        
        #fields=['id','name','roll','city']
        fields='__all__'
        #read_only_fields=['name']
        model=product_add





'''
class stu_model_serialiser(serializers.ModelSerializer):
    
    class Meta:
        
        #fields=['id','name','roll','city']
        fields='__all__'
        #read_only_fields=['name']
        model=stu
        
        
        #Validation fiels in modelserialiser
    def validate_roll(self,value):
        if value >=100:
            raise serializers.ValidationError('seat full !')
        return value
    # object level validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm =='car':
            raise serializers.ValidationError('car not valid name')
        if ct=='india':
            raise serializers.ValidationError('india not valid city name')
        return data











#start

class stuserializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    
    
    
    
  # Deserializers method class

#Validator field

def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('Name should start with R')
        

class stu_de_serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    def create(self,validate_data):
        return stu.objects.create(**validate_data)
    
    
    #validation Field leval  condition for data
    def validate_roll(self,value):
        if value >=100:
            raise serializers.ValidationError('seat full !')
        return value
    # object level validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm =='car':
            raise serializers.ValidationError('car not valid name')
        if ct=='india':
            raise serializers.ValidationError('india not valid city name')
        return data

    
    
    
# serialiser for update data
class stu_update_serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
        
   ''' 

