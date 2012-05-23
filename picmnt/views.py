from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from picmnt.models import *
from django.contrib.auth.decorators import login_required


def main_page(request):
    return render_to_response('main_page.html')

def random_image(request):
    image = Image.objects.order_by('?')[:1]
    variables = RequestContext(request, {
            'image': image[0]
            })
    return render_to_response('random_image.html', variables)

