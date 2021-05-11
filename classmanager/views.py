from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "classroom/index.html"

from django.shortcuts import render_to_response

def myViewFunction(request):
    return render_to_response('classroom/index.html', myContext, context_instance=RequestContext(request))
