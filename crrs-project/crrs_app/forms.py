from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()

from .models import cseformdb
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

# Create your form functions here


# CSE FORM
class cse_form(forms.ModelForm):

    class Meta:
        model = cseformdb
        fields = ('expertid', 'formdomainlevel')
        labels = {
            'expertid': 'Expert ID:', 
            'formdomainlevel': 'Form Domain Level' 
        }


# Forms
#Goal Forms
#Asset Management Forms
# amg1form
class amg_one_form(forms.ModelForm):

    class Meta:
        model = amg1formdb
        fields = ('expertid', 'formid', 'response_one',
                  'response_two', 'response_three', 'response_four','amg1_complete','amg1_incomplete')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' ',
            'response_eight': ' ',
            'response_nine': ' ',
            'response_ten': ' ',
            'amg1_complete':'Complete Responses',
            'amg1_incomplete':'Incomplete Responses'
        }

    def __init__(self, *args, **kwargs):
        super(amg_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# amg2form
class amg_two_form(forms.ModelForm):

    class Meta:
        model = amg2formdb
        fields = ('expertid', 'formid', 'response_one',
                  'response_two', 'response_three', 'response_four', 'response_five', 'amg2_complete', 'amg2_incomplete' )
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'amg2_complete':'Complete Responses',
            'amg2_incomplete':'Incomplete Responses'
        }

    def __init__(self, *args, **kwargs):
        super(amg_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# amg3form
class amg_three_form(forms.ModelForm):

    class Meta:
        model = amg3formdb
        fields = ('expertid', 'formid', 'response_one','response_two' )
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(amg_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# amg4form
class amg_four_form(forms.ModelForm):

    class Meta:
        model = amg4formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(amg_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# amg5form
class amg_five_form(forms.ModelForm):

    class Meta:
        model = amg5formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six', 'response_seven' )
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' '
        }

    def __init__(self, *args, **kwargs):
        super(amg_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# amg6form
class amg_six_form(forms.ModelForm):

    class Meta:
        model = amg6formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six', 'response_seven')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' '
        }

    def __init__(self, *args, **kwargs):
        super(amg_six_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# amg7form
class amg_seven_form(forms.ModelForm):

    class Meta:
        model = amg7formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(amg_seven_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Configuration Change Management
# ccmg1form
class ccmg_one_form(forms.ModelForm):

    class Meta:
        model = ccmg1formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ccmg_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ccmg2form
class ccmg_two_form(forms.ModelForm):

    class Meta:
        model = ccmg2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six', 'response_seven', 'response_eight', 'response_nine', 'response_ten' )
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' ',
            'response_eight': ' ',
            'response_nine': ' ',
            'response_ten': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ccmg_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ccmg3form
class ccmg_three_form(forms.ModelForm):

    class Meta:
        model = ccmg3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six' )
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ccmg_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Control Management Forms
# cmg1form
class cmg_one_form(forms.ModelForm):

    class Meta:
        model = cmg1formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmg_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# cmg2form
class cmg_two_form(forms.ModelForm):

    class Meta:
        model = cmg2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six', 'response_seven', 'response_eight', 'response_nine', 'response_ten' )
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' ',
            'response_eight': ' ',
            'response_nine': ' ',
            'response_ten': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmg_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# cmg3form
class cmg_three_form(forms.ModelForm):

    class Meta:
        model = cmg3formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmg_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# cmg4form
class cmg_four_form(forms.ModelForm):

    class Meta:
        model = cmg4formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmg_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#External Dependencies Management Forms
# edmg1form
class edmg_one_form(forms.ModelForm):

    class Meta:
        model = edmg1formdb
        fields = ('expertid', 'formid', 'response_one',
                  'response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmg_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# edmg2form
class edmg_two_form(forms.ModelForm):

    class Meta:
        model = edmg2formdb
        fields = ('expertid', 'formid', 'response_one',)
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmg_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# edmg3form
class edmg_three_form(forms.ModelForm):

    class Meta:
        model = edmg3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmg_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# edmg4form
class edmg_four_form(forms.ModelForm):

    class Meta:
        model = edmg4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmg_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# edmg5form
class edmg_five_form(forms.ModelForm):

    class Meta:
        model = edmg5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmg_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Incident Management Forms
# img1form
class img_one_form(forms.ModelForm):

    class Meta:
        model = img1formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(img_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# img2form
class img_two_form(forms.ModelForm):

    class Meta:
        model = img2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six', 'response_seven', 'response_eight', 'response_nine' )
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' ',
            'response_eight': ' ',
            'response_nine': ' '
        }

    def __init__(self, *args, **kwargs):
        super(img_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# img3form
class img_three_form(forms.ModelForm):

    class Meta:
        model = img3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(img_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# img4form
class img_four_form(forms.ModelForm):

    class Meta:
        model = img4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(img_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# img5form
class img_five_form(forms.ModelForm):

    class Meta:
        model = img5formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(img_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Risk Management Forms
# rmg1form
class rmg_one_form(forms.ModelForm):

    class Meta:
        model = rmg1formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmg_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# rmg2form
class rmg_two_form(forms.ModelForm):

    class Meta:
        model = rmg2formdb
        fields = ('expertid', 'formid', 'response_one','response_two','response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmg_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# rmg3form
class rmg_three_form(forms.ModelForm):

    class Meta:
        model = rmg3formdb
        fields = ('expertid', 'formid', 'response_one')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmg_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# rmg4form
class rmg_four_form(forms.ModelForm):

    class Meta:
        model = rmg4formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmg_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# rmg5form
class rmg_five_form(forms.ModelForm):

    class Meta:
        model = rmg5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmg_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Service Continuity Management Forms
# scmg1form
class scmg_one_form(forms.ModelForm):

    class Meta:
        model = scmg1formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six', 'response_seven')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmg_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# scmg2form
class scmg_two_form(forms.ModelForm):

    class Meta:
        model = scmg2formdb
        fields = ('expertid', 'formid', 'response_one',)
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmg_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# scmg3form
class scmg_three_form(forms.ModelForm):

    class Meta:
        model = scmg3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmg_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# scmg4form
class scmg_four_form(forms.ModelForm):

    class Meta:
        model = scmg4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmg_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Situational Awareness Forms
# sag1form
class sag_one_form(forms.ModelForm):

    class Meta:
        model = sag1formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(sag_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# sag2form
class sag_two_form(forms.ModelForm):

    class Meta:
        model = sag2formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(sag_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# sag3form
class sag_three_form(forms.ModelForm):

    class Meta:
        model = sag3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(sag_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Training Awareness Forms
# tag1form
class tag_one_form(forms.ModelForm):

    class Meta:
        model = tag1formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(tag_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#tag2form
class tag_two_form(forms.ModelForm):

    class Meta:
        model = tag2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' '
        }

    def __init__(self, *args, **kwargs):
        super(tag_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Vulnerability Management Forms
# vmg1form
class vmg_one_form(forms.ModelForm):

    class Meta:
        model = vmg1formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmg_one_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# vmg2form
class vmg_two_form(forms.ModelForm):

    class Meta:
        model = vmg2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmg_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# vmg3form
class vmg_three_form(forms.ModelForm):

    class Meta:
        model = vmg3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmg_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# vmg4form
class vmg_four_form(forms.ModelForm):

    class Meta:
        model = vmg4formdb
        fields = ('expertid', 'formid', 'response_one')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmg_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'


#Maturity Indicator Level Forms
#Asset Management Forms
# ammil2form
class ammil_two_form(forms.ModelForm):

    class Meta:
        model = ammil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ammil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ammil3form
class ammil_three_form(forms.ModelForm):

    class Meta:
        model = ammil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            
        }

    def __init__(self, *args, **kwargs):
        super(ammil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ammil4form
class ammil_four_form(forms.ModelForm):

    class Meta:
        model = ammil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ammil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ammil5form
class ammil_five_form(forms.ModelForm):

    class Meta:
        model = ammil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ammil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Configuration Change Management Forms
# ccmmil2form
class ccmmil_two_form(forms.ModelForm):

    class Meta:
        model = ccmmil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ccmmil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ccmmil3form
class ccmmil_three_form(forms.ModelForm):

    class Meta:
        model = ccmmil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '           
        }

    def __init__(self, *args, **kwargs):
        super(ccmmil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ccmmil4form
class ccmmil_four_form(forms.ModelForm):

    class Meta:
        model = ccmmil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ccmmil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# ccmmil5form
class ccmmil_five_form(forms.ModelForm):

    class Meta:
        model = ccmmil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(ccmmil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Controls Management Forms
# cmmil2form
class cmmil_two_form(forms.ModelForm):

    class Meta:
        model = cmmil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmmil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# cmmil3form
class cmmil_three_form(forms.ModelForm):

    class Meta:
        model = cmmil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmmil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# cmmil4form
class cmmil_four_form(forms.ModelForm):

    class Meta:
        model = cmmil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmmil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# cmmil5form
class cmmil_five_form(forms.ModelForm):

    class Meta:
        model = cmmil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(cmmil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#External Dependencies Management Forms
# edmmil2form
class edmmil_two_form(forms.ModelForm):

    class Meta:
        model = edmmil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmmil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# edmmil3form
class edmmil_three_form(forms.ModelForm):

    class Meta:
        model = edmmil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmmil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# edmmil4form
class edmmil_four_form(forms.ModelForm):

    class Meta:
        model = edmmil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmmil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# edmmil5form
class edmmil_five_form(forms.ModelForm):

    class Meta:
        model = edmmil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(edmmil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Incident Management Forms
#immil2form
class immil_two_form(forms.ModelForm):

    class Meta:
        model = immil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' '
        }

    def __init__(self, *args, **kwargs):
        super(immil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# immil3form
class immil_three_form(forms.ModelForm):

    class Meta:
        model = immil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four', 'response_five', 'response_six', 'response_seven')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' ',
            'response_five': ' ',
            'response_six': ' ',
            'response_seven': ' '
        }

    def __init__(self, *args, **kwargs):
        super(immil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# immil4form
class immil_four_form(forms.ModelForm):

    class Meta:
        model = immil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(immil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# immil5form
class immil_five_form(forms.ModelForm):

    class Meta:
        model = immil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(immil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Risk Management Forms
# rmmil2form
class rmmil_two_form(forms.ModelForm):

    class Meta:
        model = rmmil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmmil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# rmmil3form
class rmmil_three_form(forms.ModelForm):

    class Meta:
        model = rmmil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmmil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# rmmil4form
class rmmil_four_form(forms.ModelForm):

    class Meta:
        model = rmmil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmmil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# rmmil5form
class rmmil_five_form(forms.ModelForm):

    class Meta:
        model = rmmil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(rmmil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Service Continuity Management Forms
# scmmil2form
class scmmil_two_form(forms.ModelForm):

    class Meta:
        model = scmmil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmmil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# scmmil3form
class scmmil_three_form(forms.ModelForm):

    class Meta:
        model = scmmil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmmil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# scmmil4form
class scmmil_four_form(forms.ModelForm):

    class Meta:
        model = scmmil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmmil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# scmmil5form
class scmmil_five_form(forms.ModelForm):

    class Meta:
        model = scmmil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(scmmil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Situational Awareness Forms
# samil2form
class samil_two_form(forms.ModelForm):

    class Meta:
        model = samil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(samil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# samil3form
class samil_three_form(forms.ModelForm):

    class Meta:
        model = samil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(samil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# samil4form
class samil_four_form(forms.ModelForm):

    class Meta:
        model = samil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(samil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# samil5form
class samil_five_form(forms.ModelForm):

    class Meta:
        model = samil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(samil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Training Awareness Forms
# tamil2form
class tamil_two_form(forms.ModelForm):

    class Meta:
        model = tamil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(tamil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# tamil3form
class tamil_three_form(forms.ModelForm):

    class Meta:
        model = tamil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(tamil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# tamil4form
class tamil_four_form(forms.ModelForm):

    class Meta:
        model = tamil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(tamil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# tamil5form
class tamil_five_form(forms.ModelForm):

    class Meta:
        model = tamil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(tamil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

#Vulnerability Management Forms
# vmmil2form
class vmmil_two_form(forms.ModelForm):

    class Meta:
        model = vmmil2formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmmil_two_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# vmmil3form
class vmmil_three_form(forms.ModelForm):

    class Meta:
        model = vmmil3formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three', 'response_four')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' ',
            'response_four': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmmil_three_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# vmmil4form
class vmmil_four_form(forms.ModelForm):

    class Meta:
        model = vmmil4formdb
        fields = ('expertid', 'formid', 'response_one','response_two', 'response_three')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' ',
            'response_three': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmmil_four_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'

# vmmil5form
class vmmil_five_form(forms.ModelForm):

    class Meta:
        model = vmmil5formdb
        fields = ('expertid', 'formid', 'response_one','response_two')
        labels = {
            'expertid': 'Expert ID ',
            'formid': 'Form ID ',
            'response_one': ' ',
            'response_two': ' '
        }

    def __init__(self, *args, **kwargs):
        super(vmmil_five_form, self).__init__(*args, **kwargs)
        self.fields['expertid'].empty_label = 'Select Expert ID'










