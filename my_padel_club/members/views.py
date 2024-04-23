from django.http import HttpResponse 
from django.template import loader 
from .models import Member

def testing(request):
    mymembers = Member.objects.all()
    singlemember = mymembers[2]
    template = loader.get_template('template.html')
    context = {
        'singlemember' : singlemember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context,request))

