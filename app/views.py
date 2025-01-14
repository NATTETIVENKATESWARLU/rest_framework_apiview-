from django.shortcuts import render
from app.serializer import *
from app.models import *


#------------------------------------------------------------------------------------------------------------------------------------
from rest_framework.response import Response
from rest_framework.views import APIView

#------------------------------------------------------------------------------------------------------------------------------------
from rest_framework.viewsets import ViewSet

#------------------------------------------------------------------------------------------------------------------------------------
from rest_framework.decorators import api_view

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

# Create your views here









class Cbv_apiview(APIView):

    def get(self, request, format=None, *args, **kwargs):
        emp_id = request.GET.get("id")  # Fetch the employee ID from query parameters
        if emp_id:
            try:
                emp = Employee.objects.filter(eno__icontains=emp_id)  # Replace eno with the correct field
                if emp.exists():
                    serialize = employee_serializer(emp, many=True)
                    return Response(serialize.data)
                else:
                    return Response({"msg": "Data ID is not available"}, status=404)
            except Exception as e:
                return Response({"msg": str(e)}, status=400)
        else:
            qs = Employee.objects.all()
            serialize = employee_serializer(qs, many=True)
            return Response(serialize.data)

    def post(self,request,*args,**kwargs):
        serializ=employee_serializer(data=request.data)
        if serializ.is_valid():
            serializ.save()
            return Response({"msg":"data storede "})
        return Response(serializ.errors,status=400)
    
    
    def put(self,request,*args,**kwargs):
        
        id=request.GET.get("id") 
        if id is not None:
            emp=Employee.objects.get(eno=id)
            serializ=employee_serializer(emp,request.data)
            if serializ.is_valid():
                serializ.save()
                return Response({"masge":"put chengeged successfuly"})
            return Response(serializ.errors)
        
        return Response({"masge":"id is not there"})
    




    def patch(self,request,*args,**kwargs):
        id=request.GET.get("id") 
        if id is not None:
            emp=Employee.objects.get(eno=id)
            serializ=employee_serializer(emp,request.data,partial=True)
            if serializ.is_valid():
                serializ.save()
                return Response({"masge":"patch chengeged successfuly"})
            return Response(serializ.errors)
        
        return Response({"masge":"id is not there"})
    


    
    def delete(self,request,*args,**kwargs):
        id=request.GET.get("id")
        if id is not None:
            emp=Employee.objects.get(eno=id)
            emp.delete()
            return Response({"msg":"delete successfuly"})
        return Response({"msg":"delelte method is called"})
    





class cbv_viewset(ViewSet):
    def list(self,request):
        emp=Employee.objects.all()
        serialize=employee_serializer(emp,many=True)
        return Response(serialize.data)
        
    def create(self,reuest):
        data=reuest.data
        serialize=employee_serializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":"record created successfully"})
        
    def retrieve(self,request,pk=None):
        if pk is not None: 
            emp=Employee.objects.get(id=pk)
            serialize=employee_serializer(emp)
            return Response(serialize.data)
        
        return Response({"mgs":"data is missing"})
    
    def update(self,request,pk=None):
        if pk is not None:
            emp=Employee.objects.get(id=pk)
            serialize=employee_serializer(emp,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response({"mgs":"recored update successfuly"})
            return Response({"mgs":"all fiealds requed for update"})
        return Response({"mgs":"vekatsh update method called api user"})
    
    def partial_update(self,request,pk=None):
        if pk is not None:
            emp=Employee.objects.get(id=pk)
            serialize=employee_serializer(emp,data=request.data,partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response({"mgs":"recored update successfuly"})
            return Response({"mgs":"all fiealds requed for update"})
        return Response({"mgs":"vekatsh update method called api user"})

    
    def destroy(self,request,pk=None):
        emp=Employee.objects.get(id=pk)
        emp.delete()
        return Response({"mgs":"deleted successfuly"})
    

@api_view(["GET","POST","PUT","DELETE"])
def api_data(request):
    id=request.GET.get("id")
    if request.method=="GET":
        if id is not None:
            try:
                emp=Employee.objects.get(eno=id)
            except Exception:
                return Response({"msg":"id data is not available"})
            serialize=employee_serializer(emp)
            return Response(serialize.data)
        emp=Employee.objects.all()
        serialize=employee_serializer(emp,many=True)
        return Response(serialize.data)
    
    elif request.method=="POST":
        data=request.data
        serialize=employee_serializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"msg":"data stored successfuly"})
        return Response(serialize.errors)
    
    elif request.method=="PUT":
        id=request.GET.get("id")
        if id is not None:
            emp=Employee.objects.get(eno=id)
            serialize=employee_serializer(emp,data=request.data,partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response({"msg":"data stored successfuly"})
            return Response(serialize.errors)
        return Response({"msg":"data is not found"})
    
    elif request.method=="DELETE":
        id=request.GET.get("id")
        if id is not None:
            emp=Employee.objects.get(eno=id)
            emp.delete()
            return Response({"msg":"data deleted successfuly"})
        return Response({"msg":"data is not found"})
    return Response({"msg":"data is not found"})
    




from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin


class cbv_apiview_data(ListAPIView,CreateAPIView):
    #queryset=Employee.objects.all()
    serializer_class=employee_serializer
    def get_queryset(self):
        qs=Employee.objects.all()
        id=self.request.GET.get("id")
        if id is not None:
            qs=qs.filter(eno=id)
        return qs

class cbv_apiview_data1(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=employee_serializer

class cbv_mixin_data(CreateModelMixin,DestroyModelMixin,ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=employee_serializer
    def post(self,request,*arg,**kwargs):
        return self.create(request,*arg,**kwargs)
    def delete(self,request,*arg,**kwargs):
        return self.delete(request,*arg,**kwargs)


from rest_framework.viewsets import ModelViewSet
class cbv_mixin_data1(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=employee_serializer





