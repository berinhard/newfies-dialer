from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
from handlers import callrequestHandler, testcallHandler, \
answercallHandler, hangupcallHandler, testHandler
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
#from django.views.decorators.cache import cache_page
import custom_xml_emitter
#from common.custom_xml_emitter import CustomXmlEmitter

ALLOWED_IP_LIST = ['127.0.0.1' , 'localhost']

class IpAuthentication(object):
    """
    IP Authentication handler
    """
    def __init__(self, auth_func=authenticate, realm='API'):
        self.auth_func = auth_func
        self.realm = realm

    def is_authenticated(self, request):
        try:
            ALLOWED_IP_LIST.index(request.META['REMOTE_ADDR'])
            return True
        except:
            return False

    def challenge(self):
        resp = HttpResponse("Not Authorized")
        resp.status_code = 401
        return resp

auth = HttpBasicAuthentication(realm='Newfies Application')
auth_ip = IpAuthentication()

callrequest_handler = Resource(callrequestHandler, authentication=auth)

#API for test
testcall_handler = Resource(testcallHandler, authentication=auth_ip)
answercall_handler = Resource(answercallHandler, authentication=auth_ip)
hangupcall_handler = Resource(hangupcallHandler, authentication=auth_ip)
test_handler = Resource(testHandler, authentication=auth_ip)

urlpatterns = patterns('',

    url(r'^callrequest[/]$', callrequest_handler),
    url(r'^callrequest/(?P<callrequest_id>[^/]+)', callrequest_handler),

    url(r'^testcall[/]$', testcall_handler),
    url(r'^answercall[/]$', answercall_handler,
                                    {'emitter_format': 'custom_xml'}),
    url(r'^hangupcall[/]$', hangupcall_handler),

    url(r'^test[/]$', test_handler, {'emitter_format': 'custom_xml'}),

    # automated documentation
    url(r'^doc[/]$', documentation_view),
)
