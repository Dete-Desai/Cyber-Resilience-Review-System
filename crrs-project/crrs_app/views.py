import re
from django import forms
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user, allowed_users
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.views.generic import TemplateView

from .models import cseformdb
from .forms import cse_form

from .models import amg1formdb,amg2formdb,amg3formdb,amg4formdb,amg5formdb,amg6formdb,amg7formdb
from .models import ccmg1formdb,ccmg2formdb,ccmg3formdb
from .models import cmg1formdb,cmg2formdb,cmg3formdb,cmg4formdb
from .models import edmg1formdb,edmg2formdb,edmg3formdb,edmg4formdb,edmg5formdb
from .models import img1formdb,img2formdb,img3formdb,img4formdb,img5formdb
from .models import rmg1formdb,rmg2formdb,rmg3formdb,rmg4formdb,rmg5formdb
from .models import scmg1formdb,scmg2formdb,scmg3formdb,scmg4formdb
from .models import sag1formdb,sag2formdb,sag3formdb
from .models import tag1formdb,tag2formdb
from .models import vmg1formdb,vmg2formdb,vmg3formdb,vmg4formdb

from .models import ammil2formdb,ammil3formdb,ammil4formdb,ammil5formdb
from .models import ccmmil2formdb,ccmmil3formdb,ccmmil4formdb,ccmmil5formdb
from .models import cmmil2formdb,cmmil3formdb,cmmil4formdb,cmmil5formdb
from .models import edmmil2formdb,edmmil3formdb,edmmil4formdb,edmmil5formdb
from .models import immil2formdb,immil3formdb,immil4formdb,immil5formdb
from .models import rmmil2formdb,rmmil3formdb,rmmil4formdb,rmmil5formdb
from .models import scmmil2formdb,scmmil3formdb,scmmil4formdb,scmmil5formdb
from .models import samil2formdb,samil3formdb,samil4formdb,samil5formdb
from .models import tamil2formdb,tamil3formdb,tamil4formdb,tamil5formdb
from .models import vmmil2formdb,vmmil3formdb,vmmil4formdb,vmmil5formdb
from .forms import cse_form, amg_one_form

from .forms import amg_one_form,amg_two_form,amg_three_form,amg_four_form,amg_five_form,amg_six_form,amg_seven_form
from .forms import ccmg_one_form,ccmg_two_form,ccmg_three_form
from .forms import cmg_one_form,cmg_two_form,cmg_three_form,cmg_four_form
from .forms import edmg_one_form,edmg_two_form,edmg_three_form,edmg_four_form,edmg_five_form
from .forms import img_one_form,img_two_form,img_three_form,img_four_form,img_five_form
from .forms import rmg_one_form,rmg_two_form,rmg_three_form,rmg_four_form,rmg_five_form
from .forms import scmg_one_form,scmg_two_form,scmg_three_form,scmg_four_form
from .forms import sag_one_form,sag_two_form,sag_three_form
from .forms import tag_one_form,tag_two_form
from .forms import vmg_one_form,vmg_two_form,vmg_three_form,vmg_four_form

from .forms import ammil_two_form,ammil_three_form,ammil_four_form,ammil_five_form
from .forms import ccmmil_two_form,ccmmil_three_form,ccmmil_four_form,ccmmil_five_form
from .forms import cmmil_two_form,cmmil_three_form,cmmil_four_form,cmmil_five_form
from .forms import edmmil_two_form,edmmil_three_form,edmmil_four_form,edmmil_five_form
from .forms import immil_two_form,immil_three_form,immil_four_form,immil_five_form
from .forms import rmmil_two_form,rmmil_three_form,rmmil_four_form,rmmil_five_form
from .forms import scmmil_two_form,scmmil_three_form,scmmil_four_form,scmmil_five_form
from .forms import samil_two_form,samil_three_form,samil_four_form,samil_five_form
from .forms import tamil_two_form,tamil_three_form,tamil_four_form,tamil_five_form
from .forms import vmmil_two_form,vmmil_three_form,vmmil_four_form,vmmil_five_form


# Create your views here.



# BASE
@login_required(login_url='Login')
def base(request):
    return render(request, 'crrs_app/base.html')


# HOME
# Dashboard
#@login_required(login_url='Login')
#@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
#def crrshome(request):
    #return render(request, 'crrs_app/Dashboard/crrshome.html')




# CHARTS

#GoalChart
class GoalChartView(TemplateView):
    template_name = 'crrs_app/Charts/GoalChart/goalchart.html'
    
    # @login_required(login_url='Login')
    # @allowed_users(allowed_roles=['admin','cse'])
    def get_context_data(self, **kwargs):
        context = super(GoalChartView, self).get_context_data(**kwargs)
        context["charts"] = amg1formdb.objects.all()
        context['charts2'] = amg2formdb.objects.all()
        return context

# Goal Security Level Chart
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def goalssecuritylevels(request):
    amg1data = amg1formdb.objects.all() 
    amg2data = amg2formdb.objects.all()
    amg3data = amg3formdb.objects.all()
    amg4data = amg4formdb.objects.all()
    amg5data = amg5formdb.objects.all()
    amg6data = amg6formdb.objects.all()
    amg7data = amg7formdb.objects.all()
    ccmg1data = ccmg1formdb.objects.all()
    context = {
        'goalssecuritylevels1':amg1data, 'goalssecuritylevels2':amg2data, 'goalssecuritylevels3':amg3data, 'goalssecuritylevels4':amg4data, 'goalssecuritylevels5':amg5data, 'goalssecuritylevels6':amg6data, 'goalssecuritylevels7':amg7data,
         'goalssecuritylevels8':ccmg1data,
     }
    return render(request, 'crrs_app/Charts/GoalChart/goalssecuritylevels.html', context)


# MIL Security Level Chart
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def milsecuritylevels(request):
    return render(request, 'crrs_app/Charts/MILChart/milsecuritylevels.html')

# CONNECTOR PAGES
# AssetManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def assetmanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/AssetManagement/assetmanagementgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def assetmanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/AssetManagement/assetmanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def assetmanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/AssetManagement/assetmanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def assetmanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/AssetManagement/assetmanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse',])
def assetmanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/AssetManagement/assetmanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def assetmanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/AssetManagement/assetmanagementmiltable.html')


# ConfigurationChangeManagement
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def configurationchangemanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/ConfigurationChangeManagement/configurationchangemanagementgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def configurationchangemanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/ConfigurationChangeManagement/configurationchangemanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def configurationchangemanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/ConfigurationChangeManagement/configurationchangemanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def configurationchangemanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/ConfigurationChangeManagement/configurationchangemanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def configurationchangemanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/ConfigurationChangeManagement/configurationchangemanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def configurationchangemanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/ConfigurationChangeManagement/configurationchangemanagementmiltable.html')

# ControlsManagement
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cm'])
def controlsmanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/ControlsManagement/controlsmanagementgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def controlsmanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/ControlsManagement/controlsmanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def controlsmanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/ControlsManagement/controlsmanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cm'])
def controlsmanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/ControlsManagement/controlsmanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cm'])
def controlsmanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/ControlsManagement/controlsmanagementmiltable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cm'])
def controlsmanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/ControlsManagement/controlsmanagementmilform.html')

#External Dependencies
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def externaldependenciesmanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/ExternalDependenciesManagement/externaldependenciesmanagementgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def externaldependenciesmanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/ExternalDependenciesManagement/externaldependenciesmanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def externaldependenciesmanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/ExternalDependenciesManagement/externaldependenciesmanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def externaldependenciesmanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/ExternalDependenciesManagement/externaldependenciesmanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def externaldependenciesmanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/ExternalDependenciesManagement/externaldependenciesmanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def externaldependenciesmanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/ExternalDependenciesManagement/externaldependenciesmanagementmiltable.html')

# IncidentManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def incidentmanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/IncidentManagement/incidentmanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def incidentmanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/IncidentManagement/incidentmanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def incidentmanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/IncidentManagement/incidentmanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def incidentmanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/IncidentManagement/incidentmanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def incidentmanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/IncidentManagement/incidentmanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def incidentmanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/IncidentManagement/incidentmanagementmiltable.html')

# RiskManagement
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def riskmanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/RiskManagement/riskmanagementgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def riskmanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/RiskManagement/riskmanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def riskmanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/RiskManagement/riskmanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def riskmanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/RiskManagement/riskmanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def riskmanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/RiskManagement/riskmanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def riskmanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/RiskManagement/riskmanagementmiltable.html')

# ServiceContinuityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def servicecontinuitymanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/ServiceContinuityManagement/servicecontinuitymanagementgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def servicecontinuitymanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/ServiceContinuityManagement/servicecontinuitymanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def servicecontinuitymanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/ServiceContinuityManagement/servicecontinuitymanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def servicecontinuitymanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/ServiceContinuityManagement/servicecontinuitymanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def servicecontinuitymanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/ServiceContinuityManagement/servicecontinuitymanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def servicecontinuitymanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/ServiceContinuityManagement/servicecontinuitymanagementmiltable.html')

# situationalawareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def situationalawarenessgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/SituationalAwareness/situationalawarenessgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def situationalawarenessgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/SituationalAwareness/situationalawarenessgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def situationalawarenessgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/SituationalAwareness/situationalawarenessgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def situationalawarenessmilform(request):
    return render(request, 'crrs_app/ConnectorPages/SituationalAwareness/situationalawarenessmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def situationalawarenessmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/SituationalAwareness/situationalawarenessmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def situationalawarenessmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/SituationalAwareness/situationalawarenessmiltable.html')

# TrainingAwareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def trainingawarenessgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/TrainingAwareness/trainingawarenessgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def trainingawarenessgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/TrainingAwareness/trainingawarenessgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def trainingawarenessgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/TrainingAwareness/trainingawarenessgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def trainingawarenessmilform(request):
    return render(request, 'crrs_app/ConnectorPages/TrainingAwareness/trainingawarenessmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def trainingawarenessmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/TrainingAwareness/trainingawarenessmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def trainingawarenessmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/TrainingAwareness/trainingawarenessmiltable.html')

# VulnerabilityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vulnerabilitymanagementgoalform(request):
    return render(request, 'crrs_app/ConnectorPages/VulnerabilityManagement/vulnerabilitymanagementgoalform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vulnerabilitymanagementgoalssolution(request):
    return render(request, 'crrs_app/ConnectorPages/VulnerabilityManagement/vulnerabilitymanagementgoalssolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vulnerabilitymanagementgoalstable(request):
    return render(request, 'crrs_app/ConnectorPages/VulnerabilityManagement/vulnerabilitymanagementgoalstable.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vulnerabilitymanagementmilform(request):
    return render(request, 'crrs_app/ConnectorPages/VulnerabilityManagement/vulnerabilitymanagementmilform.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vulnerabilitymanagementmilsolution(request):
    return render(request, 'crrs_app/ConnectorPages/VulnerabilityManagement/vulnerabilitymanagementmilsolution.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vulnerabilitymanagementmiltable(request):
    return render(request, 'crrs_app/ConnectorPages/VulnerabilityManagement/vulnerabilitymanagementmiltable.html')

# WebDomains

#REPORTS
#CrrsReports
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def CrrsReports(request):
    return render(request, 'crrs_app/ConnectorPages/WebDomains/CrrsReports.html')

#CrrsFeedback
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def CrrsFeedback(request):
    return render(request, 'crrs_app/ConnectorPages/WebDomains/CrrsFeedback.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def domaingoalssolutions(request):
    return render(request, 'crrs_app/ConnectorPages/WebDomains/domaingoalssolutions.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def domainmilsolutions(request):
    return render(request, 'crrs_app/ConnectorPages/WebDomains/domainmilsolutions.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def domains(request):
    return render(request, 'crrs_app/ConnectorPages/WebDomains/domains.html')

# WebGoals
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def goalsforms(request):
    return render(request, 'crrs_app/ConnectorPages/WebGoals/goalsforms.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def goalstables(request):
    return render(request, 'crrs_app/ConnectorPages/WebGoals/goalstables.html')

# WebMIL

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def milforms(request):
    return render(request, 'crrs_app/ConnectorPages/WebMIL/milforms.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def miltables(request):
    return render(request, 'crrs_app/ConnectorPages/WebMIL/miltables.html')

# WebCyberSecurity
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame','ccme','cm','edme','ime','rme','scme','sae','tae','vme'])
def cseform(request):
    if request.method == 'POST':
        form = cse_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'crrs_app/ConnectorPages/WebDomains/domains.html')

    else:
        form = cse_form(request.POST)
        context = {'form':form,}
        return render(request, 'crrs_app/ConnectorPages/WebCyberSecurity/cseform.html',context)


def cybersecuritylevels(request):
    return render(request, 'crrs_app/ConnectorPages/WebCyberSecurity/cybersecuritylevels.html')


# FEEDBACK REPORTS
# GoalFeedbackReports
# AssetManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def amg1solution(request):
    context = {'amg1solution': amg1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/AssetManagement/amg1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def amg2solution(request):
    context = {'amg2solution': amg2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/AssetManagement/amg2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def amg3solution(request):
    context = {'amg3solution': amg3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/AssetManagement/amg3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def amg4solution(request):
    context = {'amg4solution': amg4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/AssetManagement/amg4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def amg5solution(request):
    context = {'amg5solution': amg5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/AssetManagement/amg5solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def amg6solution(request):
    context = {'amg6solution': amg6formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/AssetManagement/amg6solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def amg7solution(request):
    context = {'amg7solution': amg7formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/AssetManagement/amg7solution.html', context)

# ConfigurationChangeManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def ccmg1solution(request):
    context = {'ccmg1solution': ccmg1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ConfigurationChangeManagement/ccmg1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def ccmg2solution(request):
    context = {'ccmg2solution': ccmg2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ConfigurationChangeManagement/ccmg2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def ccmg3solution(request):
    context = {'ccmg3solution': ccmg3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ConfigurationChangeManagement/ccmg3solution.html', context)

# ControlsManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmg1solution(request):
    context = {'cmg1solution': cmg1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ControlsManagement/cmg1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmg2solution(request):
    context = {'cmg2solution': cmg2formdb.objects.all()}                                                     
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ControlsManagement/cmg2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmg3solution(request):
    context = {'cmg3solution': cmg3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ControlsManagement/cmg3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmg4solution(request):
    context = {'cmg4solution': cmg4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ControlsManagement/cmg4solution.html', context)

# ExternalDependenciesManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmg1solution(request):
    context = {'edmg1solution': edmg1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ExternalDependenciesManagement/edmg1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmg2solution(request):
    context = {'edmg2solution': edmg2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ExternalDependenciesManagement/edmg2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmg3solution(request):
    context = {'edmg3solution': edmg3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ExternalDependenciesManagement/edmg3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmg4solution(request):
    context = {'edmg4solution': edmg4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ExternalDependenciesManagement/edmg4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmg5solution(request):
    context = {'edmg5solution': edmg5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ExternalDependenciesManagement/edmg5solution.html', context)


# IncidentManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def img1solution(request):
    context = {'img1solution': img1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/IncidentManagement/img1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def img2solution(request):
    context = {'img2solution': img2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/IncidentManagement/img2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def img3solution(request):
    context = {'img3solution': img3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/IncidentManagement/img3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def img4solution(request):
    context = {'img4solution': img4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/IncidentManagement/img4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def img5solution(request):
    context = {'img5solution': img5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/IncidentManagement/img5solution.html', context)


# RiskManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmg1solution(request):
    context = {'rmg1solution': rmg1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/RiskManagement/rmg1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmg2solution(request):
    context = {'rmg2solution': rmg2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/RiskManagement/rmg2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmg3solution(request):
    context = {'rmg3solution': rmg3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/RiskManagement/rmg3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmg4solution(request):
    context = {'rmg4solution': rmg4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/RiskManagement/rmg4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmg5solution(request):
    context = {'rmg5solution': rmg5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/RiskManagement/rmg5solution.html', context)


# ServiceContinuityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmg1solution(request):
    context = {'scmg1solution': scmg1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ServiceContinuityManagement/scmg1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmg2solution(request):
    context = {'scmg2solution': scmg2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ServiceContinuityManagement/scmg2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmg3solution(request):
    context = {'scmg3solution': scmg3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ServiceContinuityManagement/scmg3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmg4solution(request):
    context = {'scmg4solution': scmg4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/ServiceContinuityManagement/scmg4solution.html', context)


# situationalawareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def sag1solution(request):
    context = {'sag1solution': sag1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/SituationalAwareness/sag1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def sag2solution(request):
    context = {'sag2solution': sag2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/SituationalAwareness/sag2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def sag3solution(request):
    context = {'sag3solution': sag3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/SituationalAwareness/sag3solution.html', context)

# TrainingAwareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def tag1solution(request):
    context = {'tag1solution': tag1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/TrainingAwareness/tag1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def tag2solution(request):
    context = {'tag2solution': tag2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/TrainingAwareness/tag2solution.html', context)


# VulnerabilityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmg1solution(request):
    context = {'vmg1solution': vmg1formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/VulnerabilityManagement/vmg1solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmg2solution(request):
    context = {'vmg2solution': vmg2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/VulnerabilityManagement/vmg2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmg3solution(request):
    context = {'vmg3solution': vmg3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/VulnerabilityManagement/vmg3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmg4solution(request):
    context = {'vmg4solution': vmg4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/GoalFeedbackReports/VulnerabilityManagement/vmg4solution.html', context)


# MILFeedbackReports
# AssetManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil2solution(request):
    context = {'ammil2solution': ammil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/AssetManagement/ammil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil3solution(request):
    context = {'ammil3solution': ammil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/AssetManagement/ammil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil4solution(request):
    context = {'ammil4solution': ammil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/AssetManagement/ammil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil5solution(request):
    context = {'ammil5solution': ammil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/AssetManagement/ammil5solution.html', context)


# ConfigurationChangeManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def ccmmil2solution(request):
    context = {'ccmmil2solution': ccmmil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ConfigurationChangeManagement/ccmmil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def ccmmil3solution(request):
    context = {'ccmmil3solution': ccmmil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ConfigurationChangeManagement/ccmmil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def ccmmil4solution(request):
    context = {'ccmmil4solution': ccmmil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ConfigurationChangeManagement/ccmmil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def ccmmil5solution(request):
    context = {'ccmmil5solution': ccmmil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ConfigurationChangeManagement/ccmmil5solution.html', context)


# controlsmanagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmmil2solution(request):
    context = {'cmmil2solution': cmmil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ControlsManagement/cmmil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmmil3solution(request):
    context = {'cmmil3solution': cmmil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ControlsManagement/cmmil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmmil4solution(request):
    context = {'cmmil4solution': cmmil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ControlsManagement/cmmil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def cmmil5solution(request):
    context = {'cmmil5solution': cmmil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ControlsManagement/cmmil5solution.html', context)


# ExternalDependenciesManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmmil2solution(request):
    context = {'edmmil2solution': edmmil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ExternalDependenciesManagement/edmmil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmmil3solution(request):
    context = {'edmmil3solution': edmmil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ExternalDependenciesManagement/edmmil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmmil4solution(request):
    context = {'edmmil4solution': edmmil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ExternalDependenciesManagement/edmmil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def edmmil5solution(request):
    context = {'edmmil5solution': edmmil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ExternalDependenciesManagement/edmmil5solution.html', context)


# IncidentManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def immil2solution(request):
    context = {'immil2solution': immil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/IncidentManagement/immil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def immil3solution(request):
    context = {'immil3solution': immil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/IncidentManagement/immil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def immil4solution(request):
    context = {'immil4solution': immil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/IncidentManagement/immil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def immil5solution(request):
    context = {'immil5solution': immil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/IncidentManagement/immil5solution.html', context)


# RiskManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmmil2solution(request):
    context = {'rmmil2solution': rmmil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/RiskManagement/rmmil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmmil3solution(request):
    context = {'rmmil3solution': rmmil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/RiskManagement/rmmil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmmil4solution(request):
    context = {'rmmil4solution': rmmil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/RiskManagement/rmmil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def rmmil5solution(request):
    context = {'rmmil5solution': rmmil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/RiskManagement/rmmil5solution.html', context)


# ServiceContinuityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmmil2solution(request):
    context = {'scmmil2solution': scmmil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ServiceContinuityManagement/scmmil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmmil3solution(request):
    context = {'scmmil3solution': scmmil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ServiceContinuityManagement/scmmil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmmil4solution(request):
    context = {'scmmil4solution': scmmil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ServiceContinuityManagement/scmmil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def scmmil5solution(request):
    context = {'scmmil5solution': scmmil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/ServiceContinuityManagement/scmmil5solution.html', context)


# situationalawareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def samil2solution(request):
    context = {'samil2solution': samil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/SituationalAwareness/samil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def samil3solution(request):
    context = {'samil3solution': samil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/SituationalAwareness/samil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def samil4solution(request):
    context = {'samil4solution': samil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/SituationalAwareness/samil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def samil5solution(request):
    context = {'samil5solution': samil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/SituationalAwareness/samil5solution.html', context)


# TrainingAwareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def tamil2solution(request):
    context = {'tamil2solution': tamil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/TrainingAwareness/tamil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def tamil3solution(request):
    context = {'tamil3solution': tamil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/TrainingAwareness/tamil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def tamil4solution(request):
    context = {'tamil4solution': tamil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/TrainingAwareness/tamil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def tamil5solution(request):
    context = {'tamil5solution': tamil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/TrainingAwareness/tamil5solution.html', context)


# VulnerabilityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmmil2solution(request):
    context = {'vmmil2solution': vmmil2formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/VulnerabilityManagement/vmmil2solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmmil3solution(request):
    context = {'vmmil3solution': vmmil3formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/VulnerabilityManagement/vmmil3solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmmil4solution(request):
    context = {'vmmil4solution': vmmil4formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/VulnerabilityManagement/vmmil4solution.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse'])
def vmmil5solution(request):
    context = {'vmmil5solution': vmmil5formdb.objects.all()}
    return render(request, 'crrs_app/FeedbackReports/MILFeedbackReports/VulnerabilityManagement/vmmil5solution.html', context)


# FORMS
# GoalForms
# AssetManagement

def _find_reg(pattern, str_):
    '''
        Helper method for searching for the url string
        within an http_referer
    '''
    match = re.search(pattern, str_)
    if match:
        return match.group()
    return None


def _extract_id(request_):
    '''
        Helper method for returning
        the id with http_referer string
        in the request
    '''
    try:
        if 'HTTP_REFERER' in request_.META:
            value = request_.META['HTTP_REFERER']
            temp_str = _find_reg(r'/amg1form/\d*', value)
            id = int(temp_str.split('/')[-1])
            return id
        return None
        if 'HTTP_REFERER' in request_.META:
            value = request_.META['HTTP_REFERER']
            temp_str = _find_reg(r'/amg2form/\d*', value)
            id = int(temp_str.split('/')[-1])
            return id
        return None
    except Exception:
        return None

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = amg_one_form()
        else:
            amg1form = amg1formdb.objects.get(pk=id)
            form = amg_one_form(instance=amg1form)
        return render(request, 'crrs_app/Forms/GoalForms/AssetManagement/amg1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = amg_one_form(request.POST)
        else:
            amg1form = amg1formdb.objects.get(pk=id)
            form = amg_one_form(request.POST, instance=amg1form)
        if form.is_valid():
            form.save()
            amg1_complete = request.POST.get('amg1_complete')
            amg1_incomplete = request.POST.get('amg1_incomplete')
            from pdb import set_trace
            set_trace()
            amg1_incomplete = 4 - int(amg1_complete)
            db = amg1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Services can be externally or internally focused. Examples can include: a customer-facing website such as an online payment system human resources transactions A fundamental operational resilience objective is to focus on activities to protect and sustain the identified services and assets that most directly affect the organization’s ability to achieve its mission. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization should conduct analysis of identified services (e.g., a business impact analysis) to determine the impact to the organization of the loss or disruption of each service. The results of this analysis should then be used to prioritize the organizational services. Typical work products include the  results of risk assessment and business impact analyses and prioritized list of organizational services, activities, and associated assets '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' An organization’s strategic objectives include mission, vision, and values. Effective operational resilience ensures the organization can accomplish these strategic objectives. Specific objectives are goal oriented and outline the targets the organization is attempting to reach. For example: opening 100 stores improving revenue by 14 percent The organization’s mission, vision, values, as well as the organization’s place in critical infrastructure should be readily available in company literature such as employee handbooks and annual reports. Mission, vision, values, and the organization’s place in critical infrastructure should be effectively communicated. Typical work products include the  organizational strategic objectives organizational mission, vision, values, and purpose statement'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The organization should prioritize its mission, objectives, and activities to ensure the organization remains operationally resilient. The high-value services of the organization directly support the achievement of the organization’s mission and objectives and therefore must be protected and sustained to the extent necessary to minimize disruption.Typical work products include prioritized list of organizational mission, objectives, and activities '

            db.save()

        return redirect('/amg1table')


def amg1formdelete(request, id):
    amg1form = amg1formdb.objects.get(pk=id)
    amg1form.delete()
    return redirect('/amg1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = amg_two_form()
        else:
            amg2form = amg2formdb.objects.get(pk=id)
            form = amg_two_form(instance=amg2form)
        return render(request, 'crrs_app/Forms/GoalForms/AssetManagement/amg2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = amg_two_form(request.POST)
        else:
            amg2form = amg2formdb.objects.get(pk=id)
            form = amg_two_form(request.POST, instance=amg2form)
        if form.is_valid():
            form.save()
            db = amg2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'The organization should inventory the assets (people, information, technology, and facilities) required for the delivery of the critical service. Inventories of assets may exist in multiple forms or physical locations. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Including protection and sustainment requirements in asset descriptions provides a common source for communicating and updating those requirements. The confidentiality, integrity, and availability requirements of the service are used to derive the collective protection and sustainment requirements of associated assets. Activities that implement protection and sustainment requirements often appear as processes, procedures, policies, controls, and plans. Protection requirements describe how an asset’s exposure to sources of disruption and to the exploitation of vulnerabilities must be minimized.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Asset owners are the people or organizational entities, internal or external to the organization, that have primary responsibility for the viability, productivity, and resilience of the asset. Example asset owners include:  service owners  managers and staff supervisors  organizational units  lines of business  Asset custodians are people or organizational entities, internal or external to the organization, who are responsible for satisfying the protection and sustainment requirements for the asset established by the asset owner. Example asset custodians include:  system/database administrator  facility manager  IT support organization  contractors hosting and managing data (e.g., cloud service provider) '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Physical locations of assets can be internal or external to the organization.  The location details should be sufficient enough to support the resilience requirements of the service. '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' Information flow control regulates where information is allowed to travel within an information system and between information systems.  Dedicated connections between information systems should be authorized.  The interconnection interface characteristics, security requirements, and the nature of the communication should be documented. '

            db.save()

        return redirect('/amg2table')

def amg2formdelete(request, id):
    amg2form = amg2formdb.objects.get(pk=id)
    amg2form.delete()
    return redirect('/amg2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = amg_three_form()
        else:
            amg3form = amg3formdb.objects.get(pk=id)
            form = amg_three_form(instance=amg3form)
        return render(request, 'crrs_app/Forms/GoalForms/AssetManagement/amg3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = amg_three_form(request.POST)
        else:
            amg3form = amg3formdb.objects.get(pk=id)
            form = amg_three_form(request.POST, instance=amg3form)
        if form.is_valid():
            form.save()
            db = amg3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Associating assets in the asset inventory to services helps the organization to determine where critical dependencies exist, validate resilience requirements, and develop and implement resilience strategies in support of the critical service. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The confidentiality, integrity, and availability requirements of the service are used to derive the collective protection and sustainment requirements of associated assets.  Asset-level requirements should be based on the deployment in, contributions to, and the support of the critical service'
            
            db.save()

        return redirect('/amg3table')

def amg3formdelete(request, id):
    amg3form = amg3formdb.objects.get(pk=id)
    amg3form.delete()
    return redirect('/amg3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = amg_four_form()
        else:
            amg4form = amg4formdb.objects.get(pk=id)
            form = amg_four_form(instance=amg4form)
        return render(request, 'crrs_app/Forms/GoalForms/AssetManagement/amg4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = amg_four_form(request.POST)
        else:
            amg4form = amg4formdb.objects.get(pk=id)
            form = amg_four_form(request.POST, instance=amg4form)
        if form.is_valid():
            form.save()
            db = amg4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The organization should have a set of criteria to identify when changes to assets affect the delivery of the critical service and require a change to the asset description.  Change criteria should be applied consistently across all asset types. Examples of triggers that can affect high-value assets:  changes in services affecting the assets on which they rely (e.g., changes in availability requirements)  changes in technology infrastructure and configuration  creation or alteration of information  contracts that the organization enters into that would identify new assets  changes in organizational structure and staff—termination or transfer of staff between organizational units or changes in roles and responsibilities  real-estate transactions that add, alter, or change existing facilities  acquisition of assets such as technology or facilities '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' When changes to assets occur, asset descriptions should be updated to ensure that current protection and sustainment strategies continue to be satisfied. Typical work products:  asset change documentation  asset inventory status  updated asset and service resilience requirements  updated asset and service protection strategies and controls  updated strategies and continuity plans for sustaining assets and services '
            
            db.save()

        return redirect('/amg4table')

def amg4formdelete(request, id):
    amg4form = amg4formdb.objects.get(pk=id)
    amg4form.delete()
    return redirect('/amg4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = amg_five_form()
        else:
            amg5form = amg5formdb.objects.get(pk=id)
            form = amg_five_form(instance=amg5form)
        return render(request, 'crrs_app/Forms/GoalForms/AssetManagement/amg5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = amg_five_form(request.POST)
        else:
            amg5form = amg5formdb.objects.get(pk=id)
            form = amg_five_form(request.POST, instance=amg5form)
        if form.is_valid():
            form.save()
            db = amg5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Protection requirements describe how an assets exposure to sources of disruption and to the exploitation of vulnerabilities must be minimized.  Access requests should be granted in accordance with the protection requirements that have been established for the asset.  Access privileges are assigned and approved by asset owners based on the role of the person, object, or entity that is requesting access. Typical work products:  asset protection requirements  access requests  access approval  access control policy  access rights and responsibilities'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Asset owners are responsible for reviewing the access request and the asset’s protection requirements to decide whether to approve or deny access.  The access provided should be commensurate with and not exceed the requestor’s job responsibilities.  If the custodian of the asset is different from the owner, the owner should communicate in writing the approval for the request.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Periodic review (as defined by the organization) of access privileges is the primary responsibility of the asset owners.  Reviews should identify privileges that are:  excessive and in violation of the asset’s resilience requirement  out of alignment with the identity’s role or job responsibility  assigned but never approved by the asset owner '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Excessive or inappropriate levels of access privileges must be corrected in a timely manner  to avoid exposing the organization to additional risk.   As a result of periodic review, asset owners may authorize custodians to make modifications  such as:   change or disable certain privileges to preserve resilience requirements   disable an access account that is no longer valid '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' The identification of authorized users and the specification of access privileges reflect the requirements of the critical service.  Access control policies control access between users (or processes acting on behalf of users) and information systems.  Access permissions can also be employed at the application and service level to provide increased information security.  The principle of least privilege is employed to ensure users and processes operate at privilege levels no higher than necessary. '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' The identification of authorized users and the specification of access privileges reflect the requirements of the critical service.  Access control policies control access between users (or processes acting on behalf of users) and information systems.  Separation of duties addresses the potential for abuse of authorized privileges by dividing roles and privileges between users (e.g., ensuring security personnel administering access control functions do not also administer audit functions).'
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = 'An identity documents the existence of a person, object, or entity that requires access to organizational assets, such as information, technology, and facilities, to fulfill its role in executing services. An entity may be both internal and external to the organization. Requiring multiple forms of identification, such as documentary evidence or a combination of documents and biometrics, reduces the likelihood of individuals using fraudulent identification to establish an identity.'

            db.save()

        return redirect('/amg5table')

def amg5formdelete(request, id):
    amg5form = amg5formdb.objects.get(pk=id)
    amg5form.delete()
    return redirect('/amg5table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg6form(request, id=0):
    if request.method == "GET":
        if not id:
            form = amg_six_form()
        else:
            amg6form = amg6formdb.objects.get(pk=id)
            form = amg_six_form(instance=amg6form)
        return render(request, 'crrs_app/Forms/GoalForms/AssetManagement/amg6form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = amg_six_form(request.POST)
        else:
            amg6form = amg6formdb.objects.get(pk=id)
            form = amg_six_form(request.POST, instance=amg6form)
        if form.is_valid():
            form.save()
            db = amg6formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Categorizing information assets based on sensitivity and potential impact to the critical service allows an organization to properly label the information assets and provide an appropriate level of protection.  The sensitivity categorization scheme should cover all information assets that support the critical service.  Sensitivity categorization is a characteristic of an information asset that should be documented as part of the information asset inventory. Examples of information asset sensitivity categories:  public or non-sensitive  restricted or internal use only  confidential or proprietary (organizational intellectual property, product designs, customer information, employee records) '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization should monitor the categorization of information assets using techniques such as audits or spot-check inspections to ensure that the approved methods of information categorization are being followed.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The labeling and handling of information assets should be defined and communicated through policy.  Procedures should address how to label and handle the information assets to satisfy policy.'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The organization should train staff (including those who are external to the organization) on the approved methods of categorizing, labeling, and handling of information assets.  Training the staff supports the consistent application of the categorization scheme and the consistent handling of information assets across the organization. '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' High-value information assets should be backed-up and retained to meet the protection and sustainment requirements of the critical service.  The organization should consider the following when backing up information assets:  protection and sustainment requirements for the critical service  frequency of backup and storage  retention period  acceptable back-up and retention media  accessing information back-ups'
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' Properly disposing of information assets is necessary to ensure that there are no unauthorized disclosures.  Guidelines for the disposal of information assets should consider:  confidentiality requirements  sensitivity categorization  applicable rules, laws, and regulations '
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = ' The organization should provide oversight, such as audits or spot-check inspections to ensure that the approved methods of information disposal are being followed.'

            db.save()

        return redirect('/amg6table')

def amg6formdelete(request, id):
    amg6form = amg6formdb.objects.get(pk=id)
    amg6form.delete()
    return redirect('/amg6table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg7form(request, id=0):
    if request.method == "GET":
        if not id:
            form = amg_seven_form()
        else:
            amg7form = amg7formdb.objects.get(pk=id)
            form = amg_seven_form(instance=amg7form)
        return render(request, 'crrs_app/Forms/GoalForms/AssetManagement/amg7form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = amg_seven_form(request.POST)
        else:
            amg7form = amg7formdb.objects.get(pk=id)
            form = amg_seven_form(request.POST, instance=amg7form)
        if form.is_valid():
            form.save()
            db = amg7formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Prioritization should be used to identify the facilities that should be the focus of protection and sustainment activities. Example criteria for the establishment of high-priority facility assets can include:  the use of the facility asset in the general management and control of the organization (corporate headquarters, primary data centers, etc.)  facility assets that support more than one critical service  the value of the asset in directly supporting the organization’s delivery of the critical service'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Periodic review and validation of the prioritization of facilities is needed to account for operational and organizational environment changes.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The confidentiality, integrity, and availability requirements of the service are used to derive the collective protection and sustainment requirements of associated facility assets.  Protection requirements describe how an asset’s exposure to sources of disruption and to the exploitation of vulnerabilities must be minimized.  Sustainment requirements describe how assets must be kept operating when faced with disruptive events.  Protecting facility assets from vulnerabilities, threats, and risks requires the organization to develop appropriate protection and sustainment requirements'
            
            db.save()

        return redirect('/amg7table')

def amg7formdelete(request, id):
    amg7form = amg7formdb.objects.get(pk=id)
    amg7form.delete()
    return redirect('/amg7table')


#ConfigurationChangeManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])  
def ccmg1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ccmg_one_form()
        else:
            ccmg1form = ccmg1formdb.objects.get(pk=id)
            form = ccmg_one_form(instance=ccmg1form)
        return render(request, 'crrs_app/Forms/GoalForms/ConfigurationChangeManagement/ccmg1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ccmg_one_form(request.POST)
        else:
            ccmg1form = ccmg1formdb.objects.get(pk=id)
            form = ccmg_one_form(request.POST, instance=ccmg1form)
        if form.is_valid():
            form.save()
            db = ccmg1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Change management is a continuous process of controlling and approving changes to assets that support the service. This process addresses:  addition of new assets  changes to the asset, including ownership, custodianship, and location  elimination of assets Typical work products:  change requests  change implementation plan  backout plan  change and configuration management board meeting minutes  change approvals  change tracking and status  change documentation, including test results '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization should evaluate the impact of asset changes on existing resilience requirements.  The requirements from all the services supported by the changed asset should be considered. Evaluating resilience requirements is especially critical when assets are shared between services. Typical work products:  documented criteria that establishes when a change in requirements must be evaluated  requirements change history with rationale for performing the change  requirements baseline  resilience requirements included in change requests  updated asset resilience requirements '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Capacity planning determines the operational demand for a technology asset over a variable range of operational needs.  Capacity management and planning involves:  measurement of current demand  tests for anticipated demand  and gathering usage trends over time to be able to predict expansion needs. Typical work products include:  capacity management strategy  capacity forecasts  capacity statistics and performance metrics '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' This activity ensures that all change requests have a disposition.  And; changes that have not been closed are provided an updated status. Typical work products:  status reports  change request database  open items list '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' The organization should establish communication channels to ensure stakeholders are aware of changes to assets.  The organization should update service level agreements with stakeholders if necessary to reflect commitment to change notifications. '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' A well-defined System Development Life Cycle provides the foundation for the successful development, implementation, operation, and disposal of organizational information systems.  Information system security engineering principles (ensuring security is a design requirement, developers are trained accordingly, etc.) are incorporated and applied to the specification, design, development, implementation, and modification of information systems.  Maintaining the integrity of changes requires configuration control throughout the System Development Life Cycle.  Security testing/evaluation occurs at all post-design phases of the System Development Life Cycle. '

            db.save()

        return redirect('/ccmg1table')

def ccmg1formdelete(request, id):
    ccmg1form = ccmg1formdb.objects.get(pk=id)
    ccmg1form.delete()
    return redirect('/ccmg1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmg2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ccmg_two_form()
        else:
            ccmg2form = ccmg2formdb.objects.get(pk=id)
            form = ccmg_two_form(instance=ccmg2form)
        return render(request, 'crrs_app/Forms/GoalForms/ConfigurationChangeManagement/ccmg2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ccmg_two_form(request.POST)
        else:
            ccmg2form = ccmg2formdb.objects.get(pk=id)
            form = ccmg_two_form(request.POST, instance=ccmg2form)
        if form.is_valid():
            form.save()
            db = ccmg2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Configuration management is a process for managing the integrity of a technology asset over its lifetime.  The resilience of critical services and technology assets may be affected when the integrity of those assets is compromised. Configuration management:  supports the integrity of technology assets by ensuring that they can be restored to an acceptable form when necessary (perhaps after a disruption)  provides a level of control over changes that can potentially disrupt the asset’s support to the service Configuration management activities can include:  determining which assets to place under configuration management  identifying the configuration of selected assets  creating configuration baselines  controlling changes to configuration items  maintaining the integrity of baseline configurations  auditing configuration baselines '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Typical techniques include:  audits (configuration baselines, logs, etc.)  automated tools (security integrated event manager (SIEM), baseline configuration scanners, etc.)  procedural methods '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Proposed changes to assets are analyzed to determine the impact to the critical service including the resilience requirements.  Changes are also evaluated for their potential impact to multiple services.'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Integrity requirements address qualities to ensure the information is:  complete and intact  accurate and valid  authorized and official  Controlling which staff members are authorized to modify information assets helps ensure the continued integrity of those assets.  A fundamental way of controlling modifications to information assets is to limit access to those assets, both:  electronically (by controlling access to networks, servers, application systems, and databases and files)  physically (by limiting access to file rooms, work areas, computer rooms, and facilities) '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' The alteration of information assets through the processing cycle of the critical service must be controlled to ensure that the resulting information asset remains complete, accurate, and reliable.  Alteration of information assets can be due to:  unauthorized access or changes  operational risk such as loss of power (resulting in a corrupted file or database)  authorized changes resulting in unintended changes to the information asset Typical monitoring practices include:  establishing data validation controls such as selecting records for recalculation and review  performing regular reviews of information asset outputs from processes  periodically verifying that changes are valid and authorized (e.g., audits) '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' Periodically verify (through monitoring and auditing) that changes to configurations are valid and authorized.  Identify action items that are required to repair any unauthorized or unexplained modifications to technology assets.  Track action items to closure.'
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = ' To minimize operational impact, the organization should test in a segregated test environment to identify issues.  Once all issues have been identified and addressed, the organization can move the modified technology asset into production. Typical work products:  release management policy, guidelines, and standards  test builds  test procedure'
            if request.POST['response_eight'] == 'yes':
                db.feedback['response_eight'] = 'Excellent'
            elif request.POST['response_eight'] == 'no':
                db.feedback['response_eight'] = ' The process should address:  identifying and documenting staff who are authorized to modify technology assets  access requests and approvals  periodic auditing of technology assets to identify unauthorized access  Controlling access to technology assets by authorized staff ensures the continued integrity of these assets by limiting their unauthorized or inadvertent modification.  Access controls for technology assets may take electronic or physical forms. For example:  ensuring that technology assets are protected behind a physical barrier.  ensuring that technology assets are protected using role-based electronic access controls. '
            if request.POST['response_nine'] == 'yes':
                db.feedback['response_nine'] = 'Excellent'
            elif request.POST['response_nine'] == 'no':
                db.feedback['response_nine'] = ' Organizations should schedule, perform, document, and review records of maintenance and repairs on information system components.  All maintenance activities, whether performed on site or remotely, should be approved and monitored.  A process for authorizing maintenance personnel and for keeping a list of authorized personnel or maintenance organizations should be established. '
            if request.POST['response_ten'] == 'yes':
                db.feedback['response_ten'] = 'Excellent'
            elif request.POST['response_ten'] == 'no':
                db.feedback['response_ten'] = ' Organizations should approve, control, and monitor information system maintenance tools.'

            db.save()

        return redirect('/ccmg2table')

def ccmg2formdelete(request, id):
    ccmg2form = ccmg2formdb.objects.get(pk=id)
    ccmg2form.delete()
    return redirect('/ccmg2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmg3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ccmg_three_form()
        else:
            ccmg3form = ccmg3formdb.objects.get(pk=id)
            form = ccmg_three_form(instance=ccmg3form)
        return render(request, 'crrs_app/Forms/GoalForms/ConfigurationChangeManagement/ccmg3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ccmg_three_form(request.POST)
        else:
            ccmg3form = ccmg3formdb.objects.get(pk=id)
            form = ccmg_three_form(request.POST, instance=ccmg3form)
        if form.is_valid():
            form.save()
            db = ccmg3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Establishing a technology asset baseline (commonly called a configuration item) provides a foundation for managing the integrity of the asset as it changes over its lifecycle.  A configuration item may also extend to other technology work products such as test scripts, test plans, and asset documentation.  A configuration item may also be a grouping of related assets that are tied together in a logical baseline.  Configuration management establishes additional controls over the configuration baseline so that the asset integrity is maintained and always in a form that is available and authorized for use. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' An important component of configuration management is the ability to control and manage changes to the configuration baselines of technology assets.  Because of the nature of the operational environment, most technology assets are expected to change over time. For example:  the addition of new functionality  repair of software bugs and security vulnerabilities  the retirement or replacement of hardware components  Defining and communicating change procedures, including approval of proposed changes to baselines from relevant stakeholders, ensures that changes to technology assets will be handled in a controlled manner.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Baseline configurations include information about information system components, network topology, and the logical placement of those components within the system architecture.  Baseline configurations for information systems and assets are developed, documented, and maintained under configuration control. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Baseline configurations for information systems and assets are developed, documented, and maintained under configuration control.  Baseline configurations are formally reviewed.  Maintaining baseline configurations requires creating new baselines as organizational information systems change over time. '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' Information flow control regulates where information is allowed to travel within an information system and between information systems.  Dedicated connections between information systems should be authorized.  The interconnection interface characteristics, security requirements, and the nature of the communication should be documented as part of the baseline. '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' Dedicated connections should be periodically (frequency defined by the organization) reviewed and updated.  Baseline configurations for information systems and assets are developed, documented, and maintained under configuration control.  Baseline configurations are formally reviewed.  Maintaining baseline configurations requires creating new baselines as organizational information systems change over time. '
            
            db.save()

        return redirect('/ccmg3table')

def ccmg3formdelete(request, id):
    ccmg3form = ccmg3formdb.objects.get(pk=id)
    ccmg3form.delete()
    return redirect('/ccmg3table')


# controlsmanagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])  
def cmg1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmg_one_form()
        else:
            cmg1form = cmg1formdb.objects.get(pk=id)
            form = cmg_one_form(instance=cmg1form)
        return render(request, 'crrs_app/Forms/GoalForms/ControlsManagement/cmg1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmg_one_form(request.POST)
        else:
            cmg1form = cmg1formdb.objects.get(pk=id)
            form = cmg_one_form(request.POST, instance=cmg1form)
        if form.is_valid():
            form.save()
            db = cmg1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Control objectives are important because controls are designed to meet those objectives.  Control objectives provide a set of high-level requirements for the protection and sustainment of a critical service and associated assets.  Sources for identifying control objectives may be found in governance documents, policy documents, etc.:: People  Ensure all employees are trustworthy and reliable prior to hiring them.  All outside support personnel are identified. Information  Ensure the confidentiality and integrity of customer’s payment information.  Information assets are disposed of according to policy. Technology  Ensure the databases that support one or more critical services remain available.  Network integrity is protected. Facilities  Ensure environmental systems are maintained at an appropriate level to support datacenter equipment.  Physical access to assets is managed and protected.'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'service if the objective is not met.  Assigning a relative priority to each control objective also aids in determining the level of resources to apply when defining, analyzing, assessing, and addressing gaps in controls.  Prioritization can be based on: risk assessments, business impact analysis, etc. '
            
            db.save()

        return redirect('/cmg1table')

def cmg1formdelete(request, id):
    cmg1form = cmg1formdb.objects.get(pk=id)
    cmg1form.delete()
    return redirect('/cmg1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmg2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmg_two_form()
        else:
            cmg2form = cmg2formdb.objects.get(pk=id)
            form = cmg_two_form(instance=cmg2form)
        return render(request, 'crrs_app/Forms/GoalForms/ControlsManagement/cmg2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmg_two_form(request.POST)
        else:
            cmg2form = cmg2formdb.objects.get(pk=id)
            form = cmg_two_form(request.POST, instance=cmg2form)
        if form.is_valid():
            form.save()
            db = cmg2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'People  Ensure all employees are trustworthy and reliable prior to them being hired.  All outside support personnel are identified.  Background check  Visitor badges required for outside support personnel  Visitors are escorted Information  Ensure the confidentiality and integrity of customer’s payment information  Information assets are disposed of according to policy.  Encryption of customer payment data  Provide secure disposal bins  Monitor adherence to policy Technology  Ensure the databases, which support one or more critical services, remains available.  Network integrity is protected.  Fault tolerant architecture  Implement network monitoring Facilities  Ensure environmental systems are maintained at appropriate level to support datacenter equipment.  Physical access to assets is managed and protected.  Establish preventative maintenance schedule  Implement an access control system'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Methods to protect network integrity include implementation of:  firewalls  intrusion detection and prevention systems (IDS/IPS)  host-based intrusion detection  unidirectional gateways  vulnerability scanners  security information and event management (SIEM) systems  Segregation is a form of boundary protection. Segregation is the capability to isolate or segregate certain organizational information system assets.  Segregation reduces the attack surface of the information system and provides the capability to more effectively control information flows. Segregation can be implemented using VLANs, firewalls, DMZs, etc.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Data-at-rest is information located on storage devices that are components of information systems.  This control addresses the confidentiality and integrity of data-at-rest. System-related information that requires protection includes:  configurations or rule sets for  firewalls  gateways  intrusion detection/prevention systems  routers Mechanisms to achieve confidentiality and integrity protections include:  encryption  file share scanning  write-once-read-many (WORM) technologies  secure off-line storage  access controls'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The information system protects the confidentiality and/or integrity of data-in-transit.  This control applies to both internal and external networks and all types of information system components from which information can be transmitted. Mechanisms to achieve confidentiality and integrity protections include:  encryption  randomized communication patterns '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' Information/data leakage is the intentional or unintentional release of information to an untrusted environment. Methods to protect against data leaks include:  special cabling (emanation protection)  access control  encryption  data leakage prevention (DLP)'
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' To determine the set of auditable events, organizations should consider the auditing appropriate for each of the security controls to be implemented.  To ensure that the current set of auditable events is still appropriate, a periodic review should be performed.  Information system audit records should be periodically (as defined by the organization) reviewed for indications of inappropriate or unusual activity.  Audit information and audit tools should be protected from unauthorized access, modification, and deletion.  Organizations should retain audit records until it is determined that they are no longer needed for administrative, legal, audit, or other purposes. '
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = ' Organizations may restrict user access to removable media to defined personnel or roles.  Organizations may restrict the use of certain types of removable media.  Physically controlling information system media includes:  conducting inventories  ensuring procedures are in place to allow individuals to check out and return media to the media library  maintaining accountability for all stored media  The type of media storage should be appropriate for the security category and/or classification of the information residing on the media.  Media should be protected during transport outside of controlled areas using established safeguards. Safeguards can include:  locked containers  encryption '
            if request.POST['response_eight'] == 'yes':
                db.feedback['response_eight'] = 'Excellent'
            elif request.POST['response_eight'] == 'no':
                db.feedback['response_eight'] = ' Establish and document usage restrictions, configuration/connection requirements, and implementation guidance for:  each type of remote access allowed  wireless access  communication systems access (radios, phones, public address, etc.)  supervisory control and data acquisition (SCADA) and industrial control system (ICS)  The organization establishes alternate telecommunications services for the critical service to use when the primary telecommunications capabilities are unavailable.  Connections to communication or control systems are implemented through managed interfaces. Managed interfaces include:  gateways  routers  firewalls  encrypted tunnels '
            if request.POST['response_nine'] == 'yes':
                db.feedback['response_nine'] = 'Excellent'
            elif request.POST['response_nine'] == 'no':
                db.feedback['response_nine'] = 'Example cybersecurity human resource practices include:  assigning a risk designation to organizational positions  personnel screening and rescreening processes  personnel termination processes  personnel transfer process  implementing and managing access agreements (nondisclosure agreements, acceptable use agreements, access agreements, etc.)  third-party personnel security processes  personnel sanctions for noncompliance '
            if request.POST['response_ten'] == 'yes':
                db.feedback['response_ten'] = 'Excellent'
            elif request.POST['response_ten'] == 'no':
                db.feedback['response_ten'] = ' Information systems should be configured to provide only essential capabilities and prohibit or restrict the use of unnecessary functions, ports, protocols, services, etc.  Where feasible, organizations should limit component functionality to a single function per device/system (e.g., email server or web server but not both).  Other examples of least functionality include:  whitelisting  blacklisting  preventing program execution '

            db.save()

        return redirect('/cmg2table')

def cmg2formdelete(request, id):
    cmg2form = cmg2formdb.objects.get(pk=id)
    cmg2form.delete()
    return redirect('/cmg2olution')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmg3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmg_three_form()
        else:
            cmg3form = cmg3formdb.objects.get(pk=id)
            form = cmg_three_form(instance=cmg3form)
        return render(request, 'crrs_app/Forms/GoalForms/ControlsManagement/cmg3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmg_three_form(request.POST)
        else:
            cmg3form = cmg3formdb.objects.get(pk=id)
            form = cmg_three_form(request.POST, instance=cmg3form)
        if form.is_valid():
            form.save()
            db = cmg3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Controls analysis establishes a baseline from which the organization can begin to assess control effectiveness on a scheduled basis.  Controls analysis should identify gaps where a control objective is not adequately satisfied.  Analysis may include:  a design review of the control and its ability to meet the control objective.  development and execution of tests that demonstrate the control’s capability. Typical work products:  analysis results  control objectives that are satisfied by controls  a traceability matrix of control objectives and the controls that satisfy them  control gaps  proposed updates to existing controls  proposed new controls  risks related to unsatisfied control objectives  risks related to redundant and conflicting controls '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization uses the output of the controls gap analysis (CTRL:G3.Q1) to address all gaps that require resolution by:  modifying existing controls  Or; introducing new controls'
            
            db.save()

        return redirect('/cmg3table')

def cmg3formdelete(request, id):
    cmg3form = cmg3formdb.objects.get(pk=id)
    cmg3form.delete()
    return redirect('/cmg3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmg4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmg_four_form()
        else:
            cmg4form = cmg4formdb.objects.get(pk=id)
            form = cmg_four_form(instance=cmg4form)
        return render(request, 'crrs_app/Forms/GoalForms/ControlsManagement/cmg4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmg_four_form(request.POST)
        else:
            cmg4form = cmg4formdb.objects.get(pk=id)
            form = cmg_four_form(request.POST, instance=cmg4form)
        if form.is_valid():
            form.save()
            db = cmg4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The assessment verifies controls continue to protect and sustain the critical service and identifies any controls that do not.  The organization can use the analysis of control designs (established in G3.Q1) as the baseline of continuous assessment.  The organization sets the assessment schedule.  The organization should consider regulatory obligations and internal policy for performance and scheduling requirements. Typical work products:  assessment results  control objectives that are satisfied by controls  control gaps (control objectives not satisfied by controls)  proposed updates to existing controls  proposed new controls  remediation plans  updates to service continuity plans  risks related to unsatisfied control objectives  risks related to redundant and conflicting controls '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Problem areas require remediation to ensure that controls continue to satisfy control objectives. '
           
            db.save()

        return redirect('/cmg4table')

def cmg4formdelete(request, id):
    cmg4form = cmg4formdb.objects.get(pk=id)
    cmg4form.delete()
    return redirect('/cmg4table')


# ExternalDependenciesManagement
 
@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])  
def edmg1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmg_one_form()
        else:
            edmg1form = edmg1formdb.objects.get(pk=id)
            form = edmg_one_form(instance=edmg1form)
        return render(request, 'crrs_app/Forms/GoalForms/ExternalDependenciesManagement/edmg1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmg_one_form(request.POST)
        else:
            edmg1form = edmg1formdb.objects.get(pk=id)
            form = edmg_one_form(request.POST, instance=edmg1form)
        if form.is_valid():
            form.save()
            db = edmg1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' An external dependency exists when an external entity (contractor, customer, service provider, etc.)  has access to  control of  ownership in  possession of  responsibility for  or other defined obligations related to the critical service or its associated assets Examples of services provided to an organization from external entities can include:  outsourced activities that support operation or maintenance of the critical service  security operations, IT service delivery and operations management, or services that directly affect resilience processes  backup and recovery of data, provision of backup facilities for operations and processing, and provision of support technology, or similar resilience-specific services  infrastructure providers such as power and dark fiber  telecommunications (telephony and data)  public services such as fire and police support, emergency medical services, and emergency management services  technology and information assets, such as application software and databases Typical work products include:  list of external dependencies and entities '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization’s external dependencies will change over time as a result of changes to relationships with suppliers and customers, changes in services, the lifecycle of assets, etc.  Once the list of external dependencies is established, it is important that it be maintained.  A process for updating the list on a regular basis should be established. Typical work products include:  documented process for creating and maintaining the list of external dependencies '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Prioritization criteria may include dependencies that:  directly affect the operation and delivery of the critical service  support, maintain, or have custodial care of critical service assets  support the continuity of operations of the critical service  have access to highly sensitive or classified information  support more than one critical service  supply assets that support the operation of a critical service  impact the recovery time objective of the critical service Typical work products include:  criteria for prioritizing external dependencies  prioritized list of external dependencies '
            
            db.save()

        return redirect('/edmg1table')

def edmg1formdelete(request, id):
    edmg1form = edmg1formdb.objects.get(pk=id)
    edmg1form.delete()
    return redirect('/edmg1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmg_two_form()
        else:
            edmg2form = edmg2formdb.objects.get(pk=id)
            form = edmg_two_form(instance=edmg2form)
        return render(request, 'crrs_app/Forms/GoalForms/ExternalDependenciesManagement/edmg2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmg_two_form(request.POST)
        else:
            edmg2form = edmg2formdb.objects.get(pk=id)
            form = edmg_two_form(request.POST, instance=edmg2form)
        if form.is_valid():
            form.save()
            db = edmg2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Examples of risk include:  financial conditions  availability of external staff  reliance on subcontractors  risks to assets owned or operated by external entities  scalability of the external entity to meet capacity requirements  ability to support the continuity of operations of the critical service Typical work products include:  external dependency risk statements, with impact valuation  list of external dependency risks, with categorization and prioritization  vendor management process to identify and evaluate risk '           
            db.save()

        return redirect('/edmg2table')

def edmg2formdelete(request, id):
    edmg2form = edmg2formdb.objects.get(pk=id)
    edmg2form.delete()
    return redirect('/edmg2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmg_three_form()
        else:
            edmg3form = edmg3formdb.objects.get(pk=id)
            form = edmg_three_form(instance=edmg3form)
        return render(request, 'crrs_app/Forms/GoalForms/ExternalDependenciesManagement/edmg3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmg_three_form(request.POST)
        else:
            edmg3form = edmg3formdb.objects.get(pk=id)
            form = edmg_three_form(request.POST, instance=edmg3form)
        if form.is_valid():
            form.save()
            db = edmg3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' For each external dependency, the organization should establish a detailed set of resilience (protection and sustainment) requirements that the external entity must meet to support the critical service. When developing protection and sustainment requirements for external dependencies, the organization should:  consider the external entity’s impact on the operation of the critical service  consider the external entity’s impact on the sustainability and recovery of the critical service  consider regulatory obligations  consult internal and external stakeholders responsible for the associated assets and services  consider other critical services that rely upon the same external dependency  include enterprise-level requirements Typical work products include:  documented resilience requirements of the critical service:  Availability  Security  Integrity  RPO/RTO  Backup Requirements  '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = '  Typically this would be done periodically (as defined by the organization).  This can also be done as conditions warrant. Example conditions:  Change in external entity relationship  Change in the critical service operating environment that may affect the resilience requirements. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The selection process and criteria should be designed to ensure that the selected entity can fully meet the organization’s established requirements. Typical work products include:  requests for proposals or other types of solicitation documents that include resilience requirements  external entity selection criteria  evaluation of each external entity proposal against the selection criteria '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = 'Types of agreements may include:  contracts  service level agreements  memoranda of agreement  purchase orders  licensing agreements The agreement should:  be enforceable by the organization  include detailed and complete requirements that must be met by the external entity  include required performance standards and/or work products  be updated to reflect changes in requirements over the life of the relationship Example resilience requirements can include:  performance standards  security, confidentiality, and privacy requirements  disclosure obligations for security breaches  business resumption and contingency plans  staff performance or prescreening  controls  regulatory, legal, and compliance obligations Typical work products include:  agreements with external entities  service level agreements  requirements traceability matrix  resilience requirements specification '
            
            db.save()

        return redirect('/edmg3table')

def edmg3formdelete(request, id):
    edmg3form = edmg3formdb.objects.get(pk=id)
    edmg3form.delete()
    return redirect('/edmg3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmg_four_form()
        else:
            edmg4form = edmg4formdb.objects.get(pk=id)
            form = edmg_four_form(instance=edmg4form)
        return render(request, 'crrs_app/Forms/GoalForms/ExternalDependenciesManagement/edmg4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmg_four_form(request.POST)
        else:
            edmg4form = edmg4formdb.objects.get(pk=id)
            form = edmg_four_form(request.POST, instance=edmg4form)
        if form.is_valid():
            form.save()
            db = edmg4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Typically performance would be reviewed periodically (as defined by the organization).  Performance reviews can also be done as conditions warrant. Example conditions:  Sudden change in external entity performance  Change in the expected quality of work products.  Protection and sustainment requirements included in agreements should be used as the basis for monitoring the performance of the external entity.  This includes all services provided in support of the critical service for which the external entity is responsible.  Any deviations from established agreements must be analyzed to understand the potential impact on the organization. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Assigning responsibility ensures that monitoring is performed on a timely and consistent basis.  The organization should assign responsibility for monitoring each entity.  Responsibility is typically assigned to the owner of the relationship.  The responsible staff should establish procedures that determine the frequency, protocol, and responsibility for monitoring a particular external entity.  These procedures should be consistent with the terms of the agreement with the external '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'The intent of any corrective action is to minimize disruption to the critical service.  The range of corrective actions should be established in the agreement with the external entity. Typical work products include:  corrective action reports or documentation  correspondence with an external entity documenting corrective actions '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Typically performance would be reviewed periodically (as defined by the organization).  Performance reviews can also be done as conditions warrant. Example conditions:  Sudden change in external entity performance  Change in the expected quality of work products.'
           
            db.save()

        return redirect('/edmg4table')

def edmg4formdelete(request, id):
    edmg4form = edmg4formdb.objects.get(pk=id)
    edmg4form.delete()
    return redirect('/edmg4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmg_five_form()
        else:
            edmg5form = edmg5formdb.objects.get(pk=id)
            form = edmg_five_form(instance=edmg5form)
        return render(request, 'crrs_app/Forms/GoalForms/ExternalDependenciesManagement/edmg5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmg_five_form(request.POST)
        else:
            edmg5form = edmg5formdb.objects.get(pk=id)
            form = edmg_five_form(request.POST, instance=edmg5form)
        if form.is_valid():
            form.save()
            db = edmg5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Public services may be vital to a facility’s continued operation during a disruption.  Thorough consideration of these services must be given for service continuity planning.  Public services generally include services that are specific to the geographical region of the facility. Public services include:  fire response and rescue services  local and federal law enforcement (police, National Guard, FBI, etc.)  emergency management services, including paramedics and first responders  other services, such as hazardous material control Typical work products include:  results of business impact analysis (documenting public service dependencies for facilities)  list of public service providers on which facilities are dependent  key contact list  updated service continuity plans '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Critical services may be dependent on infrastructure providers to remain viable.  The organization must be prepared to address the loss of these providers, which can affect the resilience of the critical service.  The organization may need to consider the resilience of the providers when developing service continuity plans. These infrastructure services include:  telecommunications and telephone services  data and network service providers  electricity, natural gas, and other energy sources  water and sewer services  fuel providers for emergency power Typical work products include:  results of business impact analysis (documenting infrastructure dependencies for the critical service)  list of infrastructure providers on which the critical service depends  key contact list  updated service continuity plans '
            
            db.save()

        return redirect('/edmg5table')

def edmg5formdelete(request, id):
    edmg5form = edmg5formdb.objects.get(pk=id)
    edmg5form.delete()
    return redirect('/edmg5table')


# IncidentManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = img_one_form()
        else:
            img1form = img1formdb.objects.get(pk=id)
            form = img_one_form(instance=img1form)
        return render(request, 'crrs_app/Forms/GoalForms/IncidentManagement/img1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = img_one_form(request.POST)
        else:
            img1form = img1formdb.objects.get(pk=id)
            form = img_one_form(request.POST, instance=img1form)
        if form.is_valid():
            form.save()
            db = img1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The organization’s plan for managing incidents should address the identification, analysis, and response to an incident.  An event is one or more occurrences that affect organizational assets and have the potential to disrupt operations.  An incident significantly impacts the critical service and requires the organization to respond to prevent or limit impact to the critical service and the organization.  An incident may result from an event or a series of events that requires a response that is beyond standard operating procedures for managing events. The organization must plan for how it will:  identify events and incidents  analyze these events and incidents and determine an appropriate response  develop declaration criteria  respond to incidents  communicate incident information to stakeholders  staff the plan to meet plan objectives  structure the incident management staff (including roles and responsibilities)  train staff to identify, analyze, and respond to incidents '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The incident management plan should be periodically (as defined by the organization) reviewed and updated.  The knowledge gained through managing incidents can be used by the organization to improve the plan.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The organization should define the roles and responsibilities to achieve the plan’s objectives.  Job descriptions are a means to ensure that incident management staff understand their roles and are aware of their responsibilities.  Those roles and responsibilities should be included in the job description.'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The organization should establish a list of skilled staff and alternates to fill each role and responsibility defined in the incident management plan.  The organization should assign staff to each role and responsibility defined in the plan. Examples of incident management skills include:  event detection and reporting  analyzing events and incidents  collecting and preserving evidence '
            
            db.save()

        return redirect('/img1table')

def img1formdelete(request, id):
    img1form = img1formdb.objects.get(pk=id)
    img1form.delete()
    return redirect('/img1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = img_one_form()
        else:
            img2form = img2formdb.objects.get(pk=id)
            form = img_one_form(instance=img2form)
        return render(request, 'crrs_app/Forms/GoalForms/IncidentManagement/img2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = img_one_form(request.POST)
        else:
            img2form = img2formdb.objects.get(pk=id)
            form = img_one_form(request.POST, instance=img2form)
        if form.is_valid():
            form.save()
            db = img2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The organization’s plan for managing incidents should address the identification, analysis, and response to an incident.  An event is one or more occurrences that affect organizational assets and have the potential to disrupt operations.  An incident significantly impacts the critical service and requires the organization to respond to prevent or limit impact to the critical service and the organization.  An incident may result from an event or a series of events that requires a response that is beyond standard operating procedures for managing events. The organization must plan for how it will:  identify events and incidents  analyze these events and incidents and determine an appropriate response  develop declaration criteria  respond to incidents  communicate incident information to stakeholders  staff the plan to meet plan objectives  structure the incident management staff (including roles and responsibilities)  train staff to identify, analyze, and respond to incidents '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Logging and tracking event data in an incident knowledgebase or similar mechanism:  facilitates event triage and analysis activities  provides the ability to obtain a status and disposition of the event An incident knowledgebase should contain basic event (and incident) information such as:  a unique identifier  a brief description of the event  an event category (e.g., denial of service, virus intrusion, physical access violation)  the assets, services, and organizational units that are affected by the event  a brief description of how the event was identified and reported, by whom, and other relevant details (e.g., application system, network segment, operating system) '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Event categories can help the organization understand and communicate the severity and impact the event will have on the critical service.  Events may be categorized by:  type (e.g., security, safety, unauthorized access, user issue, denial of service, virus intrusion, physical access violation)  severity (e.g., critical, high, medium, low)  other categorization labels (e.g., internal, external, physical, technical) '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Analysis should be conducted to determine whether the event correlates to other events (correlation may indicate larger issues, problems, or incidents). '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' Prioritization determines what order events should be addressed.  Events may be prioritized based on:  the results of categorization (severity, type, etc.) and analysis  experience with past events  potential impact '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' The status of events should be checked regularly to ensure that they are moving through the organization’s established incident management process. Possible status types for event reports include:  closed  referred for further analysis  referred to an organizational unit or line of business for disposition  declared as an incident '
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = ' Periodically (as defined by the organization) review the incident knowledgebase for events that have not been closed or for which there is no disposition.  Events that have not been closed or that do not have a disposition should be reprioritized, analyzed, and tracked to resolution.'
            if request.POST['response_eight'] == 'yes':
                db.feedback['response_eight'] = 'Excellent'
            elif request.POST['response_eight'] == 'no':
                db.feedback['response_eight'] = ' An event may become an organizational incident that has the potential to be a violation of local, state, or federal rules, laws, and regulations. For example:  Securities and Exchange Commission regulatory requirements  state privacy laws  Food and Drug Administration regulatory requirements  chain of custody requirements  This is often not known early in the investigation of an event, so the organization should ensure that all event evidence is handled properly.'
            if request.POST['response_nine'] == 'yes':
                db.feedback['response_nine'] = 'Excellent'
            elif request.POST['response_nine'] == 'no':
                db.feedback['response_nine'] = ' Based on applicable requirements (identified in IM:G2.Q8), the organization should develop a process using standards and guidelines for the collection, documentation, and preservation of event evidence.  Staff should be trained on the organizational process for proper identification and handling of evidence to ensure that the evidence is not altered and the integrity is maintained. '

            db.save()

        return redirect('/img2table')

def img2formdelete(request, id):
    img2form = img2formdb.objects.get(pk=id)
    img2form.delete()
    return redirect('/img2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = img_one_form()
        else:
            img3form = img3formdb.objects.get(pk=id)
            form = img_one_form(instance=img3form)
        return render(request, 'crrs_app/Forms/GoalForms/IncidentManagement/img3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = img_one_form(request.POST)
        else:
            img3form = img3formdb.objects.get(pk=id)
            form = img_one_form(request.POST, instance=img3form)
        if form.is_valid():
            form.save()
            db = img3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Incident declaration defines the point at which the organization has established that an incident has occurred, is occurring, or is imminent.  Incident declaration may occur based on a specific event or when multiple events are occurring. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Declaration criteria guides the organization in determining when to declare an incident (particularly if incident declaration is not immediately apparent). Example incident declaration criteria:  Is the event isolated?  Predefined thresholds of impact.  Did past occurrences of the event result in an incident declaration?  Is the impact of the event imminent or immediate?  Is the organization already suffering some effects from the event?  Is the life or safety of people at risk?  Is the integrity and operability of a facility at risk?  Is the integrity and operability of a high-value service or system at risk?  Does the event constitute fraud or theft? '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Incident analysis should focus on properly defining the underlying problem, condition, or issue.  Incident analysis should help the organization prepare the most appropriate and timely response to the incident.  Incident analysis should determine whether the incident has legal ramifications. Example incident analysis activities:  interviews with those who reported the underlying event(s) and were affected  interviews of specific knowledge experts  review of relevant logs and audit trails of network and physical activity  consultation of vulnerability and incident databases (US-CERT Vulnerability Notes Database / MITRE’s Common Vulnerabilities and Exposures List)  consultation with law enforcement, legal, audit, product vendors, and emergency management '
            
            db.save()

        return redirect('/img3table')

def img3formdelete(request, id):
    img3form = img3formdb.objects.get(pk=id)
    img3form.delete()
    return redirect('/img3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = img_one_form()
        else:
            img4form = img4formdb.objects.get(pk=id)
            form = img_one_form(instance=img4form)
        return render(request, 'crrs_app/Forms/GoalForms/IncidentManagement/img4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = img_one_form(request.POST)
        else:
            img4form = img4formdb.objects.get(pk=id)
            form = img_one_form(request.POST, instance=img4form)
        if form.is_valid():
            form.save()
            db = img4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Incidents that the organization has declared should be escalated to stakeholders who can implement, manage, and resolve the incident.  Stakeholders can be internal to the organization (such as a standing incident response team or an incident-specific team) or external, in the form of contractors or other suppliers. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization’s response to an incident should be founded on pre-defined incident response procedures.  Pre-defined procedures describe the actions the organization takes to prevent or contain the impact of an incident.  Incident response may be as simple as notifying users to avoid opening a specific type of email message or as complicated as having to implement service continuity plans. The actions related to incident response can include:  containing damage (i.e., taking hardware or systems offline or by locking-down a facility)  collecting evidence (including logs and audit trails)  interviewing relevant staff  communicating to stakeholders'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Incident status and response should be communicated in a controlled and regular manner to internal and external stakeholders.  Incident status and response should be managed throughout the incident lifecycle. The incident communication process should include:  the stakeholders with whom communication about incidents are required  the level of communication appropriate to various stakeholders  special controls over communication (i.e., encryption or secured communications) that are appropriate for some stakeholders Examples of stakeholders that may need to be included in incident communication:  internal staff who have incident handling and management responsibilities  asset owners and service owners  information technology staff  business continuity staff  affected customers or suppliers '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The organization should have a process for the formal closure of incidents that results in formally logging a status of closed in the incident knowledgebase.  The status of incidents in the incident knowledgebase should be reviewed regularly to determine if open incidents should be closed or need additional action. Typical work products:  criteria for incident closure  updated incident knowledgebase '
            
            db.save()

        return redirect('/img4table')

def img4formdelete(request, id):
    img4form = img4formdb.objects.get(pk=id)
    img4form.delete()
    return redirect('/img4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = img_one_form()
        else:
            img5form = img5formdb.objects.get(pk=id)
            form = img_one_form(instance=img5form)
        return render(request, 'crrs_app/Forms/GoalForms/IncidentManagement/img5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = img_one_form(request.POST)
        else:
            img5form = img5formdb.objects.get(pk=id)
            form = img_one_form(request.POST, instance=img5form)
        if form.is_valid():
            form.save()
            db = img5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The organization should employ commonly available techniques to perform root cause analysis as a means of potentially preventing future incidents of a similar type and impact. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Problem management is the process that an organization uses to identify recurring problems, examine root causes, and develop tables for these problems to prevent future, similar incidents.  Formal linkages to other processes (risk management, change and configuration management, vulnerability management, etc.) that may impact an incident should be established.  Formal linkages strengthen the organization’s overall ability to prevent incidents.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Lessons learned in incident management should help determine the validity and effectiveness of the organization’s current strategies for protecting and sustaining assets.  Lessons learned should also provide valuable information for continuous improvement of the incident management process. Examples of improvements to asset protection and service continuity strategies may include:  updated asset protection requirements  updated controls to protect assets and services from future incidents of a similar type and nature  updated policies to reflect lessons learned  updated training for employees regarding the incident '
            
            db.save()

        return redirect('/img5table')

def img5formdelete(request, id):
    img5form = img5formdb.objects.get(pk=id)
    img5form.delete()
    return redirect('/img5table')


# RiskManagement 

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])  
def rmg1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmg_one_form()
        else:
            rmg1form = rmg1formdb.objects.get(pk=id)
            form = rmg_one_form(instance=rmg1form)
        return render(request, 'crrs_app/Forms/GoalForms/RiskManagement/rmg1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmg_one_form(request.POST)
        else:
            rmg1form = rmg1formdb.objects.get(pk=id)
            form = rmg_one_form(request.POST, instance=rmg1form)
        if form.is_valid():
            form.save()
            db = rmg1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Operational risk is defined as the potential impact on assets and the related services—the risk that results from operating services and assets on a day-to-day basis.  Operational risk sources are the fundamental areas of risk that can affect the critical service and associated assets.  Identifying risk sources or areas of risk helps the organization determine and categorize the types of operational risk that are most likely to affect day-to-day operations. Risk sources typically include:  poorly designed and executed business processes and services  inadvertent actions of people, such as accidental disclosures or modifications of information  intentional actions of people, such as insider threat and fraud  failure of systems to perform as intended '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Risk categories provide a means for collecting and organizing risk for ease of analysis and mitigation.  Operational risk categories typically align with the sources of operational risk.  Risk categories can be as granular as necessary for the organization to effectively manage risk. Examples of operational risk categories:  failed processes  employee screening  vendor management  actions of people  malicious attack  inadvertent disclosure  systems and technology  unsupported software  hardware failure  external events  natural disaster  supply chain interruption '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The plan provides a common foundation for the performance of operational risk management activities.  The operational risk management plan should be developed to facilitate the accumulation of operational risks as input to the organization’s enterprise risk management program. Typical items addressed in an operational risk management plan include:  the scope of operational risk management activities  the methods to be used for operational risk identification, analysis, mitigation, monitoring, etc.  identification of sources of operational risk  risk mitigation techniques to be used  identification and definition of risk metrics  frequency of risk monitoring and reassessment '
            
            db.save()

        return redirect('/rmg1table')

def rmg1formdelete(request, id):
    rmg1form = rmg1formdb.objects.get(pk=id)
    rmg1form.delete()
    return redirect('/rmg1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmg_two_form()
        else:
            rmg2form = rmg2formdb.objects.get(pk=id)
            form = rmg_two_form(instance=rmg2form)
        return render(request, 'crrs_app/Forms/GoalForms/RiskManagement/rmg2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmg_two_form(request.POST)
        else:
            rmg2form = rmg2formdb.objects.get(pk=id)
            form = rmg_two_form(request.POST, instance=rmg2form)
        if form.is_valid():
            form.save()
            db = rmg2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Organizational impact areas identify the categories where realized risk may have meaningful and disruptive consequences.  Impact areas reflect what is important to the organization and to the accomplishment of its mission.  Organizational impact areas help identify how realized risk may affect the organization. Examples of organizational impact areas:  reputation and customer confidence  revenue  staff productivity  safety and health of staff and customers  fines and legal penalties  compliance with regulations '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Risk parameters may differ for each impact area.  Risk parameters provide the organization a means for consistent measurement of risk across the organization.  Risk tolerance parameters describe the risk measurement criteria for each impact area.  Risk measurement criteria include how impact is measured, how frequently it is measured, and what is to be measured.  Risk tolerance parameters can be qualitative (high, medium, low) or quantitative (based on levels of loss, fines, number of customers lost, etc.). '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Risk tolerance parameters describe the risk measurement criteria for each impact area.  Risk tolerance thresholds are used by management to determine when a risk is in control or when it has exceeded acceptable limits.  Risk tolerance thresholds should be set for each category of risk that the organization establishes as a means for measuring and managing risk. For example:  A risk tolerance threshold for a category of risk may be whenever more than 200 users are impacted.  The risk tolerance threshold indicates when action needs to be taken to prevent operational disruption. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Risk tolerance parameters describe the risk measurement criteria for each impact area.  Risk tolerance thresholds are used by management to determine when a risk is in control or when it has exceeded acceptable limits.  Risk tolerance thresholds should be set for each category of risk that the organization establishes as a means for measuring and managing risk. For example:  A risk tolerance threshold for a category of risk may be whenever more than 200 users are impacted.  The risk tolerance threshold indicates when action needs to be taken to prevent operational disruption. '

            db.save()

        return redirect('/rmg2table')

def rmg2formdelete(request, id):
    rmg2form = rmg2formdb.objects.get(pk=id)
    rmg2form.delete()
    return redirect('/rmg2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmg_three_form()
        else:
            rmg3form = rmg3formdb.objects.get(pk=id)
            form = rmg_three_form(instance=rmg3form)
        return render(request, 'crrs_app/Forms/GoalForms/RiskManagement/rmg3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmg_three_form(request.POST)
        else:
            rmg3form = rmg3formdb.objects.get(pk=id)
            form = rmg_three_form(request.POST, instance=rmg3form)
        if form.is_valid():
            form.save()
            db = rmg3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' From the sources and categories of risk established in G1.Q1 and G1.Q2, specific risks that affect the delivery of the critical service should be identified.  The organization should determine the effect on the service that could result from the realization of risk at the asset level. Typical Work Products:  List of operational risks by service '
            
            db.save()

        return redirect('/rmg3table')

def rmg3formdelete(request, id):
    rmg3form = rmg3formdb.objects.get(pk=id)
    rmg3form.delete()
    return redirect('/rmg3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmg_four_form()
        else:
            rmg4form = rmg4formdb.objects.get(pk=id)
            form = rmg_four_form(instance=rmg4form)
        return render(request, 'crrs_app/Forms/GoalForms/RiskManagement/rmg4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmg_four_form(request.POST)
        else:
            rmg4form = rmg4formdb.objects.get(pk=id)
            form = rmg_four_form(request.POST, instance=rmg4form)
        if form.is_valid():
            form.save()
            db = rmg4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Each risk (identified in RM:G3.Q1) should be evaluated and assigned values in accordance with the defined risk parameters to determine impact to the critical service.  The organization should determine if the impact of the risk would exceed the risk tolerance thresholds. Typical Work Products:  Business Impact Analysis  Updated operational risk statements to include the impact valuation. Risk statements may include:  asset affected  weakness or vulnerability  means of exploitation  likelihood (if known)  undesired outcomes or impacts  consequence to the organization '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A disposition is a statement of how the organization intends to address the risk.  A risk disposition should be assigned to each operational risk. Risk dispositions typically include:  Avoid – altering operations to avoid the risk while still providing the service  Accept – acknowledging the risk without taking action  Monitor – deferring action until there is a need to address the risk  Transfer – assigning the risk to a willing and able entity  Mitigate or control – taking active steps to minimize the risk '
            
            db.save()

        return redirect('/rmg4table')

def rmg4formdelete(request, id):
    rmg4form = rmg4formdb.objects.get(pk=id)
    rmg4form.delete()
    return redirect('/rmg4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmg_five_form()
        else:
            rmg5form = rmg5formdb.objects.get(pk=id)
            form = rmg_five_form(instance=rmg5form)
        return render(request, 'crrs_app/Forms/GoalForms/RiskManagement/rmg5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmg_five_form(request.POST)
        else:
            rmg5form = rmg5formdb.objects.get(pk=id)
            form = rmg_five_form(request.POST, instance=rmg5form)
        if form.is_valid():
            form.save()
            db = rmg5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Risk mitigation plans should be developed when operational risk exceeds the organization’s risk threshold and are determined to be unacceptable. Risk mitigation plans may include actions to:  reduce the likelihood (probability) of the vulnerability or threat and resulting risk  minimize exposure to the vulnerability or threat from which the risk arises  develop service continuity plans that would keep an asset or service in production if affected by realized risk  develop recovery and restoration plans to address the consequences of realized risk'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The disposition of risks must be tracked, periodically assessed, and revised as necessary.  The organization should provide a method for tracking open risks to closure. '
            
            db.save()

        return redirect('/rmg5table')

def rmg5formdelete(request, id):
    rmg5form = rmg5formdb.objects.get(pk=id)
    rmg5form.delete()
    return redirect('/rmg5table')


# ServiceContinuityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmg_one_form()
        else:
            scmg1form = scmg1formdb.objects.get(pk=id)
            form = scmg_one_form(instance=scmg1form)
        return render(request, 'crrs_app/Forms/GoalForms/ServiceContinuityManagement/scmg1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmg_one_form(request.POST)
        else:
            scmg1form = scmg1formdb.objects.get(pk=id)
            form = scmg_one_form(request.POST, instance=scmg1form)
        if form.is_valid():
            form.save()
            db = scmg1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A service continuity plan is a proactive plan of action an organization will take if a service disruption occurs.  Plans should be developed at the time of service development and implementation.  Plans should also be adjusted on an ongoing basis as new risks are encountered and the operational environment changes.  Service continuity plans may require one or more sub plans such as a recovery or restoration plan. Typical work products include:  service continuity plan templates  service continuity plans (including a list of relevant stakeholders)'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Standards and guidelines ensure enterprise-wide consistency of service continuity plans.  Standards, guidelines, and templates can be derived by the organization from both internal and external sources. Standards, guidelines, and templates may cover topics such as:  alternative resources and locations that would support the organization’s high-value services  alternative activities that would have to be performed (technical or manual)  identification of:  vital staff roles and responsibilities  high-value technology, information, and facility assets necessary to support the plan  relevant stakeholders of the plan and method of communicating with them  documentation of:  the recovery and restoration sequence for the critical service  security and access-related issues that are required to execute the plan  any special handling that is required of information or technology  the service continuity test plan '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The activities documented in the service continuity plan must be assigned to responsible and skilled individuals in the event that the plan must be executed.  These staff members may be internal or external (through outsourcing arrangements and service contracts) to the organization. Typical work products include:  service continuity plan staff requirements  list of potential staff members  staff and task assignments (internal and external)  staff commitments to service continuity plans '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The critical service may depend on assets both internal and external to the organization.  Services may also rely on external partnerships such as public agencies and infrastructure providers (public utilities, telecommunications, etc.).  Key contacts can therefore be internal or external to the organization. Typical work products include:  list of public service providers on which the critical service is dependent  list of external entities, including business partners and vendors, that facilitate critical service delivery  list of key contacts (both internal and external) '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' The ability to execute service continuity plans during a disruption depends on their accessibility and integrity.  The organization must take steps to ensure that the plans are:  archived in a controlled manner  up to date and available  secured and free from unapproved modification  readily retrievable, when necessary, by those who need access to them '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' Availability requirements must be met by an asset not only in day-to-day operations but also under diminished conditions brought on by a disruption or event.  Recovery time objectives establish the period of acceptable downtime or the maximum time allowed for the recovery of a critical service following a disruption.  Recovery point objectives establish the maximum amount of data that may be lost when service is restored after a disruption. The recovery point objective is typically expressed as a length of time. (e.g., a maximum of 4 hours’ worth of data).'
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = 'The organization must plan to sustain technology assets to ensure the continued operation of services. Mechanisms implemented to achieve this practice can take many forms:  load balancing: a method that improves the distribution of workloads across multiple resources to optimize resource use, maximize throughput, minimize response time, and avoid overload of any single resource  hot swap capabilities: the ability to replace or add components without stopping or shutting down the associated system  high availability implementations: a failover methodology to ensure availability during device or component interruptions  alternate telecommunications'
           
            db.save()

        return redirect('/scmg1table')

def scmg1formdelete(request, id):
    scmg1form = scmg1formdb.objects.get(pk=id)
    scmg1form.delete()
    return redirect('/scmg1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmg_two_form()
        else:
            scmg2form = scmg2formdb.objects.get(pk=id)
            form = scmg_two_form(instance=scmg2form)
        return render(request, 'crrs_app/Forms/GoalForms/ServiceContinuityManagement/scmg2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmg_two_form(request.POST)
        else:
            scmg2form = scmg2formdb.objects.get(pk=id)
            form = scmg_two_form(request.POST, instance=scmg2form)
        if form.is_valid():
            form.save()
            db = scmg2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Test standards help ensure service continuity plans are viable.  Testing should be conducted in a controlled environment.  Testing is often the only opportunity for an organization to know whether the plans meet their stated objectives.  The testing program and standards should be enforced to ensure consistency and the ability to interpret results at the organizational level. Standards for service continuity testing can include:  types of tests (i.e., walkthroughs, tabletops, dependency testing, etc.)  required test components  testing frequency  quality assurance standards  involvement and commitment of plan stakeholders  reporting standards '
         
            db.save()

        return redirect('/scmg2table')

def scmg2formdelete(request, id):
    scmg2form = scmg2formdb.objects.get(pk=id)
    scmg2form.delete()
    return redirect('/scmg2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmg_three_form()
        else:
            scmg3form = scmg3formdb.objects.get(pk=id)
            form = scmg_three_form(instance=scmg3form)
        return render(request, 'crrs_app/Forms/GoalForms/ServiceContinuityManagement/scmg3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmg_three_form(request.POST)
        else:
            scmg3form = scmg3formdb.objects.get(pk=id)
            form = scmg_three_form(request.POST, instance=scmg3form)
        if form.is_valid():
            form.save()
            db = scmg3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Test standards help ensure service continuity plans are viable.  Testing should be conducted in a controlled environment.  Testing is often the only opportunity for an organization to know whether the plans meet their stated objectives.  The testing program and standards should be enforced to ensure consistency and the ability to interpret results at the organizational level. Standards for service continuity testing can include:  types of tests (i.e., walkthroughs, tabletops, dependency testing, etc.)  required test components  testing frequency  quality assurance standards  involvement and commitment of plan stakeholders  reporting standards  measurement standards  test plan maintenance '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The service continuity test schedule should meet the requirements of the service. Typical work products include:  plan test schedule '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The tests should establish the viability, accuracy, and completeness of the plan.  The tests should also provide information about the organization’s level of preparedness.  The tests are performed under conditions established by the organization, and the results of the test should be recorded and documented. Typical work products include:  documented test results '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Backup and storage of information assets should meet the requirements of the service.  Testing of backup and storage procedures is done to ensure those requirements are being met.  Periodic testing of the organization’s backup and storage procedures ensures continued validity as operational conditions change. Information asset backup and storage procedures typically include:  frequency standards  retention periods  authorized storage locations and methods  encryption and protection requirements  testing standards  periodic review and revision of backup and storage procedures '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' The objective of service continuity plan testing is to ensure that plans work as intended.  Testing identifies required improvements to the service continuity plans as well as the associated test plans.  The evaluation of test results involves comparing the documented test results against the established test objectives.  Areas where objectives could not be met are recorded, and strategies are developed to review and revise the plans.  Improvements to the testing process and plans should also be identified, documented, and incorporated into future tests. Improvement areas may include:  lack of sufficient resources  lack of appropriate resources  training gaps for plan staff and stakeholders  plan conflicts (if multiple plans are tested simultaneously)  required changes to infrastructure Typical work products include:  documented test results  list of improvements to service continuity plans  list of improvements to service continuity test plans '
            
            db.save()

        return redirect('/scmg3table')

def scmg3formdelete(request, id):
    scmg3form = scmg3formdb.objects.get(pk=id)
    scmg3form.delete()
    return redirect('/scmg3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmg_four_form()
        else:
            scmg4form = scmg4formdb.objects.get(pk=id)
            form = scmg_four_form(instance=scmg4form)
        return render(request, 'crrs_app/Forms/GoalForms/ServiceContinuityManagement/scmg4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmg_four_form(request.POST)
        else:
            scmg4form = scmg4formdb.objects.get(pk=id)
            form = scmg_four_form(request.POST, instance=scmg4form)
        if form.is_valid():
            form.save()
            db = scmg4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The organization must be able to determine when the plan must be executed and who is responsible for initiating action.  The organization should ensure that owners of service continuity plans understand the conditions for execution.  Plans may be executed for a variety of reasons, including:  in response to a perceived or known threat  as a result of an incident  in response to a crisis  cut-over from one application system to another  moving office locations  moving data centers Typical work products include:  organizational conditions for executing service continuity plans '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The review of executed service continuity plans identifies plan shortcomings and needed improvements.  Unforeseen circumstances that arise during the execution are documented and addressed. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' As a result of the review of executed service continuity plans (SCM:G4.Q2), improvements are identified and documented. Typical work products include:  list of improvements to service continuity plans  list of improvements to service continuity test plans '
            
            db.save()

        return redirect('/scmg4table')

def scmg4formdelete(request, id):
    scmg4form = scmg4formdb.objects.get(pk=id)
    scmg4form.delete()
    return redirect('/scmg4table')


# situationalawareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def sag1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = sag_one_form()
        else:
            sag1form = sag1formdb.objects.get(pk=id)
            form = sag_one_form(instance=sag1form)
        return render(request, 'crrs_app/Forms/GoalForms/SituationalAwareness/sag1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = sag_one_form(request.POST)
        else:
            sag1form = sag1formdb.objects.get(pk=id)
            form = sag_one_form(request.POST, instance=sag1form)
        if form.is_valid():
            form.save()
            db = sag1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Threat monitoring is a process of data collection and distribution with the purpose of providing timely, accurate, complete, and relevant information about the organization’s current threat environment.  Threat monitoring is an integral part of establishing a common operating picture for the organization. Responsible staff typically include:  CISO office  physical security  technology administrators (i.e., network, server, database, etc.)  asset owners Example Sources:  vendors’ notifications  industry groups (Internet Storm Center, Nextgov Threatwatch)  international sources (multinational vendors, CERT-EU )  weather alerts (NOAA)  law enforcement (FBI InfraGard, IC3)  DHS (ICS-CERT, US-CERT, sector-specific ISACs) '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Effective monitoring requires people, procedures, and technology that need to be deployed and managed to meet monitoring requirements.  Procedures ensure the timeliness, consistency, and accuracy of threat information and the distribution of this information to relevant stakeholders. Procedures may address:  source identification  monitoring frequency  threat identification  threat validation and analysis  threat communication '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The threat monitoring program must take into consideration the scope and breadth of the activities necessary to meet its goals, including the human resources necessary to fulfill requirements.  Staff assigned to the monitoring process must have appropriate knowledge of threat monitoring procedures.  Training or skills improvement activities must be conducted to meet threat monitoring requirements. Examples of Training:  operating, monitoring and configuring monitoring system components  securing data collected from monitoring system components  understanding and interpreting monitoring data  communicating threat monitoring information to stakeholders '
            
            db.save()

        return redirect('/sag1table')

def sag1formdelete(request, id):
    sag1form = sag1formdb.objects.get(pk=id)
    sag1form.delete()
    return redirect('/sag1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def sag2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = sag_two_form()
        else:
            sag2form = sag2formdb.objects.get(pk=id)
            form = sag_two_form(instance=sag2form)
        return render(request, 'crrs_app/Forms/GoalForms/SituationalAwareness/sag2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = sag_two_form(request.POST)
        else:
            sag2form = sag2formdb.objects.get(pk=id)
            form = sag_two_form(request.POST, instance=sag2form)
        if form.is_valid():
            form.save()
            db = sag2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Internal stakeholders are identified to:  ensure communications about ongoing threat monitoring activities  promote threat awareness  ensure that the organization is performing under a common operating picture. Examples of internal stakeholders include:  members of the incident handling and management team  asset owners and service owners  information technology staff  senior management  business continuity staff  human resources departments  communications and public relations staff  support functions such as legal and audit Typical work products:  list of internal stakeholders and alternates  stakeholder contact information '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' External stakeholders are identified to  ensure communications about ongoing threat monitoring activities  promote threat awareness  ensure that the organization and its external stakeholders are performing under a common operating picture  External stakeholders may have a stated role in communication plans or the service continuity plans of the organization. Examples of external stakeholders include:  first responders including law enforcement, fire, and medical  media including newspaper, television, radio, and internet  customers, business partners, and upstream suppliers  local, state, and federal emergency management  local utilities such as power, gas, telecommunications, and water  legal, regulatory, and governing agencies Typical work products:  list of external stakeholders and alternates  stakeholder contact information '
            
            db.save()

        return redirect('/sag2table')

def sag2formdelete(request, id):
    sag2form = sag2formdb.objects.get(pk=id)
    sag2form.delete()
    return redirect('/sag2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def sag3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = sag_three_form()
        else:
            sag3form = sag3formdb.objects.get(pk=id)
            form = sag_three_form(instance=sag3form)
        return render(request, 'crrs_app/Forms/GoalForms/SituationalAwareness/sag3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = sag_three_form(request.POST)
        else:
            sag3form = sag3formdb.objects.get(pk=id)
            form = sag_three_form(request.POST, instance=sag3form)
        if form.is_valid():
            form.save()
            db = sag3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Threat information must be communicated according to established requirements.  Communication requirements may dictate that various communications methods and channels should be considered and identified.  The infrastructure to support those methods may need to be developed and implemented. Example methods of communicating threat information include:  threat communication standards and guidelines  standardized report templates  communication escalation protocols  communication channels (email, text, mobile phone, etc.) Typical work products:  list of stakeholders and contact information  stakeholder communication requirements  documented methods and channels (by stakeholder class or requirement)  tools and techniques for communication '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Effective threat communications requires the assignment of authority and accountability for threat communication activities.  Resources must be available to meet threat communication requirements.  The authority and accountability should be detailed in job descriptions. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Training must be provided to staff that support and enable communications procedures.  A skills inventory and gap analysis may be used to identify training requirements. Typical work products:  threat communication procedures with resources assigned  job descriptions that contain threat communication responsibilities  list of available and skilled resources  list of skill and resource gaps  training plan to address skill gaps '
            
            db.save()

        return redirect('/sag3table')

def sag3formdelete(request, id):
    sag3form = sag3formdb.objects.get(pk=id)
    sag3form.delete()
    return redirect('/sag3table')


# TrainingAwareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tag1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = tag_one_form()
        else:
            tag1form = tag1formdb.objects.get(pk=id)
            form = tag_one_form(instance=tag1form)
        return render(request, 'crrs_app/Forms/GoalForms/TrainingAwareness/tag1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = tag_one_form(request.POST)
        else:
            tag1form = tag1formdb.objects.get(pk=id)
            form = tag_one_form(request.POST, instance=tag1form)
        if form.is_valid():
            form.save()
            db = tag1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Awareness differs from skill based training; it focuses on making staff more cognizant of their cyber security responsibilities.  To establish an effective awareness program, an organization must identify awareness needs and establish a plan and capability to meet those needs.  Awareness activities focus on staff members developing an understanding of issues, concerns, policies, plans, and practices related to the resilience of the critical service. Awareness sources for the critical service may include:  resilience requirements (protection and sustainment requirements for assets and services)  organizational policies  vulnerabilities being actively managed  laws and regulations (confidentiality and privacy regulations, other federal, state, and local laws that restrict disclosure of information or modification of information)  service continuity and communication plans  event reporting procedures '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' In order to determine what skills the organization must possess to meet its cyber security needs, baseline competencies must be established for the critical service.  Baseline competencies represent the staffing and skill set needs, not what it currently has in terms of staff and skills. Sources of baseline competencies may include:  role (security administrator, network administrator, CIO, etc.)  position (CIO, senior security analyst, network engineer, etc.)  organizational processes such as vulnerability management, incident management, service continuity management, etc.  skills (Java programming, Oracle DBA, etc.)  certifications (CISSP, MSCE, etc.)  aptitudes and job requirements (able to work long hours, travel, or be on call) '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The organization must determine what skills it currently possesses in the assigned personnel and identify skill gaps that can affect their ability to perform assigned cyber security tasks in support of the critical service.  The differences, if any, between the skills the organization currently possess and the required skills (established in TA:G1.Q2) represent skill gaps.  Skill gaps and deficiencies expose the areas where the organization does not have the expertise or experience to meet current needs.  When identifying skills gaps the following should also be considered:  the use of specialized tools  procedures that are new to the individuals who will perform them  These gaps can result in risks to the organization. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = 'These are examples of sources to identify training needs:  The roles and responsibilities of staff in the security, business continuity, and IT operations areas.  The organization’s vulnerability management process.  The organization’s service continuity process.  The organization’s compliance management process.  The organization’s incident management process.  Training needs for external parties that may be supporting the critical service. '
            
            db.save()

        return redirect('/tag1table')
    
def tag1formdelete(request, id):
    tag1form = tag1formdb.objects.get(pk=id)
    tag1form.delete()
    return redirect('/tag1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tag2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = tag_two_form()
        else:
            tag2form = tag2formdb.objects.get(pk=id)
            form = tag_two_form(instance=tag2form)
        return render(request, 'crrs_app/Forms/GoalForms/TrainingAwareness/tag2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = tag_two_form(request.POST)
        else:
            tag2form = tag2formdb.objects.get(pk=id)
            form = tag_two_form(request.POST, instance=tag2form)
        if form.is_valid():
            form.save()
            db = tag2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Awareness activities must meet the broad needs of staff members (established in TA:G1.Q1).  The activities must be scheduled, advertised (if necessary), resourced, and tracked. Typical work products include:  awareness activity materials  newsletters  email campaigns  posters  presentations  awareness activity schedules  awareness activity logistics  list of staff responsible for each awareness activity '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization must perform cyber security training to ensure that staff is appropriately skilled in their roles.  Training should be planned and scheduled.  Training provided should address identified skill gaps (established in TA:G1.Q3) including:  training in the use of specialized tools  training in procedures that are new to the individuals who will perform them Typical work products include:  delivered training courses  training schedule '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' A process should exist to determine the effectiveness of the awareness and training programs in meeting the needs of staff that support the critical service. Examples of methods to evaluate the effectiveness:  testing on the presented material  post-training surveys (e.g. instructor evaluation, manager feedback)  focus groups  selective interviews  behavioral measures (password strength could be evaluated before and after a passwordawareness activity.)  observations, evaluations, and benchmarking activities '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Capabilities for implementing the awareness and training plan must be established and maintained, including:  the selection of appropriate training approaches  sourcing or developing training materials  obtaining appropriate instructors  announcing the training schedule  revising the awareness and training capability as needed Situations in which awareness and training materials may need to be revised:  training needs change (e.g., new technology is deployed)  an evaluation of the training identifies the need for change  changes in existing awareness needs and requirements  emergence of new awareness needs and requirements  assessments on the effectiveness of awareness and training activities (Established in TA:G2.Q3)  training refresh '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' Role-based security training is provided to privileged users with assigned security roles and responsibilities:  before authorizing their access to the information system or before they perform their assigned duties  when required by information system changes  periodically (frequency defined by the organization) thereafter  Comprehensive role-based training addresses management, operational, and technical roles and responsibilities.  Role-based security training also applies to contractors providing services'
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' Role-based security training is provided to senior executives with assigned security roles and responsibilities:  before authorizing their access to the information system  when required by information system changes  periodically (frequency defined by the organization) thereafter  Comprehensive role-based training addresses management, operational, and technical roles and responsibilities.'
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = ' Role-based security training is provided to physical and information security personnel with assigned security roles and responsibilities:  before authorizing their access to the information system or before they perform their assigned duties  when required by information system changes  periodically (frequency defined by the organization) thereafter  Comprehensive role-based training addresses management, operational, and technical roles and responsibilities.  Role-based security training also applies to contractors providing services. '
            
            db.save()

        return redirect('/tag2table')

def tag2formdelete(request, id):
    tag2form = tag2formdb.objects.get(pk=id)
    tag2form.delete()
    return redirect('/tag2table')


# VulnerabilityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])   
def vmg1form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmg_one_form()
        else:
            vmg1form = vmg1formdb.objects.get(pk=id)
            form = vmg_one_form(instance=vmg1form)
        return render(request, 'crrs_app/Forms/GoalForms/VulnerabilityManagement/vmg1form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmg_one_form(request.POST)
        else:
            vmg1form = vmg1formdb.objects.get(pk=id)
            form = vmg_one_form(request.POST, instance=vmg1form)
        if form.is_valid():
            form.save()
            db = vmg1formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The strategy for addressing vulnerability analysis and resolution should be documented, communicated to relevant stakeholders, and implemented.  The strategy may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. The vulnerability analysis and resolution strategy should address:  The scope of assets relevant to the critical service.  The scoping should be driven by the resilience requirements of the service and the identified assets.  The essential activities that are required for vulnerability identification, analysis, and resolution.  A process for organizing, categorizing, comparing, and consolidating vulnerabilities.  Approved tools, techniques, and methods.  A schedule for performing vulnerability activities.  The skills and training required.  Relevant stakeholders of the vulnerability activities and their roles. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Pre-approving tools, techniques, and methods ensures consistency, as well as validity of results.  The tools and methods should cover all the assets that support the critical service.  The tools and methods can be both procedural and automated.'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' The organization employs malicious code protection mechanisms at information system entry and exit points to detect and eradicate malicious code.  The organization updates malicious code protection mechanisms whenever new releases are available.  The organization performs periodic scans (as defined by the organization) of the information system and real-time scans of files from external sources. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Mobile code technologies include:  Java and JavaScript  ActiveX  PDFs  Shockwave movies  Flash animations  The organization should:  define acceptable and unacceptable mobile code technologies  establish usage restrictions and implementation guidance  authorize, monitor, and control the use of mobile code within information systems  Corrective actions when unacceptable mobile code is detected include:  blocking file transmissions  quarantining  alerting administrators/security personnel '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' Enforce physical access controls to information systems in addition to the physical access controls for facilities (badging system, guard rounds, etc.).  Monitor physical access to facilities where the information systems reside to detect and respond to physical security incidents.  Monitor information systems to detect unauthorized local, network, and remote connections.  Information system monitoring capability is achieved through a variety of tools and techniques that may include:  intrusion detection systems  intrusion prevention systems  audit record monitoring software  network monitoring software '
           
            db.save()

        return redirect('/vmg1table')

def vmg1formdelete(request, id):
    vmg1form = vmg1formdb.objects.get(pk=id)
    vmg1form.delete()
    return redirect('/vmg1table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmg2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmg_two_form()
        else:
            vmg2form = vmg2formdb.objects.get(pk=id)
            form = vmg_two_form(instance=vmg2form)
        return render(request, 'crrs_app/Forms/GoalForms/VulnerabilityManagement/vmg2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmg_two_form(request.POST)
        else:
            vmg2form = vmg2formdb.objects.get(pk=id)
            form = vmg_two_form(request.POST, instance=vmg2form)
        if form.is_valid():
            form.save()
            db = vmg2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Internal sources typically provide information about vulnerabilities that are unique to the organization.  Internal processes, such as incident management, could be an internal source of vulnerability information.  External or public sources typically provide information that is focused on common technologies.Example sources of vulnerability information:  vendors of software, systems, and hardware technologies  common free catalogs, such as:  US-CERT Vulnerability Database  The Common Vulnerabilities and Exposures (CVE) List  industry groups  results of executing automated tools, techniques, and methods '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Vulnerability data collection is a continuous process.  The information from the sources (established in VM:G2.Q1) needs to be continually updated.  New sources of vulnerability information must also be added to the source list as they emerge. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Vulnerabilities are discovered from an active review of the organization’s standard list of vulnerability sources. Techniques used to discover vulnerabilities include:  performing internal vulnerability audits or assessments  performing assessments of external entities  reviewing the results of internal and external audits  periodically reviewing vulnerability catalogs, such as the US-CERT  reviewing notifications from identified vendor services  reviewing notifications from identified vulnerability services  reviewing reports from industry groups  using reports of vulnerabilities from other processes such as the organization’s service desk'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Prioritization can be:  qualitative (high, medium, or low)  quantitative (through a numerical scale)  Prioritization provides the organization a structured means for determining the appropriate categorization. Examples of categories based on actions to be taken for vulnerability resolution:  take no action; ignore  fix immediately (typically the case for vendor updates or changes)  develop and implement a vulnerability resolution strategy (typically the case when the resolution is more extensive than simple actions such as vendor updates)  perform additional research and analysis  refer the vulnerability to the risk management process for formal risk consideration Typical Work Products:  vulnerability categorization and prioritization guidelines  list of vulnerabilities categorized and prioritized for disposition  updated vulnerability repository '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = ' Through vulnerability analysis, the organization seeks to understand the potential threat that the vulnerability represents.  The organization should assign a course of action to each vulnerability based upon its relevance to the organization. Vulnerability analysis includes activities to:  understand the threat and exposure  review trend information to determine whether the vulnerability existed before and what actions were taken to reduce or eliminate it  identify and understand underlying causes for exposure to the vulnerability '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' A vulnerability repository should be used as the central source of vulnerability lifecycle information.  A vulnerability repository supports analysis, disposition, trending, root cause analysis, and vulnerability management. Information that should be recorded includes:  a unique identifier  description of the vulnerability  date entered into the repository  references to the source of the vulnerability  the priority of the vulnerability (high, medium, low)  categorization and disposition of the vulnerability  individuals or teams assigned to analyze and remediate the vulnerability  a log of actions taken to reduce or eliminate the vulnerability '
            
            db.save()

        return redirect('/vmg2table')
def vmg2formdelete(request, id):
    vmg2form = vmg2formdb.objects.get(pk=id)
    vmg2form.delete()
    return redirect('/vmg2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmg3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmg_three_form()
        else:
            vmg3form = vmg3formdb.objects.get(pk=id)
            form = vmg_three_form(instance=vmg3form)
        return render(request, 'crrs_app/Forms/GoalForms/VulnerabilityManagement/vmg3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmg_three_form(request.POST)
        else:
            vmg3form = vmg3formdb.objects.get(pk=id)
            form = vmg_three_form(request.POST, instance=vmg3form)
        if form.is_valid():
            form.save()
            db = vmg3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The organization must develop and implement a resolution strategy to manage exposure from identified vulnerabilities. The resolution strategy may include actions to:  Minimize the organization’s exposure to the vulnerability (by reducing the likelihood that the vulnerability will be exploited).  Eliminate the organization’s exposure to the vulnerability. Actions taken to manage exposure may include:  implementing software, systems, and firmware patches  developing and implementing operational workarounds  developing and implementing new protective controls  updating existing controls  developing and implementing new service continuity plans, or updating existing plansTypical Work Products:  vulnerability management strategies or action plans  updated vulnerability repository, with resolution status information  vulnerability management strategy status reports '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' The organization should review mitigation activities to ensure they are effective in reducing or eliminating the exposure to identified vulnerabilities. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Unresolved vulnerabilities should be regularly monitored and reported. Unresolved vulnerabilities are typically those whose disposition is:  to monitor a vulnerability resolution strategy that remains incomplete  to perform additional research and analysis  to refer the vulnerability to the risk management process for formal risk consideration'
            
            db.save()

        return redirect('/vmg3table')

def vmg3formdelete(request, id):
    vmg3form = vmg3formdb.objects.get(pk=id)
    vmg3form.delete()
    return redirect('/vmg3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmg4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmg_four_form()
        else:
            vmg4form = vmg4formdb.objects.get(pk=id)
            form = vmg_four_form(instance=vmg4form)
        return render(request, 'crrs_app/Forms/GoalForms/VulnerabilityManagement/vmg4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmg_four_form(request.POST)
        else:
            vmg4form = vmg4formdb.objects.get(pk=id)
            form = vmg_four_form(request.POST, instance=vmg4form)
        if form.is_valid():
            form.save()
            db = vmg4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Root-cause analysis is a general approach for determining the underlying causes of vulnerabilities and how to eliminate or reduce them. Underlying causes of vulnerabilities may include:  poor software design  failure of organizational policies and processes  improper training  operational complexity Activities to address the root causes of identified vulnerabilities include:  developing or improving controls  using strategies for sustaining assets and services  updating training and awareness activities  correcting practices and processes that result in exposures  developing lessons learned Typical Work Products:  root-cause analysis reports  an updated vulnerability repository with analysis results '
           
            db.save()

        return redirect('/vmg4table')

def vmg4formdelete(request, id):
    vmg4form = vmg4formdb.objects.get(pk=id)
    vmg4form.delete()
    return redirect('/vmg4table')


# MILForms
# AssetManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ammil_two_form()
        else:
            ammil2form = ammil2formdb.objects.get(pk=id)
            form = ammil_two_form(instance=ammil2form)
        return render(request, 'crrs_app/Forms/MILForms/AssetManagement/ammil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ammil_two_form(request.POST)
        else:
            ammil2form = ammil2formdb.objects.get(pk=id)
            form = ammil_two_form(request.POST, instance=ammil2form)
        if form.is_valid():
            form.save()
            db = ammil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines asset management within the organization and prescribes how asset management activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the asset management process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform asset management activities  establishment of procedures, standards, and guidelines  establishing and maintaining an asset inventory  managing access to assets  categorizing, safeguarding, and disposing of information assets  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the asset management process have the following responsibilities:  creating an asset inventory baseline  associating assets with the critical service  overseeing the asset management process  managing the risk resulting from unresolved problems (gaps in the inventory of asset protection and sustainment requirements, insufficient staffing or funding, etc.) Examples of stakeholders include:  critical service owners  asset management staff  owners and custodians of assets that underpin the service (to include facility security personnel)  critical service staff  external entities responsible for some part of the service  information technology staff  human resources  internal and external auditors '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of asset management activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  establishing an asset inventory  documenting asset descriptions and relevant information  identifying asset owners  identifying asset custodians  assigning access to assets  sensitivity categorization for information assets  documenting asset resilience requirements '

            db.save()

        return redirect('/ammil2table')

def ammil2formdelete(request, id):
    ammil2form = ammil2formdb.objects.get(pk=id)
    ammil2form.delete()
    return redirect('/ammil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ammil_three_form()
        else:
            ammil3form = ammil3formdb.objects.get(pk=id)
            form = ammil_three_form(instance=ammil3form)
        return render(request, 'crrs_app/Forms/MILForms/AssetManagement/ammil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ammil_three_form(request.POST)
        else:
            ammil3form = ammil3formdb.objects.get(pk=id)
            form = ammil_three_form(request.POST, instance=ammil3form)
        if form.is_valid():
            form.save()
            db = ammil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the asset management activities.  Oversight provides visibility into the asset management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing, or spot checks. Examples of corrective actions:  taking actions to repair defective work products (access control lists, outdated asset profiles, excessive access privileges, improper disposal of sensitive information, etc.) or services  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in the asset management activities  escalating issues that require higher-level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'evaluate the qualifications of the staff, not the completeness of the plan.  Qualified means that staff are appropriately skilled to perform asset management activities. Examples of staff include personnel responsible for:  developing and maintaining the asset inventory, including asset profiles  identifying asset’s dependencies  documenting changes to assets in the asset inventory  implementing processes, standards, and guidelines  addressing issues and problems, including developing and executing remediation plans Examples of skills needed include:  knowledge of the tools, techniques, and methods necessary to identify and inventory assets  knowledge necessary to identify, document, and manage assets through their lifecycle  knowledge of sensitivity categories for information assets '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher-level management support and sponsorship of asset management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned asset management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing asset management activities (asset management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the asset management process include:  poorly defined asset management processes  inadequate staffing  inadequate funding '
            
            db.save()

        return redirect('/ammil3table')

def ammil3formdelete(request, id):
    ammil3form = ammil3formdb.objects.get(pk=id)
    ammil3form.delete()
    return redirect('/ammil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ammil_four_form()
        else:
            ammil4form = ammil4formdb.objects.get(pk=id)
            form = ammil_four_form(instance=ammil4form)
        return render(request, 'crrs_app/Forms/MILForms/AssetManagement/ammil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ammil_four_form(request.POST)
        else:
            ammil4form = ammil4formdb.objects.get(pk=id)
            form = ammil_four_form(request.POST, instance=ammil4form)
        if form.is_valid():
            form.save()
            db = ammil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the asset management process are needed to ensure that:  the asset inventory is up to date  excessive access to assets is identified and remediated  the quality of particular work products meets established guidelines  risk related to asset management problem areas are identified and addressed  actions requiring management involvement are elevated in a timely manner Example metrics of the asset management process may include:  number of assets with incomplete asset profiles  number of discrepancies between the current inventory and the documented inventory  assets that do not have an assigned owner or custodian  the level of adherence to the asset management plan and processes '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Periodic (as defined by the organization) reviews for adherence to the asset management plan are needed to ensure that:  Activities are performed as planned and adhere to process descriptions, standards, and procedures.  Deviations from the plan are identified and evaluated.  Problems in the plan for performing asset management activities are identified.  Non-compliance is addressed.  Needed process changes are identified when expected results or outputs are not met. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher-level managers include those in the organization above the immediate level of management responsible for the asset management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher-level managers typically includes:  status reviews of asset management activities '
            
            db.save()

        return redirect('/ammil4table')

def ammil4formdelete(request, id):
    ammil4form = ammil4formdb.objects.get(pk=id)
    ammil4form.delete()
    return redirect('/ammil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ammil_five_form()
        else:
            ammil5form = ammil5formdb.objects.get(pk=id)
            form = ammil_five_form(instance=ammil5form)
        return render(request, 'crrs_app/Forms/MILForms/AssetManagement/ammil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ammil_five_form(request.POST)
        else:
            ammil5form = ammil5formdb.objects.get(pk=id)
            form = ammil_five_form(request.POST, instance=ammil5form)
        if form.is_valid():
            form.save()
            db = ammil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in asset management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow including diagrams  inputs and expected outputs  performance measures for improvement'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the asset management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned from process reviews  lessons learned in the post-event review of incidents and disruptions in continuity '
            
            db.save()

        return redirect('/ammil5table')

def ammil5formdelete(request, id):
    ammil5form = ammil5formdb.objects.get(pk=id)
    ammil5form.delete()
    return redirect('/ammil5table')


#ConfigurationChangeManagement  

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ccmmil_two_form()
        else:
            ccmmil2form = ccmmil2formdb.objects.get(pk=id)
            form = ccmmil_two_form(instance=ccmmil2form)
        return render(request, 'crrs_app/Forms/MILForms/ConfigurationChangeManagement/ccmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ccmmil_two_form(request.POST)
        else:
            ccmmil2form = ccmmil2formdb.objects.get(pk=id)
            form = ccmmil_two_form(request.POST, instance=ccmmil2form)
        if form.is_valid():
            form.save()
            db = ccmmil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines change management within the organization and prescribes how change management activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. The plan typically includes:  change management activities (change management process, establishing and managing baselines, capacity management, etc.)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders  measurement and reporting requirements  training requirements  management oversight '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the change management process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform change management activities  establishment of procedures, standards, and guidelines  requesting and approving changes to assets  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the change management process have the following responsibilities:  creating asset baselines  overseeing the change management process  capacity management planning  configuration management  requesting and approving changes to assets  resolving issues in the change management process Examples of stakeholders include:  critical service owners  management  change management staff  owners and custodians of assets that underpin the service  critical service staff  external entities responsible for some part of the service  information technology staff  staff responsible for physical security  human resources  internal and external auditors'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of change management activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  documenting and maintaining asset descriptions  documenting changes to resilience requirements for assets  capacity management  stakeholder notification  configuration management including baselines  requesting, approving, and implementing changes to assets'
            
            db.save()

        return redirect('/ccmmil2table')

def ccmmil2formdelete(request, id):
    ccmmil2form = ccmmil2formdb.objects.get(pk=id)
    ccmmil2form.delete()
    return redirect('/ccmmil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ccmmil_three_form()
        else:
            ccmmil3form = ccmmil3formdb.objects.get(pk=id)
            form = ccmmil_three_form(instance=ccmmil3form)
        return render(request, 'crrs_app/Forms/MILForms/ConfigurationChangeManagement/ccmmil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ccmmil_three_form(request.POST)
        else:
            ccmmil3form = ccmmil3formdb.objects.get(pk=id)
            form = ccmmil_three_form(request.POST, instance=ccmmil3form)
        if form.is_valid():
            form.save()
            db = ccmmil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Question Intent: To determine if management oversight exists. The intent of oversight is to ensure the direct day-to-day monitoring of the change management activities.  Management consists of the immediate level of managers that govern the day-to-day operation of the change management activities.  Oversight provides visibility into the change management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing, or spot checks. Examples of corrective actions:  taking actions to repair defective work products (baselines, configuration items, capacity management plans, documentation)  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.) '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Examples of staff include personnel responsible for:  change management  configuration management  capacity management  implementing processes, standards, and guidelines  addressing issues and problems, including developing and executing remediation plans Examples of skills needed include:  knowledge of the service to effectively evaluate requested changes  knowledge necessary to elicit and prioritize stakeholder requirements and interpret them to develop effective change control procedures  proficiency with tools, techniques, and methods '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher-level management support and sponsorship of change management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned change management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing change management activities (change management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the change management process include:  poorly defined change management processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools  lack of a documented plan, policy, standards, and guidelines  lack of stakeholder involvement  lack of management oversight '
            
            db.save()

        return redirect('/ccmmil3table')

def ccmmil3formdelete(request, id):
    ccmmil3form = ccmmil3formdb.objects.get(pk=id)
    ccmmil3form.delete()
    return redirect('/ccmmil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ccmmil_four_form()
        else:
            ccmmil4form = ccmmil4formdb.objects.get(pk=id)
            form = ccmmil_four_form(instance=ccmmil4form)
        return render(request, 'crrs_app/Forms/MILForms/ConfigurationChangeManagement/ccmmil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ccmmil_four_form(request.POST)
        else:
            ccmmil4form = ammil4formdb.objects.get(pk=id)
            form = ccmmil_four_form(request.POST, instance=ccmmil4form)
        if form.is_valid():
            form.save()
            db = ccmmil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the change management process are needed to ensure that:  unauthorized changes are identified, tracked, and addressed  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risks related to change management activities are identified and addressed  actions requiring management involvement are elevated in a timely manner Example metrics of the change management process may include:  number of requested changes per asset  number of unauthorized or unexplained changes  number of approved but unincorporated changes  number of times stakeholders weren’t notified of approved changes  number of times an approved change is implemented and then reversed  percentage of technology assets that deviate from approved configuration baselines'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' This review is often done by an independent entity (either internal or external to the organization). Periodic (as defined by the organization) reviews for adherence to the change management plan are needed to ensure that:  Activities are performed as planned and adhere to process descriptions, standards, and procedures.  Deviations from the plan are identified and evaluated.  Problems in the plan for performing change management activities are identified.  Non-compliance is addressed.  Needed process changes are identified when expected results or outputs are not met. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher-level managers include those in the organization above the immediate level of management responsible for the change management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher-level managers typically includes:  status reviews of change management activities  issues identified in process and plan reviews  risks associated with change management activities  recommendations for improvement '
            
            db.save()

        return redirect('/ccmmil4table')

def ccmmil4formdelete(request, id):
    ccmmil4form = ccmmil4formdb.objects.get(pk=id)
    ccmmil4form.delete()
    return redirect('/ccmmil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = ccmmil_five_form()
        else:
            ccmmil5form = ccmmil5formdb.objects.get(pk=id)
            form = ccmmil_five_form(instance=ccmmil5form)
        return render(request, 'crrs_app/Forms/MILForms/ConfigurationChangeManagement/ccmmil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = ccmmil_five_form(request.POST)
        else:
            ccmmil5form = ccmmil5formdb.objects.get(pk=id)
            form = ccmmil_five_form(request.POST, instance=ccmmil5form)
        if form.is_valid():
            form.save()
            db = ccmmil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in change management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the change management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned from the execution and review of change management activities  direct feedback from stakeholders  improvements based on executed or tested service continuity plans'
           
            db.save()

        return redirect('/ccmmil5table')

def ccmmil5formdelete(request, id):
    ccmmil5form = ccmmil5formdb.objects.get(pk=id)
    ccmmil5form.delete()
    return redirect('/ccmmil5table')


#controlsmanagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmmil_two_form()
        else:
            cmmil2form = cmmil2formdb.objects.get(pk=id)
            form = cmmil_two_form(instance=cmmil2form)
        return render(request, 'crrs_app/Forms/MILForms/ControlsManagement/cmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmmil_two_form(request.POST)
        else:
            cmmil2form = cmmil2formdb.objects.get(pk=id)
            form = cmmil_two_form(request.POST, instance=cmmil2form)
        if form.is_valid():
            form.save()
            db = cmmil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines controls management within the organization and prescribes how controls management activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. The plan typically includes:  control management activities (control design, analysis and assessment methodology)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders  measurement and reporting requirements  training requirements  management oversight '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the controls management process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform controls management activities  establishment of procedures, standards, and guidelines  requirements for periodically assessing the control environment  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the controls management process have the following responsibilities:  defining and managing control objectives and controls, including ensuring the effectiveness of controls  overseeing the controls management process  managing the risk resulting from unresolved problems (gaps in controls, insufficient staffing or funding, etc.) Examples of stakeholders include:  critical service owners  management  controls management staff  owners and custodians of assets that underpin the service  critical service staff  external entities responsible for some part of the service  information technology staff  staff responsible for physical security  human resources  internal and external auditors '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of controls management activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  defining and selecting control objectives  prioritizing control objectives  implementing controls to meet objectives (for example, controls could be selected from the NIST 800-53 recommended security control, NERC CIP standards, and Control Objectives for Information and Related Technology [COBIT] standard).  evaluating and acquiring tools for monitoring the performance of controls  analyzing and assessing controls  identifying gaps in controls and approaches for addressing them  identifying redundant and conflicting controls  identifying risks associated with problems in the control environment  periodically assessing the control environment '
            
            db.save()

        return redirect('/cmmil2table')

def cmmil2formdelete(request, id):
    cmmil2form = cmmil2formdb.objects.get(pk=id)
    cmmil2form.delete()
    return redirect('/cmmil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmmil_three_form()
        else:
            cmmil3form = cmmil3formdb.objects.get(pk=id)
            form = cmmil_three_form(instance=cmmil3form)
        return render(request, 'crrs_app/Forms/MILForms/ControlsManagement/cmmil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmmil_three_form(request.POST)
        else:
            cmmil3form = cmmil3formdb.objects.get(pk=id)
            form = cmmil_three_form(request.POST, instance=cmmil3form)
        if form.is_valid():
            form.save()
            db = cmmil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the controls management activities.  Oversight provides visibility into the controls management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing or spot checks. Examples of corrective actions:  taking actions to repair defective work products (assessment results, control designs, control objectives, documentation) or services  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in the controls management activities  escalating issues that require higher-level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Qualified means that staff are appropriately skilled to perform controls management activities. Examples of staff include personnel responsible for:  designing, implementing, and assessing controls  implementing processes, standards, and guidelines  addressing issues and problems, including developing and executing remediation plans Examples of skills needed include:  knowledge necessary to elicit and prioritize stakeholder requirements and interpret them to develop effective control objectives  knowledge of control objectives necessary for control design  proficiency with tools, techniques, and methods used to design, analyze, assess, and manage '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher-level management support and sponsorship of controls management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned controls management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc.'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing controls management activities (controls management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the controls management process include:  poorly defined controls management processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools  lack of a documented plan, policy, standards, and guidelines  lack of stakeholder involvement  lack of management oversight '
           
            db.save()

        return redirect('/cmmil3table')

def cmmil3formdelete(request, id):
    cmmil3form = cmmil3formdb.objects.get(pk=id)
    cmmil3form.delete()
    return redirect('/cmmil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmmil_four_form()
        else:
            cmmil4form = cmmil4formdb.objects.get(pk=id)
            form = cmmil_four_form(instance=cmmil4form)
        return render(request, 'crrs_app/Forms/MILForms/ControlsManagement/cmmil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmmil_four_form(request.POST)
        else:
            cmmil4form = cmmil4formdb.objects.get(pk=id)
            form = cmmil_four_form(request.POST, instance=cmmil4form)
        if form.is_valid():
            form.save()
            db = cmmil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the controls management process are needed to ensure that:  control objectives continue to be satisfied  control problem areas are identified and remediated  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risk related to control problem areas are identified and addressed  actions requiring management involvement are elevated in a timely manner Example metrics of the controls management process may include:  percentage of control objectives that are fully satisfied by existing controls  time and resources expended to conduct an analysis (baseline) or assessment (periodic) of controls  number of problem areas resulting from assessments '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' This review is often done by an independent entity (either internal or external to the organization). Periodic (as defined by the organization) reviews for adherence to the controls management plan are needed to ensure that:  Activities are performed as planned and adhere to process descriptions, standards, and procedures.  Deviations from the plan are identified and evaluated.  Problems in the plan for performing controls management activities are identified.  Non-compliance is addressed.  Needed process changes are identified when expected results or outputs are not met. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher-level managers include those in the organization above the immediate level of management responsible for the controls management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher-level managers typically includes:  status reviews of controls management activities  issues identified in process and plan reviews  risks associated with controls management activities.  recommendations for improvement '
            
            db.save()

        return redirect('/cmmil4table')

def cmmil4formdelete(request, id):
    cmmil4form = cmmil4formdb.objects.get(pk=id)
    cmmil4form.delete()
    return redirect('/cmmil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = cmmil_five_form()
        else:
            cmmil5form = cmmil5formdb.objects.get(pk=id)
            form = cmmil_five_form(instance=cmmil5form)
        return render(request, 'crrs_app/Forms/MILForms/ControlsManagement/cmmil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = cmmil_five_form(request.POST)
        else:
            cmmil5form = cmmil5formdb.objects.get(pk=id)
            form = cmmil_five_form(request.POST, instance=cmmil5form)
        if form.is_valid():
            form.save()
            db = cmmil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in controls management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the controls management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned from control analysis and assessments  lessons learned from satisfying control objectives  risk evaluations '
            
            db.save()

        return redirect('/cmmil5table')

def cmmil5formdelete(request, id):
    cmmil5form = cmmil5formdb.objects.get(pk=id)
    cmmil5form.delete()
    return redirect('/cmmil5table')


# ExternalDependenciesManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmmil_two_form()
        else:
            edmmil2form = edmmil2formdb.objects.get(pk=id)
            form = edmmil_two_form(instance=edmmil2form)
        return render(request, 'crrs_app/Forms/MILForms/ExternalDependenciesManagement/edmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmmil_two_form(request.POST)
        else:
            edmmil2form = edmmil2formdb.objects.get(pk=id)
            form = edmmil_two_form(request.POST, instance=edmmil2form)
        if form.is_valid():
            form.save()
            db = edmmil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines external dependency management within the organization and prescribes how external dependency management activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents.  A vendor management or contract management program and plan may suffice if it encompasses planning elements similar to those listed below. The plan typically includes:  external dependency management activities (external dependency identification, prioritization, performance management, etc.)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders  measurement and reporting requirements  training requirements  management oversight '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the external dependency management process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform external dependency management activities  establishment of procedures, standards, and guidelines  requirements for periodically assessing the external dependency management activities  requesting, approving, providing, and terminating access for external entities  requesting, approving, providing, and terminating agreements with external entities  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the external dependency management process have the following responsibilities: overseeing the external dependency management process resolving issues with the external dependency management process planning for evaluating, selecting, and managing relationships with external entities creating and maintaining a prioritized inventory of all external dependencies monitoring the performance of external entities ensuring that service continuity plans reflect all external dependencies managing the operational risk that arises from external dependenciesExamples of stakeholders include: critical service owners management owners of external entity relationships external dependency management program staff owners and custodians of assets that underpin the service critical service staff external entities responsible for some part of the service information technology staff staff responsible for physical security '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of external dependency management activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  identifying and prioritizing external dependencies  associating external dependencies with services and assets  managing operational risks resulting from external entities  evaluating and selecting external entities  standards of performance and service levels  periodically monitoring the performance of external entities  establishing service continuity plans and procedures for external entities  terminating relationships with entities  issue escalation and dispute resolution procedures '
            
            db.save()

        return redirect('/edmmil2table')

def edmmil2formdelete(request, id):
    edmmil2form = edmmil2formdb.objects.get(pk=id)
    edmmil2form.delete()
    return redirect('/edmmil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmmil_three_form()
        else:
            edmmil3form = edmmil3formdb.objects.get(pk=id)
            form = edmmil_three_form(instance=edmmil3form)
        return render(request, 'crrs_app/Forms/MILForms/ExternalDependenciesManagement/edmmil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmmil_three_form(request.POST)
        else:
            edmmil3form = edmmil3formdb.objects.get(pk=id)
            form = edmmil_three_form(request.POST, instance=edmmil3form)
        if form.is_valid():
            form.save()
            db = edmmil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the external dependency management activities.  Oversight provides visibility into the external dependency management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing or spot checks. Examples of corrective actions:  taking actions to repair defective work products or services  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in the external dependency management activities  escalating issues that require higher level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Examples of staff include personnel responsible for:  preparing request for proposals (RFPs), including applicable service level agreements (SLAs)  evaluating proposals and selecting external entities  establishing formal agreements with external entities  inspecting deliverables  monitoring the performance of external entities  service continuity as it involves external dependencies Examples of skills needed include:  identifying and prioritizing external dependencies  elicitation of resilience specifications to be reflected in RFPs and agreements  evaluating and selecting external entities '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher level management support and sponsorship of external dependency management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned external dependency management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing external dependency management activities (external dependency management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the external dependency management process include:  poorly defined external dependency management processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools '
            
            db.save()

        return redirect('/edmmil3table')

def edmmil3formdelete(request, id):
    edmmil3form = edmmil3formdb.objects.get(pk=id)
    edmmil3form.delete()
    return redirect('/edmmil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmmil_four_form()
        else:
            edmmil4form = edmmil4formdb.objects.get(pk=id)
            form = edmmil_four_form(instance=edmmil4form)
        return render(request, 'crrs_app/Forms/MILForms/ExternalDependenciesManagement/edmmil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmmil_four_form(request.POST)
        else:
            edmmil4form = edmmil4formdb.objects.get(pk=id)
            form = edmmil_four_form(request.POST, instance=edmmil4form)
        if form.is_valid():
            form.save()
            db = edmmil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the external dependency management process are needed to ensure that:  external dependency performance issues are identified and remediated  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risks related to external dependency performance are identified and addressed  actions requiring management involvement are elevated in a timely manner  new external dependencies are included and prioritized  agreements with external entities include stated resilience requirements  the mapping of external dependencies to services and assets is accurate and current Example metrics of the external dependency management process may include:  number of performance issues resulting from external entity monitoring  percentage of external entities whose deliverables do not meet expectations  number of external dependency risks where corrective action is still pending  level of adherence to external dependency related policies '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Periodic (as defined by the organization) reviews for adherence to the external dependency management plan are needed to ensure that:  Activities are performed as planned and adhere to process descriptions, standards, and procedures.  Deviations from the plan are identified and evaluated.  Problems in the plan for performing external dependency management activities are identified.  Non-compliance is addressed.  Needed process changes are identified when expected results or outputs are not met. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher-level managers include those in the organization above the immediate level of management responsible for the external dependency management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher-level managers typically includes:  status reviews of external dependency management activities  issues identified in process and plan reviews  risks associated with external dependency management activities  recommendations for improvement '
            
            db.save()

        return redirect('/edmmil4table')

def edmmil4formdelete(request, id):
    edmmil4form = edmmil4formdb.objects.get(pk=id)
    edmmil4form.delete()
    return redirect('/edmmil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = edmmil_five_form()
        else:
            edmmil5form = edmmil5formdb.objects.get(pk=id)
            form = edmmil_five_form(instance=edmmil5form)
        return render(request, 'crrs_app/Forms/MILForms/ExternalDependenciesManagement/edmmil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = edmmil_five_form(request.POST)
        else:
            edmmil5form = edmmil5formdb.objects.get(pk=id)
            form = edmmil_five_form(request.POST, instance=edmmil5form)
        if form.is_valid():
            form.save()
            db = edmmil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in external dependency management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the external dependency management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned in post-event review of external entity incidents and disruptions in continuity  lessons learned in managing an external entity  improvements based on risk identification and mitigation  improvements based on executed or tested service continuity plans that rely on external entities '
            
            db.save()

        return redirect('/edmmil5table')

def edmmil5formdelete(request, id):
    edmmil5form = edmmil5formdb.objects.get(pk=id)
    edmmil5form.delete()
    return redirect('/edmmil5table')


# IncidentManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = immil_two_form()
        else:
            immil2form = immil2formdb.objects.get(pk=id)
            form = immil_two_form(instance=immil2form)
        return render(request, 'crrs_app/Forms/MILForms/IncidentManagement/immil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = immil_two_form(request.POST)
        else:
            immil2form = immil2formdb.objects.get(pk=id)
            form = immil_two_form(request.POST, instance=immil2form)
        if form.is_valid():
            form.save()
            db = immil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines incident management within the organization and prescribes how incident management activities will be performed.  The plan may be a standalone document, embedded in a more comprehensive document, or distributed across multiple documents. The plan typically includes:  incident management activities (event detection, incident declaration, incident analysis, etc.)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders  measurement and reporting requirements  training requirements  management oversight '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to its employees.  It establishes the organizational expectations for planning and performing the incident management process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform incident management activities  establishment of procedures, standards, and guidelines  requirements for periodically assessing incident management activities  post-incident review, problem resolution, and closure  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the incident management process have the following responsibilities:  overseeing the incident management process  making critical decisions during the incident management process  resolving issues with the incident management process  detecting events and incidents  planning for incident handling, management, and response  collecting, documenting, and preserving event and incident evidence  analyzing events and incidents  declaring incidents Examples of stakeholders include:  critical service owners and staff  management  incident manages  incident owners '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of incident management activities meets standards and is predictable, measurable, and repeatable.'
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = 'Standards and guidelines typically address:  detecting, logging, reporting, and tracking events  collecting and preserving evidence  triaging events  analyzing events  declaring an incident from one or more events  responding to incidents, including escalation procedures  incident communication protocols  creating and maintaining the incident knowledgebase '
            
            db.save()

        return redirect('/immil2table')

def immil2formdelete(request, id):
    immil2form = immil2formdb.objects.get(pk=id)
    immil2form.delete()
    return redirect('/immil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = immil_three_form()
        else:
            immil3form = immil3formdb.objects.get(pk=id)
            form = immil_three_form(instance=immil3form)
        return render(request, 'crrs_app/Forms/MILForms/IncidentManagement/immil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = immil_three_form(request.POST)
        else:
            immil3form = immil3formdb.objects.get(pk=id)
            form = immil_three_form(request.POST, instance=immil3form)
        if form.is_valid():
            form.save()
            db = immil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the incident management activities.  Oversight provides visibility into the incident management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing, or spot checks. Examples of corrective actions:  taking actions to repair defective work products or services  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in the incident management activities  escalating issues that require higher level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Qualified means that staff are appropriately skilled to perform incident management activities. Examples of staff include personnel responsible for:  detecting, logging, analyzing, reporting, and tracking events  collecting and preserving evidence  declaring an incident from one or more events  managing incidents and making critical decisions  analyzing and responding to incidents, including escalation procedures  communicating incidents Examples of skills needed include:  event detection, reporting, and tracking, including service desk activities  documenting and logging event reports  collecting and preserving evidence  declaring incidents  incident analysis '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher level management support and sponsorship of incident management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned incident management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing incident management activities (incident management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the incident management process include:  poorly defined incident management processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools '
            if request.POST['response_five'] == 'yes':
                db.feedback['response_five'] = 'Excellent'
            elif request.POST['response_five'] == 'no':
                db.feedback['response_five'] = 'Periodic (as defined by the organization) reviews of the incident management process are needed to ensure that:  incident management performance issues are identified and remediated  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risks related to incident management performance are identified and addressed  actions requiring management involvement are elevated in a timely manner  events and incidents are identified, reported, and addressed in a timely manner Example metrics of the incident management process may include:  number of work products that don’t meet standards  number of incidents that did not undergo post-incident review  number of open incident management process performance issues  percentage of incidents that are the result of exploited vulnerabilities '
            if request.POST['response_six'] == 'yes':
                db.feedback['response_six'] = 'Excellent'
            elif request.POST['response_six'] == 'no':
                db.feedback['response_six'] = ' This review is often done by an independent entity (either internal or external to the organization). Periodic (as defined by the organization) reviews for adherence to the incident management plan are needed to ensure that:  activities are performed as planned and adhere to process descriptions, standards, and procedures  deviations from the plan are identified and evaluated  problems in the plan for performing incident management activities are identified  non-compliance is addressed  needed process changes are identified when expected results or outputs are not met '
            if request.POST['response_seven'] == 'yes':
                db.feedback['response_seven'] = 'Excellent'
            elif request.POST['response_seven'] == 'no':
                db.feedback['response_seven'] = ' Higher-level managers include those in the organization above the immediate level of management responsible for the incident management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher-level managers typically includes:  status reviews of incident management activities  issues identified in process and plan reviews  risks associated with incident management activities  recommendations for improvement '
            
            db.save()

        return redirect('/immil3table')


def immil3formdelete(request, id):
    immil3form = immil3formdb.objects.get(pk=id)
    immil3form.delete()
    return redirect('/immil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = immil_four_form()
        else:
            immil4form = immil4formdb.objects.get(pk=id)
            form = immil_four_form(instance=immil4form)
        return render(request, 'crrs_app/Forms/MILForms/IncidentManagement/immil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = immil_four_form(request.POST)
        else:
            immil4form = immil4formdb.objects.get(pk=id)
            form = immil_four_form(request.POST, instance=immil4form)
        if form.is_valid():
            form.save()
            db = immil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in incident management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow, including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the incident management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned in the post-incident review  improvements based on risk identification and mitigation  recommended updates to the incident management plan '
            
            db.save()

        return redirect('/immil4table')

def immil4formdelete(request, id):
    immil4form = immil4formdb.objects.get(pk=id)
    immil4form.delete()
    return redirect('/immil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = immil_five_form()
        else:
            immil5form = immil5formdb.objects.get(pk=id)
            form = immil_five_form(instance=immil5form)
        return render(request, 'crrs_app/Forms/MILForms/IncidentManagement/immil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = immil_five_form(request.POST)
        else:
            immil5form = immil5formdb.objects.get(pk=id)
            form = immil_five_form(request.POST, instance=immil5form)
        if form.is_valid():
            form.save()
            db = immil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in incident management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow, including diagrams  inputs and expected outputs  performance measures for improvement'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the incident management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned in the post-incident review  improvements based on risk identification and mitigation  recommended updates to the incident management plan '
            
            db.save()

        return redirect('/immil5table')

def immil5formdelete(request, id):
    immil5form = immil5formdb.objects.get(pk=id)
    immil5form.delete()
    return redirect('/immil5table')


# RiskManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmmil_two_form()
        else:
            rmmil2form = rmmil2formdb.objects.get(pk=id)
            form = rmmil_two_form(instance=rmmil2form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmmil_two_form(request.POST)
        else:
            rmmil2form = rmmil2formdb.objects.get(pk=id)
            form = rmmil_two_form(request.POST, instance=rmmil2form)
        if form.is_valid():
            form.save()
            db = rmmil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines risk management within the organization and prescribes how risk management activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. The plan typically includes:  risk management activities (risk identification, risk analysis, and risk mitigation)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the risk management process and communicates those expectations to the organization. The policy should address:w  responsibility, authority, ownership, and the requirement to perform risk management activities  establishment of procedures, standards, and guidelines  requirements for periodically assessing the risk environment  measuring adherence to policy, when exceptions are granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the risk management process have the following responsibilities:  identifying risk  analyzing risk  developing and implementing risk mitigation plans  reviewing the effectiveness of the risk management process  managing the risk resulting from unresolved problems (gaps in processes, insufficient staffing or funding, etc.) Examples of stakeholders include:  critical service owners  management  owners and custodians of assets that underpin the service  external entities responsible for some part of the service  information technology staff  staff responsible for physical security'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of risk management activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  identifying risk sources and categories of risk  defining risk parameters (such as risk tolerance thresholds) and risk measurement criteria  assigning risk priorities based on risk analysis  assigning risk dispositions  developing risk mitigation plans '
           
            db.save()

        return redirect('/rmmil2table')

def rmmil2formdelete(request, id):
    rmmil2form = rmmil2formdb.objects.get(pk=id)
    rmmil2form.delete()
    return redirect('/rmmil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmmil_three_form()
        else:
            rmmil3form = rmmil3formdb.objects.get(pk=id)
            form = rmmil_three_form(instance=rmmil3form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmmil_three_form(request.POST)
        else:
            rmmil3form = rmmil3formdb.objects.get(pk=id)
            form = rmmil_three_form(request.POST, instance=rmmil3form)
        if form.is_valid():
            form.save()
            db = rmmil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of risk management activities.  Oversight provides visibility into risk management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing, or spot checks. Examples of Corrective Actions:  taking actions to repair defective work products (risk statements, risk disposition, risk mitigation plans, documentation)  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in risk management activities  escalating issues that require higher level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Examples of staff include personnel responsible for:  identifying operational risk sources and categories  assessing operational risks  business impact analysis  developing risk mitigation plans  monitoring and tracking risk to closure Examples of skills needed include:  proficiency with tools, techniques, and methods used to identify, analyze, mitigate, and monitor operational risk  knowledge necessary to develop, implement, and monitor risk mitigation plans  strong communication skills for conveying the operational risk and mitigation plans to higher level managers '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher level management support and sponsorship of risk management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned risk management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities, including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing risk management activities (risk management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the risk management process include:  poorly defined risk management processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools  lack of a documented plan, policy, standards, and guidelines  lack of stakeholder involvement  lack of management oversight '
            
            db.save()

        return redirect('/rmmil3table')

def rmmil3formdelete(request, id):
    rmmil3form = rmmil3formdb.objects.get(pk=id)
    rmmil3form.delete()
    return redirect('/rmmil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmmil_four_form()
        else:
            rmmil4form = rmmil4formdb.objects.get(pk=id)
            form = rmmil_four_form(instance=rmmil4form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmmil_four_form(request.POST)
        else:
            rmmil4form = rmmil4formdb.objects.get(pk=id)
            form = rmmil_four_form(request.POST, instance=rmmil4form)
        if form.is_valid():
            form.save()
            db = rmmil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the risk management process are needed to ensure that:  the performance of risk management process activities is being monitored and regularly reported  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  actions requiring management involvement are elevated in a timely manner Example metrics of the risk management process may include:  percentage of identified assets and services for which some form of risk assessment has been performed and documented  percentage of identified assets and services for which the impact or cost of compromise has been quantified  percentage of identified risks that have not been tracked to closure  percentage of identified risks that do not have a defined risk disposition '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Periodic (as defined by the organization) reviews for adherence to the risk management plan are needed to ensure that:  activities are performed as planned and adhere to process descriptions, standards, and procedures  deviations from the plan are identified and evaluated  problems in the plan for performing risk management activities are identified  non-compliance is addressed  needed process changes are identified when expected results or outputs are not met '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher-level managers include those in the organization above the immediate level of management responsible for the risk management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher level managers typically includes:  status reviews of risk management activities  issues identified in process and plan reviews  risks associated with risk management activities  recommendations for improvement '
           
            db.save()

        return redirect('/rmmil4table')

def rmmil4formdelete(request, id):
    rmmil4form = rmmil4formdb.objects.get(pk=id)
    rmmil4form.delete()
    return redirect('/rmmil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = rmmil_five_form()
        else:
            rmmil5form = rmmil5formdb.objects.get(pk=id)
            form = rmmil_five_form(instance=rmmil5form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = rmmil_five_form(request.POST)
        else:
            rmmil5form = rmmil5formdb.objects.get(pk=id)
            form = rmmil_five_form(request.POST, instance=rmmil5form)
        if form.is_valid():
            form.save()
            db = rmmil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in risk management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow, including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the risk management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned from both successfully and unsuccessfully mitigating identified risks  issues with the risk identification, analysis, prioritization, assessment, mitigation, and monitoring processes '
            
            db.save()

        return redirect('/rmmil5table')

def rmmil5formdelete(request, id):
    rmmil5form = rmmil5formdb.objects.get(pk=id)
    rmmil5form.delete()
    return redirect('/rmmil5table')


# ServiceContinuityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmmil_two_form()
        else:
            scmmil2form = scmmil2formdb.objects.get(pk=id)
            form = scmmil_two_form(instance=scmmil2form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmmil_two_form(request.POST)
        else:
            scmmil2form = scmmil2formdb.objects.get(pk=id)
            form = scmmil_two_form(request.POST, instance=scmmil2form)
        if form.is_valid():
            form.save()
            db = scmmil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines service continuity management within the organization and prescribes how service continuity management activities will be performed.  The plan may be a stand-alone document or may be comprised of multiple documents.  The plan for the service continuity process details how the organization will perform service continuity planning, including the development of service continuity plans.  The plan for the service continuity process should not be confused with a specific service continuity plan.  Service continuity plans are service-specific plans for sustaining services and associated assets. The plan typically includes:  service continuity management activities (testing, executing, reviewing both tested and executed plans, identifying improvements, etc.)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the service continuity management process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform service continuity management activities  establishment of procedures, standards, and guidelines  requirements for periodically assessing the service continuity management activities  communication of plans to stakeholders  responsibility for testing plans on a regular basis'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the service continuity management process have the following responsibilities: overseeing the service continuity management process developing service continuity plans coordinating service continuity activities participating in the test and execution of service continuity plans resolving issues with the service continuity management process ensuring that service continuity plans reflect all external dependencies reviewing and appraising the effectiveness of service continuity activities Examples of stakeholders include:  critical service owners  management  owners and custodians of assets that underpin the service  critical service staff  external entities responsible for some part of the service  information technology staff  staff responsible for physical security  regulatory and legal entities to which th'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of service continuity management activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  plan ownership  plan documentation  plan content  testing plans, including test objectives, reporting, and frequency  involvement of stakeholders, including from external dependencies  plan versioning, storage, archiving, and security  plan training  external entities  issue escalation and resolution procedures'
            
            db.save()

        return redirect('/scmmil2table')

def scmmil2formdelete(request, id):
    scmmil2form = scmmil2formdb.objects.get(pk=id)
    scmmil2form.delete()
    return redirect('/scmmil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmmil_three_form()
        else:
            scmmil3form = scmmil3formdb.objects.get(pk=id)
            form = scmmil_three_form(instance=scmmil3form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmmil_three_form(request.POST)
        else:
            scmmil3form = scmmil3formdb.objects.get(pk=id)
            form = scmmil_three_form(request.POST, instance=scmmil3form)
        if form.is_valid():
            form.save()
            db = scmmil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the service continuity management activities.  Oversight provides visibility into the service continuity management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing, or spot checks. Examples of corrective actions:  taking actions to repair defective work products or services  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in the service continuity management activities  escalating issues that require higher level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Examples of staff include personnel responsible for:  developing process standards and guidelines  developing service continuity plans  developing and conducting service continuity training  service continuity plan testing and validation  identifying internal and external dependencies Examples of skills needed include:  knowledge necessary to elicit resilience requirements to be reflected in service continuity plans  knowledge unique to each service that is required to develop service-specific continuity plans  knowledge necessary to plan and conduct service continuity testing  knowledge of service continuity tools, techniques, and methods '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher level management support and sponsorship of service continuity management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned service continuity management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing service continuity management activities (service continuity management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the service continuity management process include:  poorly defined service continuity management processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools  lack of a documented plan, policy, standards, and guidelines  lack of stakeholder involvement '
            
            db.save()

        return redirect('/scmmil3table')

def scmmil3formdelete(request, id):
    scmmil3form = scmmil3formdb.objects.get(pk=id)
    scmmil3form.delete()
    return redirect('/scmmil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmmil_four_form()
        else:
            scmmil4form = scmmil4formdb.objects.get(pk=id)
            form = scmmil_four_form(instance=scmmil4form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmmil_four_form(request.POST)
        else:
            scmmil4form = scmmil4formdb.objects.get(pk=id)
            form = scmmil_four_form(request.POST, instance=scmmil4form)
        if form.is_valid():
            form.save()
            db = scmmil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the service continuity management process are needed to ensure that:  service continuity performance issues are identified and remediated  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risks related to service continuity performance are identified and addressed  actions requiring management involvement are elevated in a timely manner  test plans are tested as required  test results meet objectives Example metrics of the service continuity management process may include:  percentage of service continuity plans completed, tested, executed, and yet to be developed  percentage of plans that meet objectives (e.g., RTOs and RPOs)  percentage of plans that require changes to meet objectives  percentage of plans that have not been reviewed post-test or post-execution  percentage of staff who have not been trained '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Periodic (as defined by the organization) reviews for adherence to the service continuity management plan are needed to ensure that:  Activities are performed as planned and adhere to process descriptions, standards, and procedures.  Deviations from the plan are identified and evaluated.  Problems in the plan for performing service continuity management activities are identified.  Non-compliance is addressed.  Needed process changes are identified when expected results or outputs are not met. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher-level managers include those in the organization above the immediate level of management responsible for the service continuity management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher-level managers typically includes:  reviews of status of service continuity management activities  issues identified in process and plan reviews  risks associated with service continuity management activities  recommendations for improvement '
            
            db.save()

        return redirect('/scmmil4table')

def scmmil4formdelete(request, id):
    scmmil4form = scmmil4formdb.objects.get(pk=id)
    scmmil4form.delete()
    return redirect('/scmmil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = scmmil_five_form()
        else:
            scmmil5form = scmmil5formdb.objects.get(pk=id)
            form = scmmil_five_form(instance=scmmil5form)
        return render(request, 'crrs_app/Forms/MILForms/RiskManagement/rmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = scmmil_five_form(request.POST)
        else:
            scmmil5form = scmmil5formdb.objects.get(pk=id)
            form = scmmil_five_form(request.POST, instance=scmmil5form)
        if form.is_valid():
            form.save()
            db = scmmil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in service continuity management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow, including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the service continuity management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  lessons learned from testing and executing service continuity plans  improvements based on risk identification and mitigation  lessons learned from conflicts arising from resource contention between service continuity plans'
            
            db.save()

        return redirect('/scmmil5table')

def scmmil5formdelete(request, id):
    scmmil5form = scmmil5formdb.objects.get(pk=id)
    scmmil5form.delete()
    return redirect('/scmmil5table')


# situationalawareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = samil_two_form()
        else:
            samil2form = samil2formdb.objects.get(pk=id)
            form = samil_two_form(instance=samil2form)
        return render(request, 'crrs_app/Forms/MILForms/SituationalAwareness/samil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = samil_two_form(request.POST)
        else:
            samil2form = samil2formdb.objects.get(pk=id)
            form = samil_two_form(request.POST, instance=samil2form)
        if form.is_valid():
            form.save()
            db = samil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines situational awareness within the organization and prescribes how situational awareness activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. The plan typically includes:  situational awareness activities (monitoring threat sources, threat communication, etc.)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders  measurement and reporting requirements  training requirements  management oversight '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the situational awareness process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform situational awareness activities  establishment of procedures, standards, and guidelines  approving threat communication methods and channels  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations'
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the situational awareness process have the following responsibilities:  identifying the threat monitoring and communication requirements  defining and managing situational awareness activities, including ensuring the effectiveness of those activities  overseeing the situational awareness process  receiving and responding to threat information Examples of stakeholders include:  critical service owners  management  situational awareness staff  owners and custodians of assets that underpin the service  critical service staff  service continuity staff  external entities responsible for some part of the service  information technology staff  staff responsible for'
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of situational awareness activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  identifying threat monitoring requirements  identifying threat communication requirements and protocols (e.g., who to call and when)  identifying threat communication methods and channels '
            
            db.save()

        return redirect('/samil2table')

def samil2formdelete(request, id):
    samil2form = samil2formdb.objects.get(pk=id)
    samil2form.delete()
    return redirect('/samil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = samil_three_form()
        else:
            samil3form = samil3formdb.objects.get(pk=id)
            form = samil_three_form(instance=samil3form)
        return render(request, 'crrs_app/Forms/MILForms/SituationalAwareness/samil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = samil_three_form(request.POST)
        else:
            samil3form = samil3formdb.objects.get(pk=id)
            form = samil_three_form(request.POST, instance=samil3form)
        if form.is_valid():
            form.save()
            db = samil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the situational awareness activities.  Oversight provides visibility into the situational awareness activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing, or spot checks. Examples of corrective actions:  taking actions to repair defective work products (monitoring procedures, communication procedures, sources of threat information, communication channels and methods) or services  ensuring that standards and guidelines are followed  ensuring training is conducted  adjusting resources (people, tools, etc.)  identifying improvements in the situational awareness activities  escalating issues that require higher level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Examples of staff include personnel responsible for:  identifying the threat monitoring and communications requirements  implementing processes, standards, and guidelines  executing threat monitoring and communication processes  addressing issues and problems, including developing and executing remediation plans Examples of needed skills include:  knowledge necessary to elicit and prioritize stakeholder requirements and interpret them to develop effective threat monitoring and communication requirements  knowledge necessary to establish and maintain the threat monitoring and communications infrastructure  knowledge necessary to interpret threat information and communicate it to stakeholders  proficiency with tools, techniques, and methods used to perform threat monitoring and communications '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher level management support and sponsorship of situational awareness activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned situational awareness activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing situational awareness activities (situational awareness process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the situational awareness process include:  poorly defined situational awareness processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools  lack of a documented plan, policy, standards, and guidelines  lack of stakeholder involvement  lack of management oversight '
            
            db.save()

        return redirect('/samil3table')

def samil3formdelete(request, id):
    samil3form = samil3formdb.objects.get(pk=id)
    samil3form.delete()
    return redirect('/samil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = samil_four_form()
        else:
            samil4form = samil4formdb.objects.get(pk=id)
            form = samil_four_form(instance=samil4form)
        return render(request, 'crrs_app/Forms/MILForms/SituationalAwareness/samil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = samil_four_form(request.POST)
        else:
            samil4form = samil4formdb.objects.get(pk=id)
            form = samil_four_form(request.POST, instance=samil4form)
        if form.is_valid():
            form.save()
            db = samil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the situational awareness process are needed to ensure that:  threat sources are current and continue to be valid  threat monitoring and communication requirements continue to be valid  the infrastructure continues to adequately support requirements  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risks related to situational awareness activities are identified and addressed  actions requiring management involvement are elevated in a timely manner Example metrics of the situational awareness process may include:  uptime or availability of monitoring and communications infrastructure  level of adherence to situational awareness process activities  percentage of work products that do not meet standards  percentage of stakeholders that do not receive communications  time elapsed between the collection of key threat information and its distribution to stakeholders  number of situational awareness requirements gaps  number of new and changed situational awareness requirements over time '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' This review is often done by an independent entity (either internal or external to the organization). Periodic (as defined by the organization) reviews for adherence to the situational awareness plan are needed to ensure that:  Activities are performed as planned and adhere to process descriptions, standards, and procedures.  Deviations from the plan are identified and evaluated.  Problems in the plan for performing situational awareness activities are identified.  Non-compliance is addressed.  Needed process changes are identified when expected results or outputs are not met. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher level managers include those in the organization above the immediate level of management responsible for the situational awareness process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher level managers typically includes:  status reviews of situational awareness activities  issues identified in process and plan reviews  risks associated with situational aware'
            
            db.save()

        return redirect('/samil4table')

def samil4formdelete(request, id):
    samil4form = samil4formdb.objects.get(pk=id)
    samil4form.delete()
    return redirect('/samil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = samil_five_form()
        else:
            samil5form = samil5formdb.objects.get(pk=id)
            form = samil_five_form(instance=samil5form)
        return render(request, 'crrs_app/Forms/MILForms/SituationalAwareness/samil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = samil_five_form(request.POST)
        else:
            samil5form = samil5formdb.objects.get(pk=id)
            form = samil_five_form(request.POST, instance=samil5form)
        if form.is_valid():
            form.save()
            db = samil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in situational awareness activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the situational awareness process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  direct feedback from stakeholders  lessons learned in post-event review of incidents and disruptions in continuity  lessons learned from periodic reviews of situational awareness activities that can be applied to improve the situational awareness process  risk evaluations '
            
            db.save()

        return redirect('/samil5table')

def samil5formdelete(request, id):
    samil5form = samil5formdb.objects.get(pk=id)
    samil5form.delete()
    return redirect('/samil5table')


# TrainingAwareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = tamil_two_form()
        else:
            tamil2form = tamil2formdb.objects.get(pk=id)
            form = tamil_two_form(instance=tamil2form)
        return render(request, 'crrs_app/Forms/MILForms/TrainingAwareness/tamil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = tamil_two_form(request.POST)
        else:
            tamil2form = tamil2formdb.objects.get(pk=id)
            form = tamil_two_form(request.POST, instance=tamil2form)
        if form.is_valid():
            form.save()
            db = tamil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines training activities within the organization and prescribes how training activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. The plan typically includes:  training activities (developing awareness and training needs, evaluating gaps, training materials, conducting training, assessing effectiveness, etc.)  standards and guidelines  roles, assignments of responsibility, resources, and funding  identification of stakeholders  measurement and reporting requirements  training requirements  management oversight '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the training process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform training activities  establishment of procedures, standards, and guidelines  requirements for periodically assessing training effectiveness  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the training process have the following responsibilities: defining and managing training requirements conducting and overseeing the delivery of training ensuring the effectiveness of trainingExamples of stakeholders include: critical service owners management training staff owners and custodians of assets that underpin the service critical service staff external entities responsible for some part of the service information technology staff staff responsible for physical security human resources internal and external auditors '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of training activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  identifying awareness and training needs  developing awareness and training plans  developing awareness and training attendance requirements  creating, delivering, and maintaining training material  creating, delivering, and maintaining training records  assessing the effectiveness of training and awareness programs '
            
            db.save()

        return redirect('/tamil2table')

def tamil2formdelete(request, id):
    tamil2form = tamil2formdb.objects.get(pk=id)
    tamil2form.delete()
    return redirect('/tamil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = tamil_three_form()
        else:
            tamil3form = tamil3formdb.objects.get(pk=id)
            form = tamil_three_form(instance=tamil3form)
        return render(request, 'crrs_app/Forms/MILForms/TrainingAwareness/tamil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = tamil_three_form(request.POST)
        else:
            tamil3form = tamil3formdb.objects.get(pk=id)
            form = tamil_three_form(request.POST, instance=tamil3form)
        if form.is_valid():
            form.save()
            db = tamil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the training activities.  Oversight provides visibility into the training activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing or spot checks. Examples of corrective actions:  taking actions to update training materials to ensure effectiveness  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in the training activities  escalating issues that require higher level management input for resolution '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Examples of staff include personnel responsible for:  designing, implementing, and assessing training  implementing training processes, standards, and guidelines  addressing issues and problems, including developing and executing remediation plans Examples of skills needed include:  curriculum and instructional design  course delivery  course and instructor evaluation  measuring the effectiveness of awareness and training materials '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher level management support and sponsorship of training activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned training activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing training activities (training process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the training process include:  poorly defined training processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools  lack of a documented plan, policy, standards, and guidelines  lack of stakeholder involvement  lack of management oversight '
            
            db.save()

        return redirect('/tamil3table')

def tamil3formdelete(request, id):
    tamil3form = tamil3formdb.objects.get(pk=id)
    tamil3form.delete()
    return redirect('/tamil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = tamil_four_form()
        else:
            tamil4form = tamil4formdb.objects.get(pk=id)
            form = tamil_four_form(instance=tamil4form)
        return render(request, 'crrs_app/Forms/MILForms/TrainingAwareness/tamil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = tamil_four_form(request.POST)
        else:
            tamil4form = tamil4formdb.objects.get(pk=id)
            form = tamil_four_form(request.POST, instance=tamil4form)
        if form.is_valid():
            form.save()
            db = tamil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the training process are needed to ensure that:  awareness and training needs have been identified and are being satisfied  training problem areas are identified and remediated  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risk related to training problem areas are identified and addressed  actions requiring management involvement are elevated in a timely manner Example metrics of the training process may include:  percentage of staff who have completed awareness training as required  percentage of staff who have completed technical training as required  percentage of favorable post-training evaluation ratings, including training effectiveness  percentage of passing scores on training examinations '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Periodic (as defined by the organization) reviews for adherence to the training plan are needed to ensure that:  Activities are performed as planned and adhere to process descriptions, standards, and procedures.  Deviations from the plan are identified and evaluated.  Problems in the plan for performing training activities are identified.  Non-compliance is addressed.  Needed process changes are identified when expected results or outputs are not met. '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Higher level managers include those in the organization above the immediate level of management responsible for the training process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher level managers typically includes:  status reviews of training activities  issues identified in process and plan reviews  risks associated with training activities  recommendations for improvement '
            
            db.save()

        return redirect('/tamil4table')

def tamil4formdelete(request, id):
    tamil4form = tamil4formdb.objects.get(pk=id)
    tamil4form.delete()
    return redirect('/tamil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = tamil_five_form()
        else:
            tamil5form = tamil5formdb.objects.get(pk=id)
            form = tamil_five_form(instance=tamil5form)
        return render(request, 'crrs_app/Forms/MILForms/TrainingAwareness/tamil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = tamil_five_form(request.POST)
        else:
            tamil5form = tamil5formdb.objects.get(pk=id)
            form = tamil_five_form(request.POST, instance=tamil5form)
        if form.is_valid():
            form.save()
            db = tamil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in training activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the training process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  results of training effectiveness surveys  course evaluations  training records  training requirements from a stakeholder group  lessons learned from training plan reviews  lessons learned in post-event reviews, including lack of staff preparedness '
            
            db.save()

        return redirect('/tamil5table')

def tamil5formdelete(request, id):
    tamil5form = tamil5formdb.objects.get(pk=id)
    tamil5form.delete()
    return redirect('/tamil5table')


# VulnerabilityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil2form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmmil_two_form()
        else:
            vmmil2form = vmmil2formdb.objects.get(pk=id)
            form = vmmil_two_form(instance=vmmil2form)
        return render(request, 'crrs_app/Forms/MILForms/VulnerabilityManagement/vmmil2form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmmil_two_form(request.POST)
        else:
            vmmil2form = vmmil2formdb.objects.get(pk=id)
            form = vmmil_two_form(request.POST, instance=vmmil2form)
        if form.is_valid():
            form.save()
            db = vmmil2formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' The plan defines vulnerability management within the organization and prescribes how vulnerability management activities will be performed.  The plan may be a stand-alone document, embedded in a more comprehensive document, or be distributed across multiple documents. The plan typically includes:  vulnerability management activities (source identification, vulnerability identification, prioritization, categorization, analysis, etc.)  standards and requirements  roles, assignments of responsibility, resources, and funding  identification of stakeholders  measurement and reporting requirements  training requirements  management oversight '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' A policy is a written communication from the organization’s senior management to employees.  It establishes the organizational expectations for planning and performing the vulnerability management process and communicates those expectations to the organization. The policy should address:  responsibility, authority, ownership, and the requirement to perform vulnerability management activities  establishment of procedures, standards, and guidelines  requirements for periodically assessing the vulnerability management activities  measuring adherence to policy, exceptions granted, and policy violations  compliance with legal, regulatory, contractual, and government obligations '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Stakeholders of the vulnerability management process have the following responsibilities:  overseeing the vulnerability management process  resolving issues with the vulnerability management process  establishing vulnerability prioritization guidelines  assessing collected vulnerability data  providing feedback to those responsible for providing vulnerability data  reviewing and appraising the effectiveness of vulnerability management activities Examples of stakeholders include:  critical service owners  management  owners of external entity relationships  vulnerability management program staff  owners and custodians of assets that underpin the service  critical service staff  external entities responsible for some part of the service  information technology staff  staff responsible for physical security  human resources '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' Standards establish expectations for performance.  Guidelines are issued by an organization to ensure the performance of vulnerability management activities meets standards and is predictable, measurable, and repeatable. Standards and guidelines typically address:  prioritization and categorization guidelines  analysis and disposition  reporting  tool selection and use  collection of vulnerability data '
            
            db.save()

        return redirect('/vmmil2table')

def vmmil2formdelete(request, id):
    vmmil2form = vmmil2formdb.objects.get(pk=id)
    vmmil2form.delete()
    return redirect('/vmmil2table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil3form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmmil_three_form()
        else:
            vmmil3form = vmmil3formdb.objects.get(pk=id)
            form = vmmil_three_form(instance=vmmil3form)
        return render(request, 'crrs_app/Forms/MILForms/VulnerabilityManagement/vmmil3form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmmil_three_form(request.POST)
        else:
            vmmil3form = vmmil3formdb.objects.get(pk=id)
            form = vmmil_three_form(request.POST, instance=vmmil3form)
        if form.is_valid():
            form.save()
            db = vmmil3formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' Management consists of the immediate level of managers that govern the day-to-day operation of the vulnerability management activities.  Oversight provides visibility into the vulnerability management activities so that issues can be identified and appropriate corrective actions can be taken when necessary.  Oversight activities could include regular meetings, written or oral status updates, auditing, or spot checks.Examples of corrective actions:  taking actions to repair defective work products or services  ensuring that standards and guidelines are followed  adjusting resources (people, tools, etc.)  identifying improvements in the vulnerability management activities  escalating issues that require higher-level management input for resolution'
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Qualified means that staff are appropriately skilled to perform vulnerability management activities. Examples of staff include personnel responsible for:  collecting, analyzing, and prioritizing vulnerability management requirements  developing vulnerability management analysis and resolution plans and programs  establishing an appropriate infrastructure for vulnerability data  the security and protection of vulnerability data.  manage external entities that have contractual obligations for vulnerability management analysis and resolution Examples of skills needed include:  knowledge of tools, techniques, and methods used to identify, analyze, remediate, monitor, and communicate vulnerabilities  knowledge to ensure confidentiality, integrity, and availability of vulnerability data  knowledge necessary to interpret vulnerability data and represent it to appropriate stakeholders '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = ' Funding is an indication of higher-level management support and sponsorship of vulnerability management activities.  Funding should be available to support the proper oversight, execution, and maintenance of these activities. Considerations for funding planned vulnerability management activities include:  defining funding needs  establishing a budget  resolving funding gaps  funding the process activities including staffing, tools, training, etc. '
            if request.POST['response_four'] == 'yes':
                db.feedback['response_four'] = 'Excellent'
            elif request.POST['response_four'] == 'no':
                db.feedback['response_four'] = ' The intent is to determine risks that prevent the organization from performing vulnerability management activities (vulnerability management process), not the risks to the organization if the activities are not performed. Risks to consider in relation to the vulnerability management process include:  poorly defined vulnerability management processes  inadequate staffing  inadequate funding  unqualified staff  lack of tools  lack of a documented plan, policy, standards, and guidelines  lack of stakeholder involvement  lack of management oversight '
            
            db.save()

        return redirect('/vmmil3table')

def vmmil3formdelete(request, id):
    vmmil3form = vmmil3formdb.objects.get(pk=id)
    vmmil3form.delete()
    return redirect('/vmmil3table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil4form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmmil_four_form()
        else:
            vmmil4form = vmmil4formdb.objects.get(pk=id)
            form = vmmil_four_form(instance=vmmil4form)
        return render(request, 'crrs_app/Forms/MILForms/VulnerabilityManagement/vmmil4form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmmil_four_form(request.POST)
        else:
            vmmil4form = vmmil4formdb.objects.get(pk=id)
            form = vmmil_four_form(request.POST, instance=vmmil4form)
        if form.is_valid():
            form.save()
            db = vmmil4formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = 'Periodic (as defined by the organization) reviews of the vulnerability management process are needed to ensure that:  vulnerability management performance issues are identified and remediated  the quality of particular work products meets established guidelines  problems in the process plan or in the execution of the process are identified  risks related to vulnerability management performance are identified and addressed  actions requiring management involvement are elevated in a timely manner  new vulnerabilities are identified and prioritized  current sources of vulnerability data are in use  vulnerability mitigation activities are effective Example metrics of the vulnerability management process may include:  number of reported vulnerabilities for which a vulnerability management strategy exists  number of vulnerabilities requiring a root-cause analysis  number of vulnerabilities referred to the risk management process  number of vulnerabilities where corrective action is still pending '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = 'Periodic (as defined by the organization) reviews for adherence to the vulnerability management plan are needed to ensure that:  activities are performed as planned and adhere to process descriptions, standards, and procedures  deviations from the plan are identified and evaluated  problems in the plan for performing vulnerability management activities are identified  non-compliance is addressed  needed process changes are identified when expected results or outputs are not met '
            if request.POST['response_three'] == 'yes':
                db.feedback['response_three'] = 'Excellent'
            elif request.POST['response_three'] == 'no':
                db.feedback['response_three'] = 'Question Intent: To determine if the performance of vulnerability management is communicated to higher-level managers to provide visibility and facilitate the resolution of issues.  Higher-level managers include those in the organization above the immediate level of management responsible for the vulnerability management process.  Communications are expected to be performed periodically (as defined by the organization) and may be event-driven when escalation is needed. Communication with higher-level managers typically includes:  status reviews of vulnerability management activities  issues identified in process and plan reviews  risks associated with vulnerability manage'
            
            db.save()

        return redirect('/vmmil4table')

def vmmil4formdelete(request, id):
    vmmil4form = vmmil4formdb.objects.get(pk=id)
    vmmil4form.delete()
    return redirect('/vmmil4table')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil5form(request, id=0):
    if request.method == "GET":
        if not id:
            form = vmmil_five_form()
        else:
            vmmil5form = vmmil5formdb.objects.get(pk=id)
            form = vmmil_five_form(instance=vmmil5form)
        return render(request, 'crrs_app/Forms/MILForms/VulnerabilityManagement/vmmil5form.html', {'form': form})
    if request.method == "POST":
        id = _extract_id(request)
        if not id:
            form = vmmil_five_form(request.POST)
        else:
            vmmil5form = vmmil5formdb.objects.get(pk=id)
            form = vmmil_five_form(request.POST, instance=vmmil5form)
        if form.is_valid():
            form.save()
            db = vmmil5formdb.objects.get(pk=form.instance.id)
            if request.POST['response_one'] == 'yes':
                db.feedback['response_one'] = 'Excellent'
            elif request.POST['response_one'] == 'no':
                db.feedback['response_one'] = ' A standard process should include guidelines for tailoring the process to meet the needs of an organizational unit.  A standard process provides a predictable level of consistency in vulnerability management activities across the organization. A standard definition may include:  process description  process activities and practices to be performed  process flow including diagrams  inputs and expected outputs  performance measures for improvement  procedures for process improvement '
            if request.POST['response_two'] == 'yes':
                db.feedback['response_two'] = 'Excellent'
            elif request.POST['response_two'] == 'no':
                db.feedback['response_two'] = ' Documenting lessons learned during the execution and review of the vulnerability management process facilitates the proposal of improvements to the process.  Sharing lessons learned enables organization-wide process improvements and organizationwide learning. Examples of improvement work products may include:  process metrics and measurements  reports on the effectiveness of controls in mitigating vulnerabilities  lessons learned from root-cause analysis  improvements based on risk identification and mitigation  changes in operating conditions, risk conditions, and the risk environment that impact vulnerability '
            
            db.save()

        return redirect('/vmmil5table')

def vmmil5formdelete(request, id):
    vmmil5form = vmmil5formdb.objects.get(pk=id)
    vmmil5form.delete()
    return redirect('/vmmil5table')


# TABLE REPORTS
# GoalTableReports
# AssetManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg1table(request):
    context = {'amg1table': amg1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/AssetManagement/amg1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg2table(request):
    context = {'amg2table': amg2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/AssetManagement/amg2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg3table(request):
    context = {'amg3table': amg3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/AssetManagement/amg3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg4table(request):
    context = {'amg4table': amg4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/AssetManagement/amg4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg5table(request):
    context = {'amg5table': amg5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/AssetManagement/amg5table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg6table(request):
    context = {'amg6table': amg6formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/AssetManagement/amg6table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def amg7table(request):
    context = {'amg7table': amg7formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/AssetManagement/amg7table.html', context)


# ConfigurationChangeManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmg1table(request):
    context = {'ccmg1table': ccmg1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ConfigurationChangeManagement/ccmg1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmg2table(request):
    context = {'ccmg2table': ccmg2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ConfigurationChangeManagement/ccmg2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmg3table(request):
    context = {'ccmg3table': ccmg3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ConfigurationChangeManagement/ccmg3table.html', context)


# controlsmanagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmg1table(request):
    context = {'cmg1table': cmg1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ControlsManagement/cmg1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmg2table(request):
    context = {'cmg2table': cmg2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ControlsManagement/cmg2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmg3table(request):
    context = {'cmg3table': cmg3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ControlsManagement/cmg3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmg4table(request):
    context = {'cmg4table': cmg4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ControlsManagement/cmg4table.html', context)


# ExternalDependenciesManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg1table(request):
    context = {'edmg1table': edmg1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ExternalDependenciesManagement/edmg1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg2table(request):
    context = {'edmg2table': edmg2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ExternalDependenciesManagement/edmg2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg3table(request):
    context = {'edmg3table': edmg3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ExternalDependenciesManagement/edmg3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg4table(request):
    context = {'edmg4table': edmg4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ExternalDependenciesManagement/edmg4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmg5table(request):
    context = {'edmg5table': edmg5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ExternalDependenciesManagement/edmg5table.html', context)


# IncidentManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img1table(request):
    context = {'img1table': img1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/IncidentManagement/img1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img2table(request):
    context = {'img2table': img2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/IncidentManagement/img2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img3table(request):
    context = {'img3table': img3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/IncidentManagement/img3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img4table(request):
    context = {'img4table': img4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/IncidentManagement/img4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def img5table(request):
    context = {'img5table': img5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/IncidentManagement/img5table.html', context)


# RiskManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg1table(request):
    context = {'rmg1table': rmg1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/RiskManagement/rmg1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg2table(request):
    context = {'rmg2table': rmg2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/RiskManagement/rmg2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg3table(request):
    context = {'rmg3table': rmg3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/RiskManagement/rmg3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg4table(request):
    context = {'rmg4table': rmg4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/RiskManagement/rmg4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmg5table(request):
    context = {'rmg5table': rmg5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/RiskManagement/rmg5table.html', context)


# ServiceContinuityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg1table(request):
    context = {'scmg1table': scmg1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ServiceContinuityManagement/scmg1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg2table(request):
    context = {'scmg2table': scmg2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ServiceContinuityManagement/scmg2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg3table(request):
    context = {'scmg3table': scmg3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ServiceContinuityManagement/scmg3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmg4table(request):
    context = {'scmg4table': scmg4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/ServiceContinuityManagement/scmg4table.html', context)


# situationalawareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def sag1table(request):
    context = {'sag1table': sag1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/SituationalAwareness/sag1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def sag2table(request):
    context = {'sag2table': sag2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/SituationalAwareness/sag2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def sag3table(request):
    context = {'sag3table': sag3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/SituationalAwareness/sag3table.html', context)


# TrainingAwareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tag1table(request):
    context = {'tag1table': tag1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/TrainingAwareness/tag1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tag2table(request):
    context = {'tag2table': tag2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/TrainingAwareness/tag2table.html', context)


# VulnerabilityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmg1table(request):
    context = {'vmg1table': vmg1formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/VulnerabilityManagement/vmg1table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmg2table(request):
    context = {'vmg2table': vmg2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/VulnerabilityManagement/vmg2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmg3table(request):
    context = {'vmg3table': vmg3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/VulnerabilityManagement/vmg3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmg4table(request):
    context = {'vmg4table': vmg4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/GoalTableReports/VulnerabilityManagement/vmg4table.html', context)


# MILTableReports
# AssetManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil2table(request):
    context = {'ammil2table': ammil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/AssetManagement/ammil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil3table(request):
    context = {'ammil3table': ammil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/AssetManagement/ammil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil4table(request):
    context = {'ammil4table': ammil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/AssetManagement/ammil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ame'])
def ammil5table(request):
    context = {'ammil5table': ammil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/AssetManagement/ammil5table.html', context)


# ConfigurationChangeManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil2table(request):
    context = {'ccmmil2table': ccmmil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ConfigurationChangeManagement/ccmmil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil3table(request):
    context = {'ccmmil3table': ccmmil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ConfigurationChangeManagement/ccmmil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil4table(request):
    context = {'ccmmil4table': ccmmil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ConfigurationChangeManagement/ccmmil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ccme'])
def ccmmil5table(request):
    context = {'ccmmil5table': ccmmil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ConfigurationChangeManagement/ccmmil5table.html', context)


# controlsmanagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil2table(request):
    context = {'cmmil2table': cmmil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ControlsManagement/cmmil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil3table(request):
    context = {'cmmil3table': cmmil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ControlsManagement/cmmil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil4table(request):
    context = {'cmmil4table': cmmil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ControlsManagement/cmmil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','cme'])
def cmmil5table(request):
    context = {'cmmil5table': cmmil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ControlsManagement/cmmil5table.html', context)


# ExternalDependenciesManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil2table(request):
    context = {'edmmil2table': edmmil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ExternalDependenciesManagement/edmmil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil3table(request):
    context = {'edmmil3table': edmmil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ExternalDependenciesManagement/edmmil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil4table(request):
    context = {'edmmil4table': edmmil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ExternalDependenciesManagement/edmmil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','edme'])
def edmmil5table(request):
    context = {'edmmil5table': edmmil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ExternalDependenciesManagement/edmmil5table.html', context)


# IncidentManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil2table(request):
    context = {'immil2table': immil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/IncidentManagement/immil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil3table(request):
    context = {'immil3table': immil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/IncidentManagement/immil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil4table(request):
    context = {'immil4table': immil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/IncidentManagement/immil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','ime'])
def immil5table(request):
    context = {'immil5table': immil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/IncidentManagement/immil5table.html', context)


# RiskManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil2table(request):
    context = {'rmmil2table': rmmil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/RiskManagement/rmmil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil3table(request):
    context = {'rmmil3table': rmmil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/RiskManagement/rmmil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil4table(request):
    context = {'rmmil4table': rmmil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/RiskManagement/rmmil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','rme'])
def rmmil5table(request):
    context = {'rmmil5table': rmmil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/RiskManagement/rmmil5table.html', context)


# ServiceContinuityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil2table(request):
    context = {'scmmil2table': scmmil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ServiceContinuityManagement/scmmil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil3table(request):
    context = {'scmmil3table': scmmil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ServiceContinuityManagement/scmmil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil4table(request):
    context = {'scmmil4table': scmmil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ServiceContinuityManagement/scmmil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','scme'])
def scmmil5table(request):
    context = {'scmmil5table': scmmil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/ServiceContinuityManagement/scmmil5table.html', context)


# situationalawareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil2table(request):
    context = {'samil2table': samil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/SituationalAwareness/samil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil3table(request):
    context = {'samil3table': samil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/SituationalAwareness/samil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil4table(request):
    context = {'samil4table': samil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/SituationalAwareness/samil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','sae'])
def samil5table(request):
    context = {'samil5table': samil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/SituationalAwareness/samil5table.html', context)


# TrainingAwareness

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil2table(request):
    context = {'tamil2table': tamil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/TrainingAwareness/tamil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil3table(request):
    context = {'tamil3table': tamil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/TrainingAwareness/tamil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil4table(request):
    context = {'tamil4table': tamil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/TrainingAwareness/tamil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','tae'])
def tamil5table(request):
    context = {'tamil5table': tamil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/TrainingAwareness/tamil5table.html', context)


# VulnerabilityManagement

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil2table(request):
    context = {'vmmil2table': vmmil2formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/VulnerabilityManagement/vmmil2table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil3table(request):
    context = {'vmmil3table': vmmil3formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/VulnerabilityManagement/vmmil3table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil4table(request):
    context = {'vmmil4table': vmmil4formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/VulnerabilityManagement/vmmil4table.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin','cse','vme'])
def vmmil5table(request):
    context = {'vmmil5table': vmmil5formdb.objects.all()}
    return render(request, 'crrs_app/TableReports/MILTableReports/VulnerabilityManagement/vmmil5table.html', context)
