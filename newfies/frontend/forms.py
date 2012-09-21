from django import forms
from django.utils.translation import ugettext_lazy as _
from dialer_campaign.models import Campaign
from frontend.constants import SEARCH_TYPE


class LoginForm(forms.Form):
    """Client Login Form"""
    user = forms.CharField(max_length=30,
        label=_('Username:'), required=True)
    user.widget.attrs['class'] = 'input-small'
    user.widget.attrs['placeholder'] = 'Username'
    password = forms.CharField(max_length=30, label=_('Password:'),
        required=True, widget=forms.PasswordInput())
    password.widget.attrs['class'] = 'input-small'
    password.widget.attrs['placeholder'] = 'Password'


class DashboardForm(forms.Form):
    """Dashboard Form"""
    campaign = forms.ChoiceField(label=_('Campaign'), required=False)
    search_type = forms.ChoiceField(label=_('Type'), required=False, initial=4,
        choices=list(SEARCH_TYPE))

    def __init__(self, user, *args, **kwargs):
        super(DashboardForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['campaign', 'search_type']
        # To get user's running campaign list
        if user:
            list = []
            #list.append((0, '---'))
            listc = Campaign.objects.filter(user=user)
            cp_list = ((l.id, l.name) for l in listc)

            for i in cp_list:
                list.append((i[0], i[1]))
            self.fields['campaign'].choices = list
