
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import *
from django.core.serializers import serialize
import json

class MyViews(View):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.method = None

    def homePage(request):
        params = {"key":'value'}
        # all_objects = Person.objects.all()
        # print("objects->",all_objects)
        return render(request, "index.html",params )
    def WorkExperience(request):
        params = {}
        params_list = []
        # all_objects = list(CompanyDetails.objects.all())
        data = serialize('json', CompanyDetails.objects.all())
        json_data = json.loads(data)
        # print(type(json_data))
        for all in json_data:
            params = {}
            fields = all['fields']
            params['name'] = fields.get('name')
            params['start_date'] = fields.get('start_date')
            params['end_date'] = fields.get('end_date')
            params['desc'] = fields.get('desc')
            params_list.append(params)
        params = {}

        if request.method=='POST':
            print(request.POST)
            print("companyName->",request.POST['company_name'])
            newCompany = CompanyDetails(
                name = request.POST['company_name'],
                desc = request.POST['desc'],
            )
            if request.POST['start_date']:
                newCompany.start_date = request.POST['start_date']
            if request.POST['end_date']:
                newCompany.end_date = request.POST['end_date']
            newCompany.save()

        return render(request, "work_experience.html",{'params':params_list})


