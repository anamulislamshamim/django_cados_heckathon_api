from rest_framework.serializers import ModelSerializer, SerializerMethodField


from .models import (
    Advocate,
    Company,
)


class CompanyModelSerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    
    class Meta:
        model = Company
        fields = '__all__'
        
    def get_employee_count(self, obj):
        return obj.advocate_set.count()


class AdvocateModelSerializer(ModelSerializer):
    company = CompanyModelSerializer()
    class Meta:
        model = Advocate
        fields = ["username", "bio", "company"]
        