#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from dnc.models import DNC, DNCContact


class DNCForm(ModelForm):
    """DNC ModelForm"""

    class Meta:
        model = DNC
        fields = ['name']
        exclude = ('user',)


class DNCContactSearchForm(forms.Form):
    """Search Form on Contact List"""
    phone_number = forms.CharField(label=_('phone number'), required=False,
                                 widget=forms.TextInput(attrs={'size': 15}))
    # contact_no_type = forms.ChoiceField(label='', required=False, initial=1,
    #                                     choices=list(CHOICE_TYPE), widget=forms.RadioSelect)
    dnc = forms.ChoiceField(label=_('Do Not Call list').title(), required=False)

    def __init__(self, user, *args, **kwargs):
        super(DNCContactSearchForm, self).__init__(*args, **kwargs)
         # To get user's dnc list
        if user:
            dnc_list_user = []
            dnc_list_user.append((0, '---'))
            dnc_list = DNC.objects.values_list('id', 'name').filter(user=user).order_by('-id')
            for i in dnc_list:
                dnc_list_user.append((i[0], i[1]))

            self.fields['dnc'].choices = dnc_list_user


class DNCContactForm(ModelForm):
    """DNCContact ModelForm"""

    class Meta:
        model = DNCContact
        fields = ['dnc', 'phone_number']

    def __init__(self, user, *args, **kwargs):
        super(DNCContactForm, self).__init__(*args, **kwargs)
        # To get user's dnc list
        if user:
            self.fields['dnc'].choices = \
                DNC.objects.values_list('id', 'name').filter(user=user).order_by('id')
