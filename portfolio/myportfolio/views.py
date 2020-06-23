# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def project(request, project_id):
    project = Project.objects.get(id=project_id)
    projects = Project.objects.all()
    return render(request, 'single-portfolio.html', {'project': project , 'projects': projects})