from django.urls import path

from . import views

#Crate your views here

urlpatterns = [

    

    #BASE
    path('base', views.base, name='base'),


    #HOME
    #Dashboard
    #path('', views.crrshome, name='home'),

    #CHARTS
    #GoalChart
    path('goalssecuritylevels/', views.goalssecuritylevels, name='goalssecuritylevels'),

    #MILChart
    path('milsecuritylevels/', views.milsecuritylevels, name='milsecuritylevels'),

    #CONNECTOR PAGES
    #AssetManagement
    path('assetmanagementgoalform/', views.assetmanagementgoalform, name='assetmanagementgoalform'),
    path('assetmanagementgoalssolution/', views.assetmanagementgoalssolution, name='assetmanagementgoalssolution'),
    path('assetmanagementgoalstable/', views.assetmanagementgoalstable, name='assetmanagementgoalstable'),
    path('assetmanagementmilform/', views.assetmanagementmilform, name='assetmanagementmilform'),
    path('assetmanagementmilsolution/', views.assetmanagementmilsolution, name='assetmanagementmilsolution'),
    path('assetmanagementmiltable/', views.assetmanagementmiltable, name='assetmanagementmiltable'),

    #ConfigurationChangeManagement
    path('configurationchangemanagementgoalform/', views.configurationchangemanagementgoalform, name='configurationchangemanagementgoalform'),
    path('configurationchangemanagementgoalssolution/', views.configurationchangemanagementgoalssolution, name='configurationchangemanagementgoalssolution'),
    path('configurationchangemanagementgoalstable/', views.configurationchangemanagementgoalstable, name='configurationchangemanagementgoalstable'),
    path('configurationchangemanagementmilform/', views.configurationchangemanagementmilform, name='configurationchangemanagementmilform'),
    path('configurationchangemanagementmilsolution/', views.configurationchangemanagementmilsolution, name='configurationchangemanagementmilsolution'),
    path('configurationchangemanagementmiltable/', views.configurationchangemanagementmiltable, name='configurationchangemanagementmiltable'),

    #controlsmanagement
    path('controlsmanagementgoalform/', views.controlsmanagementgoalform, name='controlsmanagementgoalform'),
    path('controlsmanagementgoalssolution/', views.controlsmanagementgoalssolution, name='controlsmanagementgoalssolution'),
    path('controlsmanagementgoalstable/', views.controlsmanagementgoalstable, name='controlsmanagementgoalstable'),
    path('controlsmanagementmilform/', views.controlsmanagementmilform, name='controlsmanagementmilform'),
    path('controlsmanagementmilsolution/', views.controlsmanagementmilsolution, name='controlsmanagementmilsolution'),
    path('controlsmanagementmiltable/', views.controlsmanagementmiltable, name='controlsmanagementmiltable'),
    #ExternalDependenciesManagement
    path('externaldependenciesmanagementgoalform/', views.externaldependenciesmanagementgoalform, name='externaldependenciesmanagementgoalform'),
    path('externaldependenciesmanagementgoalssolution/', views.externaldependenciesmanagementgoalssolution, name='externaldependenciesmanagementgoalssolution'),
    path('externaldependenciesmanagementgoalstable/', views.externaldependenciesmanagementgoalstable, name='externaldependenciesmanagementgoalstable'),
    path('externaldependenciesmanagementmilform/', views.externaldependenciesmanagementmilform, name='externaldependenciesmanagementmilform'),
    path('externaldependenciesmanagementmilsolution/', views.externaldependenciesmanagementmilsolution, name='externaldependenciesmanagementmilsolution'),
    path('externaldependenciesmanagementmiltable/', views.externaldependenciesmanagementmiltable, name='externaldependenciesmanagementmiltable'),
    #IncidentManagement
    path('incidentmanagementgoalform/', views.incidentmanagementgoalform, name='incidentmanagementgoalform'),
    path('incidentmanagementgoalssolution/', views.incidentmanagementgoalssolution, name='incidentmanagementgoalssolution'),
    path('incidentmanagementgoalstable/', views.incidentmanagementgoalstable, name='incidentmanagementgoalstable'),
    path('incidentmanagementmilform/', views.incidentmanagementmilform, name='incidentmanagementmilform'),
    path('incidentmanagementmilsolution/', views.incidentmanagementmilsolution, name='incidentmanagementmilsolution'),
    path('incidentmanagementmiltable/', views.incidentmanagementmiltable, name='incidentmanagementmiltable'),
    #RiskManagement
    path('riskmanagementgoalform/', views.riskmanagementgoalform, name='riskmanagementgoalform'),
    path('riskmanagementgoalssolution/', views.riskmanagementgoalssolution, name='riskmanagementgoalssolution'),
    path('riskmanagementgoalstable/', views.riskmanagementgoalstable, name='riskmanagementgoalstable'),
    path('riskmanagementmilform/', views.riskmanagementmilform, name='riskmanagementmilform'),
    path('riskmanagementmilsolution/', views.riskmanagementmilsolution, name='riskmanagementmilsolution'),
    path('riskmanagementmiltable/', views.riskmanagementmiltable, name='riskmanagementmiltable'),
    #ServiceContinuityManagement
    path('servicecontinuitymanagementgoalform/', views.servicecontinuitymanagementgoalform, name='servicecontinuitymanagementgoalform'),
    path('servicecontinuitymanagementgoalssolution/', views.servicecontinuitymanagementgoalssolution, name='servicecontinuitymanagementgoalssolution'),
    path('servicecontinuitymanagementgoalstable/', views.servicecontinuitymanagementgoalstable, name='servicecontinuitymanagementgoalstable'),
    path('servicecontinuitymanagementmilform/', views.servicecontinuitymanagementmilform, name='servicecontinuitymanagementmilform'),
    path('servicecontinuitymanagementmilsolution/', views.servicecontinuitymanagementmilsolution, name='servicecontinuitymanagementmilsolution'),
    path('servicecontinuitymanagementmiltable/', views.servicecontinuitymanagementmiltable, name='servicecontinuitymanagementmiltable'),
    #SituationalAwareness
    path('situationalawarenessgoalform/', views.situationalawarenessgoalform, name='situationalawarenessgoalform'),
    path('situationalawarenessgoalssolution/', views.situationalawarenessgoalssolution, name='situationalawarenessgoalssolution'),
    path('situationalawarenessgoalstable/', views.situationalawarenessgoalstable, name='situationalawarenessgoalstable'),
    path('situationalawarenessmilform/', views.situationalawarenessmilform, name='situationalawarenessmilform'),
    path('situationalawarenessmilsolution/', views.situationalawarenessmilsolution, name='situationalawarenessmilsolution'),
    path('situationalawarenessmiltable/', views.situationalawarenessmiltable, name='situationalawarenessmiltable'),
    #TrainingAwareness
    path('trainingawarenessgoalform/', views.trainingawarenessgoalform, name='trainingawarenessgoalform'),
    path('trainingawarenessgoalssolution/', views.trainingawarenessgoalssolution, name='trainingawarenessgoalssolution'),
    path('trainingawarenessgoalstable/', views.trainingawarenessgoalstable, name='trainingawarenessgoalstable'),
    path('trainingawarenessmilform/', views.trainingawarenessmilform, name='trainingawarenessmilform'),
    path('trainingawarenessmilsolution/', views.trainingawarenessmilsolution, name='trainingawarenessmilsolution'),
    path('trainingawarenessmiltable/', views.trainingawarenessmiltable, name='trainingawarenessmiltable'),
    #VulnerabilityManagement
    path('vulnerabilitymanagementgoalform/', views.vulnerabilitymanagementgoalform, name='vulnerabilitymanagementgoalform'),
    path('vulnerabilitymanagementgoalssolution/', views.vulnerabilitymanagementgoalssolution, name='vulnerabilitymanagementgoalssolution'),
    path('vulnerabilitymanagementgoalstable/', views.vulnerabilitymanagementgoalstable, name='vulnerabilitymanagementgoalstable'),
    path('vulnerabilitymanagementmilform/', views.vulnerabilitymanagementmilform, name='vulnerabilitymanagementmilform'),
    path('vulnerabilitymanagementmilsolution/', views.vulnerabilitymanagementmilsolution, name='vulnerabilitymanagementmilsolution'),
    path('vulnerabilitymanagementmiltable/', views.vulnerabilitymanagementmiltable, name='vulnerabilitymanagementmiltable'),
    
    #WebDomains
    path('CrrsReports/', views.CrrsReports, name='CrrsReports'),
    path('CrrsFeedback/', views.CrrsFeedback, name='CrrsFeedback'),
    path('domaingoalssolutions/', views.domaingoalssolutions, name='domaingoalssolutions'),
    path('domainmilsolutions/', views.domainmilsolutions, name='domainmilsolutions'),
    path('domains/', views.domains, name='domains'),

    #WebGoals
    path('goalsforms/', views.goalsforms, name='goalsforms'),
    path('goalstables/', views.goalstables, name='goalstables'),

    #WebMIL
    path('milforms/', views.milforms, name='milforms'),
    path('miltables/', views.miltables, name='miltables'),

    #WebCyberSecurity
    path('cseform/', views.cseform, name='cseform'),
    path('cybersecuritylevels/', views.cybersecuritylevels, name='cybersecuritylevels'),

    #FEEDBACK REPORTS
    #GoalFeedbackReports
    #AssetManagement
    path('amg1solution/', views.amg1solution, name='amg1solution'),
    path('amg2solution/', views.amg2solution, name='amg2solution'),
    path('amg3solution/', views.amg3solution, name='amg3solution'),
    path('amg4solution/', views.amg4solution, name='amg4solution'),
    path('amg5solution/', views.amg5solution, name='amg5solution'),
    path('amg6solution/', views.amg6solution, name='amg6solution'),
    path('amg7solution/', views.amg7solution, name='amg7solution'),

    #ConfigurationChangeManagement
    path('ccmg1solution/', views.ccmg1solution, name='ccmg1solution'),
    path('ccmg2solution/', views.ccmg2solution, name='ccmg2solution'),
    path('ccmg3solution/', views.ccmg3solution, name='ccmg3solution'),

    #controlsmanagement
    path('cmg1solution/', views.cmg1solution, name='cmg1solution'),
    path('cmg2solution/', views.cmg2solution, name='cmg2solution'),
    path('cmg3solution/', views.cmg3solution, name='cmg3solution'),
    path('cmg4solution/', views.cmg4solution, name='cmg4solution'),

    #ExternalDependenciesManagement
    path('edmg1solution/', views.edmg1solution, name='edmg1solution'),
    path('edmg2solution/', views.edmg2solution, name='edmg2solution'),
    path('edmg3solution/', views.edmg3solution, name='edmg3solution'),
    path('edmg4solution/', views.edmg4solution, name='edmg4solution'),
    path('edmg5solution/', views.edmg5solution, name='edmg5solution'),

    #IncidentManagement
    path('img1solution/', views.img1solution, name='img1solution'),
    path('img2solution/', views.img2solution, name='img2solution'),
    path('img3solution/', views.img3solution, name='img3solution'),
    path('img4solution/', views.img4solution, name='img4solution'),
    path('img5solution/', views.img5solution, name='img5solution'),

    #RiskManagement
    path('rmg1solution/', views.rmg1solution, name='rmg1solution'),
    path('rmg2solution/', views.rmg2solution, name='rmg2solution'),
    path('rmg3solution/', views.rmg3solution, name='rmg3solution'),
    path('rmg4solution/', views.rmg4solution, name='rmg4solution'),
    path('rmg5solution/', views.rmg5solution, name='rmg5solution'),

    #ServiceContinuityManagement
    path('scmg1solution/', views.scmg1solution, name='scmg1solution'),
    path('scmg2solution/', views.scmg2solution, name='scmg2solution'),
    path('scmg3solution/', views.scmg3solution, name='scmg3solution'),
    path('scmg4solution/', views.scmg4solution, name='scmg4solution'),

    #situationalawareness
    path('sag1solution/', views.sag1solution, name='sag1solution'),
    path('sag2solution/', views.sag2solution, name='sag2solution'),
    path('sag3solution/', views.sag3solution, name='sag3solution'),

    #TrainingAwareness
    path('tag1solution/', views.tag1solution, name='tag1solution'),
    path('tag2solution/', views.tag2solution, name='tag2solution'),

    #VulnerabilityManagement
    path('vmg1solution/', views.vmg1solution, name='vmg1solution'),
    path('vmg2solution/', views.vmg2solution, name='vmg2solution'),
    path('vmg3solution/', views.vmg3solution, name='vmg3solution'),
    path('vmg4solution/', views.vmg4solution, name='vmg4solution'),
    
    #MILFeedbackReports
    #AssetManagement
    path('ammil2solution/', views.ammil2solution, name='ammil2solution'),
    path('ammil3solution/', views.ammil3solution, name='ammil3solution'),
    path('ammil4solution/', views.ammil4solution, name='ammil4solution'),
    path('ammil5solution/', views.ammil5solution, name='ammil5solution'),

    #ConfigurationChangeManagement
    path('ccmmil2solution/', views.ccmmil2solution, name='ccmmil2solution'),
    path('ccmmil3solution/', views.ccmmil3solution, name='ccmmil3solution'),
    path('ccmmil4solution/', views.ccmmil4solution, name='ccmmil4solution'),
    path('ccmmil5solution/', views.ccmmil5solution, name='ccmmil5solution'),

    #controlsmanagement
    path('cmmil2solution/', views.cmmil2solution, name='cmmil2solution'),
    path('cmmil3solution/', views.cmmil3solution, name='cmmil3solution'),
    path('cmmil4solution/', views.cmmil4solution, name='cmmil4solution'),
    path('cmmil5solution/', views.cmmil5solution, name='cmmil5solution'),

    #ExternalDependenciesManagement
    path('edmmil2solution/', views.edmmil2solution, name='edmmil2solution'),
    path('edmmil3solution/', views.edmmil3solution, name='edmmil3solution'),
    path('edmmil4solution/', views.edmmil4solution, name='edmmil4solution'),
    path('edmmil5solution/', views.edmmil5solution, name='edmmil5solution'),

    #IncidentManagement
    path('immil2solution/', views.immil2solution, name='immil2solution'),
    path('immil3solution/', views.immil3solution, name='immil3solution'),
    path('immil4solution/', views.immil4solution, name='immil4solution'),
    path('immil5solution/', views.immil5solution, name='immil5solution'),

    #RiskManagement
    path('rmmil2solution/', views.rmmil2solution, name='rmmil2solution'),
    path('rmmil3solution/', views.rmmil3solution, name='rmmil3solution'),
    path('rmmil4solution/', views.rmmil4solution, name='rmmil4solution'),
    path('rmmil5solution/', views.rmmil5solution, name='rmmil5solution'),

    #ServiceContinuityManagement
    path('scmmil2solution/', views.scmmil2solution, name='scmmil2solution'),
    path('scmmil3solution/', views.scmmil3solution, name='scmmil3solution'),
    path('scmmil4solution/', views.scmmil4solution, name='scmmil4solution'),
    path('scmmil5solution/', views.scmmil5solution, name='scmmil5solution'),

    #situationalawareness
    path('samil2solution/', views.samil2solution, name='samil2solution'),
    path('samil3solution/', views.samil3solution, name='samil3solution'),
    path('samil4solution/', views.samil4solution, name='samil4solution'),
    path('samil5solution/', views.samil5solution, name='samil5solution'),

    #TrainingAwareness
    path('tamil2solution/', views.tamil2solution, name='tamil2solution'),
    path('tamil3solution/', views.tamil3solution, name='tamil3solution'),
    path('tamil4solution/', views.tamil4solution, name='tamil4solution'),
    path('tamil5solution/', views.tamil5solution, name='tamil5solution'),

    #VulnerabilityManagement
    path('vmmil2solution/', views.vmmil2solution, name='vmmil2solution'),
    path('vmmil3solution/', views.vmmil3solution, name='vmmil3solution'),
    path('vmmil4solution/', views.vmmil4solution, name='vmmil4solution'),
    path('vmmil5solution/', views.vmmil5solution, name='vmmil5solution'),
    
    #FORMS
    #GoalForms
    #AssetManagement
    path('amg1form/', views.amg1form, name='amg1form'),
    path('amg1form/<int:id>/', views.amg1form, name='amg1form_update'),
    path('delete/<int:id>/', views.amg1formdelete, name='amg1form delete'),
    path('amg2form/', views.amg2form, name='amg2form'),
    path('amg2form/<int:id>/', views.amg2form, name='amg2form_update'),
    path('delete/<int:id>/', views.amg2formdelete, name='amg2form delete'),
    path('amg3form/', views.amg3form, name='amg3form'),
    path('amg3form/<int:id>/', views.amg3form, name='amg3form_update'),
    path('delete/<int:id>/', views.amg3formdelete, name='amg3form delete'),
    path('amg4form/', views.amg4form, name='amg4form'),
    path('amg4form/<int:id>/', views.amg4form, name='amg4form_update'),
    path('delete/<int:id>/', views.amg4formdelete, name='amg4form delete'),
    path('amg5form/', views.amg5form, name='amg5form'),
    path('amg5form/<int:id>/', views.amg5form, name='amg5form_update'),
    path('delete/<int:id>/', views.amg5formdelete, name='amg5form delete'),
    path('amg6form/', views.amg6form, name='amg6form'),
    path('amg6form/<int:id>/', views.amg6form, name='amg6form_update'),
    path('delete/<int:id>/', views.amg6formdelete, name='amg6form delete'),
    path('amg7form/', views.amg7form, name='amg7form'),
    path('amg7form/<int:id>/', views.amg7form, name='amg7form_update'),
    path('delete/<int:id>/', views.amg7formdelete, name='amg7form delete'),

    #ConfigurationChangeManagement
    path('ccmg1form/', views.ccmg1form, name='ccmg1form'),
    path('ccmg1form/<int:id>/', views.ccmg1form, name='ccmg1form_update'),
    path('delete/<int:id>/', views.ccmg1formdelete, name='ccmg1form delete'),
    path('ccmg2form/', views.ccmg2form, name='ccmg2form'),
    path('ccmg2form/<int:id>/', views.ccmg2form, name='ccmg2form_update'),
    path('delete/<int:id>/', views.ccmg2formdelete, name='ccmg2form delete'),
    path('ccmg3form/', views.ccmg3form, name='ccmg3form'),
    path('ccmg3form/<int:id>/', views.ccmg3form, name='ccmg3form_update'),
    path('delete/<int:id>/', views.ccmg3formdelete, name='ccmg3form delete'),

    #controlsmanagement
    path('cmg1form/', views.cmg1form, name='cmg1form'),
    path('cmg1form/<int:id>/', views.cmg1form, name='cmg1form_update'),
    path('delete/<int:id>/', views.cmg1formdelete, name='cmg1form delete'),
    path('cmg2form/', views.cmg2form, name='cmg2form'),
    path('cmg2form/<int:id>/', views.cmg2form, name='cmg2form_update'),
    path('delete/<int:id>/', views.cmg2formdelete, name='cmg2form delete'),
    path('cmg3form/', views.cmg3form, name='cmg3form'),
    path('cmg3form/<int:id>/', views.cmg3form, name='cmg3form_update'),
    path('delete/<int:id>/', views.cmg3formdelete, name='cmg3form delete'),
    path('cmg4form/', views.cmg4form, name='cmg4form'),
    path('cmg4form/<int:id>/', views.cmg4form, name='cmg4form_update'),
    path('delete/<int:id>/', views.cmg4formdelete, name='cmg4form delete'),
    #ExternalDependenciesManagement
    path('edmg1form/', views.edmg1form, name='edmg1form'),
    path('edmg1form/<int:id>/', views.edmg1form, name='edmg1form_update'),
    path('delete/<int:id>/', views.edmg1formdelete, name='edmg1form delete'),
    path('edmg2form/', views.edmg2form, name='edmg2form'),
    path('edmg2form/<int:id>/', views.edmg2form, name='edmg2form_update'),
    path('delete/<int:id>/', views.edmg2formdelete, name='edmg2form delete'),
    path('edmg3form/', views.edmg3form, name='edmg3form'),
    path('edmg3form/<int:id>/', views.edmg3form, name='edmg3form_update'),
    path('delete/<int:id>/', views.edmg3formdelete, name='edmg3form delete'),
    path('edmg4form/', views.edmg4form, name='edmg4form'),
    path('edmg4form/<int:id>/', views.edmg4form, name='edmg4form_update'),
    path('delete/<int:id>/', views.edmg4formdelete, name='edmg4form delete'),
    path('edmg5form/', views.edmg5form, name='edmg5form'),
    path('edmg5form/<int:id>/', views.edmg5form, name='edmg5form_update'),
    path('delete/<int:id>/', views.edmg5formdelete, name='edmg5form delete'),

    #IncidentManagement
    path('img1form/', views.img1form, name='img1form'),
    path('img1form/<int:id>/', views.img1form, name='img1form_update'),
    path('delete/<int:id>/', views.img1formdelete, name='img1form delete'),
    path('img2form/', views.img2form, name='img2form'),
    path('img2form/<int:id>/', views.img2form, name='img2form_update'),
    path('delete/<int:id>/', views.img2formdelete, name='img2form delete'),
    path('img3form/', views.img3form, name='img3form'),
    path('img3form/<int:id>/', views.img3form, name='img3form_update'),
    path('delete/<int:id>/', views.img3formdelete, name='img3form delete'),
    path('img4form/', views.img4form, name='img4form'),
    path('img4form/<int:id>/', views.img4form, name='img4form_update'),
    path('delete/<int:id>/', views.img4formdelete, name='img4form delete'),
    path('img5form/', views.img5form, name='img5form'),
    path('img5form/<int:id>/', views.img5form, name='img5form_update'),
    path('delete/<int:id>/', views.img5formdelete, name='img5form delete'),

    #RiskManagement
    path('rmg1form/', views.rmg1form, name='rmg1form'),
    path('rmg1form/<int:id>/', views.rmg1form, name='rmg1form_update'),
    path('delete/<int:id>/', views.rmg1formdelete, name='rmg1form delete'),
    path('rmg2form/', views.rmg2form, name='rmg2form'),
    path('rmg2form/<int:id>/', views.rmg2form, name='rmg2form_update'),
    path('delete/<int:id>/', views.rmg2formdelete, name='rmg2form delete'),
    path('rmg3form/', views.rmg3form, name='rmg3form'),
    path('rmg3form/<int:id>/', views.rmg3form, name='rmg3form_update'),
    path('delete/<int:id>/', views.rmg3formdelete, name='rmg3form delete'),
    path('rmg4form/', views.rmg4form, name='rmg4form'),
    path('rmg4form/<int:id>/', views.rmg4form, name='rmg4form_update'),
    path('delete/<int:id>/', views.rmg4formdelete, name='rmg4form delete'),
    path('rmg5form/', views.rmg5form, name='rmg5form'),
    path('rmg5form/<int:id>/', views.rmg5form, name='rmg5form_update'),
    path('delete/<int:id>/', views.rmg5formdelete, name='rmg5form delete'),

    #ServiceContinuityManagement
    path('scmg1form/', views.scmg1form, name='scmg1form'),
    path('scmg1form/<int:id>/', views.scmg1form, name='scmg1form_update'),
    path('delete/<int:id>/', views.scmg1formdelete, name='scmg1form delete'),
    path('scmg2form/', views.scmg2form, name='scmg2form'),
    path('scmg2form/<int:id>/', views.scmg2form, name='scmg2form_update'),
    path('delete/<int:id>/', views.scmg2formdelete, name='scmg2form delete'),
    path('scmg3form/', views.scmg3form, name='scmg3form'),
    path('scmg3form/<int:id>/', views.scmg3form, name='scmg3form_update'),
    path('delete/<int:id>/', views.scmg3formdelete, name='scmg3form delete'),
    path('scmg4form/', views.scmg4form, name='scmg4form'),
    path('scmg4form/<int:id>/', views.scmg4form, name='scmg4form_update'),
    path('delete/<int:id>/', views.scmg4formdelete, name='scmg4form delete'),

    #situationalawareness
    path('sag1form/', views.sag1form, name='sag1form'),
    path('sag1form/<int:id>/', views.sag1form, name='sag1form_update'),
    path('delete/<int:id>/', views.sag1formdelete, name='sag1form delete'),
    path('sag2form/', views.sag2form, name='sag2form'),
    path('sag2form/<int:id>/', views.sag2form, name='sag2form_update'),
    path('delete/<int:id>/', views.sag2formdelete, name='sag2form delete'),
    path('sag3form/', views.sag3form, name='sag3form'),
    path('sag3form/<int:id>/', views.sag3form, name='sag3form_update'),
    path('delete/<int:id>/', views.sag3formdelete, name='sag3form delete'),

    #TrainingAwareness
    path('tag1form/', views.tag1form, name='tag1form'),
    path('tag1form/<int:id>/', views.tag1form, name='tag1form_update'),
    path('delete/<int:id>/', views.tag1formdelete, name='tag1form delete'),
    path('tag2form/', views.tag2form, name='tag2form'),
    path('tag2form/<int:id>/', views.tag2form, name='tag2form_update'),
    path('delete/<int:id>/', views.tag2formdelete, name='tag2form delete'),

    #VulnerabilityManagement
    path('vmg1form/', views.vmg1form, name='vmg1form'),
    path('vmg1form/<int:id>/', views.vmg1form, name='vmg1form_update'),
    path('delete/<int:id>/', views.vmg1formdelete, name='vmg1form delete'),
    path('vmg2form/', views.vmg2form, name='vmg2form'),
    path('vmg2form/<int:id>/', views.vmg2form, name='vmg2form_update'),
    path('delete/<int:id>/', views.vmg2formdelete, name='vmg2form delete'),
    path('vmg3form/', views.vmg3form, name='vmg3form'),
    path('vmg3form/<int:id>/', views.vmg3form, name='vmg3form_update'),
    path('delete/<int:id>/', views.vmg3formdelete, name='vmg3form delete'),
    path('vmg4form/', views.vmg4form, name='vmg4form'),
    path('vmg4form/<int:id>/', views.vmg4form, name='vmg4form_update'),
    path('delete/<int:id>/', views.vmg4formdelete, name='vmg4form delete'),

    #MILForms
    #AssetManagement
    path('ammil2form/', views.ammil2form, name='ammil2form'),
    path('ammil2form/<int:id>/', views.ammil2form, name='ammil2form_update'),
    path('delete/<int:id>/', views.ammil2formdelete, name='ammil2form delete'),
    path('ammil3form/', views.ammil3form, name='ammil3form'),
    path('ammil3form/<int:id>/', views.ammil3form, name='ammil3form_update'),
    path('delete/<int:id>/', views.ammil3formdelete, name='ammil3form delete'),
    path('ammil4form/', views.ammil4form, name='ammil4form'),
    path('ammil4form/<int:id>/', views.ammil4form, name='ammil4form_update'),
    path('delete/<int:id>/', views.ammil4formdelete, name='ammil4form delete'),
    path('ammil5form/', views.ammil5form, name='ammil5form'),
    path('ammil5form/<int:id>/', views.ammil5form, name='ammil5form_update'),
    path('delete/<int:id>/', views.ammil5formdelete, name='ammil5form delete'),

    #ConfigurationChangeManagement
    path('ccmmil2form/', views.ccmmil2form, name='ccmmil2form'),
    path('ccmmil2form/<int:id>/', views.ccmmil2form, name='ccmmil2form_update'),
    path('delete/<int:id>/', views.ccmmil2formdelete, name='ccmmil2form delete'),
    path('ccmmil3form/', views.ccmmil3form, name='ccmmil3form'),
    path('ccmmil3form/<int:id>/', views.ccmmil3form, name='ccmmil3form_update'),
    path('delete/<int:id>/', views.ccmmil3formdelete, name='ccmmil3form delete'),
    path('ccmmil4form/', views.ccmmil4form, name='ccmmil4form'),
    path('ccmmil4form/<int:id>/', views.ccmmil4form, name='ccmmil4form_update'),
    path('delete/<int:id>/', views.ccmmil4formdelete, name='ccmmil4form delete'),
    path('ccmmil5form/', views.ccmmil5form, name='ccmmil5form'),
    path('ccmmil5form/<int:id>/', views.ccmmil5form, name='ccmmil5form_update'),
    path('delete/<int:id>/', views.ccmmil5formdelete, name='ccmmil5form delete'),

    #controlsmanagement
    path('cmmil2form/', views.cmmil2form, name='cmmil2form'),
    path('cmmil2form/<int:id>/', views.cmmil2form, name='cmmil2form_update'),
    path('delete/<int:id>/', views.cmmil2formdelete, name='cmmil2form delete'),
    path('cmmil3form/', views.cmmil3form, name='cmmil3form'),
    path('cmmil3form/<int:id>/', views.cmmil3form, name='cmmil3form_update'),
    path('delete/<int:id>/', views.cmmil3formdelete, name='cmmil3form delete'),
    path('cmmil4form/', views.cmmil4form, name='cmmil4form'),
    path('cmmil4form/<int:id>/', views.cmmil4form, name='cmmil4form_update'),
    path('delete/<int:id>/', views.cmmil4formdelete, name='cmmil4form delete'),
    path('cmmil5form/', views.cmmil5form, name='cmmil5form'),
    path('cmmil5form/<int:id>/', views.cmmil5form, name='cmmil5form_update'),
    path('delete/<int:id>/', views.cmmil5formdelete, name='cmmil5form delete'),

    #ExternalDependenciesManagement
    path('edmmil2form/', views.edmmil2form, name='edmmil2form'),
    path('edmmil2form/<int:id>/', views.edmmil2form, name='edmmil2form_update'),
    path('delete/<int:id>/', views.edmmil2formdelete, name='edmmil2form delete'),
    path('edmmil3form/', views.edmmil3form, name='edmmil3form'),
    path('edmmil3form/<int:id>/', views.edmmil3form, name='edmmil3form_update'),
    path('delete/<int:id>/', views.edmmil3formdelete, name='edmmil23orm delete'),
    path('edmmil4form/', views.edmmil4form, name='edmmil4form'),
    path('edmmil4form/<int:id>/', views.edmmil4form, name='edmmil4form_update'),
    path('delete/<int:id>/', views.edmmil4formdelete, name='edmmil24orm delete'),
    path('edmmil5form/', views.edmmil5form, name='edmmil5form'),
    path('edmmil5form/<int:id>/', views.edmmil5form, name='edmmil5form_update'),
    path('delete/<int:id>/', views.edmmil5formdelete, name='edmmil5form delete'),

    #IncidentManagement
    path('immil2form/', views.immil2form, name='immil2form'),
    path('immil2form/<int:id>/', views.immil2form, name='immil2form_update'),
    path('delete/<int:id>/', views.immil2formdelete, name='immil2form delete'),
    path('immil3form/', views.immil3form, name='immil3form'),
    path('immil3form/<int:id>/', views.immil3form, name='immil3form_update'),
    path('delete/<int:id>/', views.immil3formdelete, name='immil3form delete'),
    path('immil4form/', views.immil4form, name='immil4form'),
    path('immil4form/<int:id>/', views.immil4form, name='immil4form_update'),
    path('delete/<int:id>/', views.immil4formdelete, name='immil4form delete'),
    path('immil5form/', views.immil5form, name='immil5form'),
    path('immil5form/<int:id>/', views.immil5form, name='immil5form_update'),
    path('delete/<int:id>/', views.immil5formdelete, name='immil5form delete'),

    #RiskManagement
    path('rmmil2form/', views.rmmil2form, name='rmmil2form'),
    path('rmmil2form/<int:id>/', views.rmmil2form, name='rmmil2form_update'),
    path('delete/<int:id>/', views.rmmil2formdelete, name='rmmil2form delete'),
    path('rmmil3form/', views.rmmil3form, name='rmmil3form'),
    path('rmmil3form/<int:id>/', views.rmmil3form, name='rmmil3form_update'),
    path('delete/<int:id>/', views.rmmil3formdelete, name='rmmil3form delete'),
    path('rmmil4form/', views.rmmil4form, name='rmmil4form'),
    path('rmmil4form/<int:id>/', views.rmmil4form, name='rmmil4form_update'),
    path('delete/<int:id>/', views.rmmil4formdelete, name='rmmil4form delete'),
    path('rmmil5form/', views.rmmil5form, name='rmmil5form'),
    path('rmmil5form/<int:id>/', views.rmmil5form, name='rmmil5form_update'),
    path('delete/<int:id>/', views.rmmil5formdelete, name='rmmil5form delete'),

    #ServiceContinuityManagement
    path('scmmil2form/', views.scmmil2form, name='scmmil2form'),
    path('scmmil2form/<int:id>/', views.scmmil2form, name='scmmil2form_update'),
    path('delete/<int:id>/', views.scmmil2formdelete, name='scmmil2form delete'),
    path('scmmil3form/', views.scmmil3form, name='scmmil3form'),
    path('scmmil3form/<int:id>/', views.scmmil3form, name='scmmil3form_update'),
    path('delete/<int:id>/', views.scmmil3formdelete, name='scmmil3form delete'),
    path('scmmil4form/', views.scmmil4form, name='scmmil4form'),
    path('scmmil4form/<int:id>/', views.scmmil4form, name='scmmil4form_update'),
    path('delete/<int:id>/', views.scmmil4formdelete, name='scmmil4form delete'),
    path('scmmil5form/', views.scmmil5form, name='scmmil5form'),
    path('scmmil5form/<int:id>/', views.scmmil5form, name='scmmil5form_update'),
    path('delete/<int:id>/', views.scmmil5formdelete, name='scmmil5form delete'),

    #situationalawareness
    path('samil2form/', views.samil2form, name='samil2form'),
    path('samil2form/<int:id>/', views.samil2form, name='samil2form_update'),
    path('delete/<int:id>/', views.samil2formdelete, name='samil2form delete'),
    path('samil3form/', views.samil3form, name='samil3form'),
    path('samil3form/<int:id>/', views.samil3form, name='samil3form_update'),
    path('delete/<int:id>/', views.samil3formdelete, name='samil3form delete'),
    path('samil4form/', views.samil4form, name='samil4form'),
    path('samil4form/<int:id>/', views.samil4form, name='samil4form_update'),
    path('delete/<int:id>/', views.samil4formdelete, name='samil4form delete'),
    path('samil5form/', views.samil5form, name='samil5form'),
    path('samil5form/<int:id>/', views.samil5form, name='samil5form_update'),
    path('delete/<int:id>/', views.samil5formdelete, name='samil5form delete'),

    #TrainingAwareness
    path('tamil2form/', views.tamil2form, name='tamil2form'),
    path('tamil2form/<int:id>/', views.tamil2form, name='tamil2form_update'),
    path('delete/<int:id>/', views.tamil2formdelete, name='tamil2form delete'),
    path('tamil3form/', views.tamil3form, name='tamil3form'),
    path('tamil3form/<int:id>/', views.tamil3form, name='tamil3form_update'),
    path('delete/<int:id>/', views.tamil3formdelete, name='tamil3form delete'),
    path('tamil4form/', views.tamil4form, name='tamil4form'),
    path('tamil4form/<int:id>/', views.tamil4form, name='tamil4form_update'),
    path('delete/<int:id>/', views.tamil4formdelete, name='tamil4form delete'),
    path('tamil5form/', views.tamil5form, name='tamil5form'),
    path('tamil5form/<int:id>/', views.tamil5form, name='tamil5form_update'),
    path('delete/<int:id>/', views.tamil5formdelete, name='tamil5form delete'),

    #VulnerabilityManagement
    path('vmmil2form/', views.vmmil2form, name='vmmil2form'),
    path('vmmil2form/<int:id>/', views.vmmil2form, name='vmmil2form_update'),
    path('delete/<int:id>/', views.vmmil2formdelete, name='vmmil2form delete'),
    path('vmmil3form/', views.vmmil3form, name='vmmil3form'),
    path('vmmil3form/<int:id>/', views.vmmil3form, name='vmmil3form_update'),
    path('delete/<int:id>/', views.vmmil3formdelete, name='vmmil3form delete'),
    path('vmmil4form/', views.vmmil4form, name='vmmil4form'),
    path('vmmil4form/<int:id>/', views.vmmil4form, name='vmmil4form_update'),
    path('delete/<int:id>/', views.vmmil4formdelete, name='vmmil4form delete'),
    path('vmmil5form/', views.vmmil5form, name='vmmil5form'),
    path('vmmil5form/<int:id>/', views.vmmil5form, name='vmmil5form_update'),
    path('delete/<int:id>/', views.vmmil5formdelete, name='vmmil5form delete'),

    #TABLE REPORTS
    #GoalTableReports
    #AssetManagement
    path('amg1table/', views.amg1table, name='amg1table'),
    path('amg2table/', views.amg2table, name='amg2table'),
    path('amg3table/', views.amg3table, name='amg3table'),
    path('amg4table/', views.amg4table, name='amg4table'),
    path('amg5table/', views.amg5table, name='amg5table'),
    path('amg6table/', views.amg6table, name='amg6table'),
    path('amg7table/', views.amg7table, name='amg7table'),

    #ConfigurationChangeManagement
    path('ccmg1table/', views.ccmg1table, name='ccmg1table'),
    path('ccmg2table/', views.ccmg2table, name='ccmg2table'),
    path('ccmg3table/', views.ccmg3table, name='ccmg3table'),

    #controlsmanagement
    path('cmg1table/', views.cmg1table, name='cmg1table'),
    path('cmg2table/', views.cmg2table, name='cmg2table'),
    path('cmg3table/', views.cmg3table, name='cmg3table'),
    path('cmg4table/', views.cmg4table, name='cmg4table'),
    #ExternalDependenciesManagement
    path('edmg1table/', views.edmg1table, name='edmg1table'),
    path('edmg2table/', views.edmg2table, name='edmg2table'),
    path('edmg3table/', views.edmg3table, name='edmg3table'),
    path('edmg4table/', views.edmg4table, name='edmg4table'),
    path('edmg5table/', views.edmg5table, name='edmg5table'),

    #IncidentManagement
    path('img1table/', views.img1table, name='img1table'),
    path('img2table/', views.img2table, name='img2table'),
    path('img3table/', views.img3table, name='img3table'),
    path('img4table/', views.img4table, name='img4table'),
    path('img5table/', views.img5table, name='img5table'),

    #RiskManagement
    path('rmg1table/', views.rmg1table, name='rmg1table'),
    path('rmg2table/', views.rmg2table, name='rmg2table'),
    path('rmg3table/', views.rmg3table, name='rmg3table'),
    path('rmg4table/', views.rmg4table, name='rmg4table'),
    path('rmg5table/', views.rmg5table, name='rmg5table'),

    #ServiceContinuityManagement
    path('scmg1table/', views.scmg1table, name='scmg1table'),
    path('scmg2table/', views.scmg2table, name='scmg2table'),
    path('scmg3table/', views.scmg3table, name='scmg3table'),
    path('scmg4table/', views.scmg4table, name='scmg4table'),

    #situationalawareness
    path('sag1table/', views.sag1table, name='sag1table'),
    path('sag2table/', views.sag2table, name='sag2table'),
    path('sag3table/', views.sag3table, name='sag3table'),

    #TrainingAwareness
    path('tag1table/', views.tag1table, name='tag1table'),
    path('tag2table/', views.tag2table, name='tag2table'),

    #VulnerabilityManagement
    path('vmg1table/', views.vmg1table, name='vmg1table'),
    path('vmg2table/', views.vmg2table, name='vmg2table'),
    path('vmg3table/', views.vmg3table, name='vmg3table'),
    path('vmg4table/', views.vmg4table, name='vmg4table'),

    #MILtables
    #AssetManagement
    path('ammil2table/', views.ammil2table, name='ammil2table'),
    path('ammil3table/', views.ammil3table, name='ammil3table'),
    path('ammil4table/', views.ammil4table, name='ammil4table'),
    path('ammil5table/', views.ammil5table, name='ammil5table'),

    #ConfigurationChangeManagement
    path('ccmmil2table/', views.ccmmil2table, name='ccmmil2table'),
    path('ccmmil3table/', views.ccmmil3table, name='ccmmil3table'),
    path('ccmmil4table/', views.ccmmil4table, name='ccmmil4table'),
    path('ccmmil5table/', views.ccmmil5table, name='ccmmil5table'),

    #controlsmanagement
    path('cmmil2table/', views.cmmil2table, name='cmmil2table'),
    path('cmmil3table/', views.cmmil3table, name='cmmil3table'),
    path('cmmil4table/', views.cmmil4table, name='cmmil4table'),
    path('cmmil5table/', views.cmmil5table, name='cmmil5table'),

    #ExternalDependenciesManagement
    path('edmmil2table/', views.edmmil2table, name='edmmil2table'),
    path('edmmil3table/', views.edmmil3table, name='edmmil3table'),
    path('edmmil4table/', views.edmmil4table, name='edmmil4table'),
    path('edmmil5table/', views.edmmil5table, name='edmmil5table'),

    #IncidentManagement
    path('immil2table/', views.immil2table, name='immil2table'),
    path('immil3table/', views.immil3table, name='immil3table'),
    path('immil4table/', views.immil4table, name='immil4table'),
    path('immil5table/', views.immil5table, name='immil5table'),

    #RiskManagement
    path('rmmil2table/', views.rmmil2table, name='rmmil2table'),
    path('rmmil3table/', views.rmmil3table, name='rmmil3table'),
    path('rmmil4table/', views.rmmil4table, name='rmmil4table'),
    path('rmmil5table/', views.rmmil5table, name='rmmil5table'),

    #ServiceContinuityManagement
    path('scmmil2table/', views.scmmil2table, name='scmmil2table'),
    path('scmmil3table/', views.scmmil3table, name='scmmil3table'),
    path('scmmil4table/', views.scmmil4table, name='scmmil4table'),
    path('scmmil5table/', views.scmmil5table, name='scmmil5table'),

    #situationalawareness
    path('samil2table/', views.samil2table, name='samil2table'),
    path('samil3table/', views.samil3table, name='samil3table'),
    path('samil4table/', views.samil4table, name='samil4table'),
    path('samil5table/', views.samil5table, name='samil5table'),

    #TrainingAwareness
    path('tamil2table/', views.tamil2table, name='tamil2table'),
    path('tamil3table/', views.tamil3table, name='tamil3table'),
    path('tamil4table/', views.tamil4table, name='tamil4table'),
    path('tamil5table/', views.tamil5table, name='tamil5table'),

    #VulnerabilityManagement
    path('vmmil2table/', views.vmmil2table, name='vmmil2table'),
    path('vmmil3table/', views.vmmil3table, name='vmmil3table'),
    path('vmmil4table/', views.vmmil4table, name='vmmil4table'),
    path('vmmil5table/', views.vmmil5table, name='vmmil5table'),
    #path('/', views.),
    #path('/', views.),
    #path('/', views.),
    #path('/', views.),
    #path('/', views.),
    #path('/', views.),
    #path('/', views.),
    #path('/', views.),
    #path('/', views.),
]