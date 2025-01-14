import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","rest_framework_apiview.settings")

import django 

django.setup()

#--------------------------------------------------------------------------------------------------------------
from app.models import *
from faker import Faker
import random
data=Faker()

for i in range(10):
    en=random.randint(1,1000)
    enam=data.name()
    sal=random.choice([10000,12000,130000,140000])
    eadd=data.address()
    ra=Employee.objects.get_or_create(eno=en,ename=enam,esal=sal,eaddr=eadd)[0]
    ra.save()
    print(en,enam,sal,eadd)





