from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from cars.models import Car
from cars.forms import ContactForm


def index(request):

	message = 'Добро пожаловать!'

	return render_to_response('main.html', locals())

def register_user(request):
    return render_to_response('main.html', locals())

def log_in(request):
    return render_to_response('main.html', locals())

def search(request):
    
	if 'searcher' in request.GET:
		search_result = 'Вы искали: %r' % request.GET['searcher']
	else:
		search_result=None

	return render_to_response('main.html', locals())

def search2(request):
    errors=[]
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Input a search request!')
        elif len(q)>20:
            errors.append('A search request can not be longer than 20 characters!')
        else:
            found_cars = Car.objects.filter(brand__icontains=q)
            return render_to_response('search_results.html', {'found_cars': found_cars, 'query':q,} )

    return render_to_response('search_form.html', {'errors':errors})

def contact2(request):
    
    errors=[]
    if request.method=='POST':
        if not request.POST.get('subject', ''):
            errors.append('Input a subject!')
        if request.POST.get('e_mail', '')!='' and '@' not in request.POST['e_mail']:
            errors.append('Input a correct e-mail address!')
        if not request.POST.get('message', ''):
            errors.append('Input a message!')
        if not errors:

            print('sending...')
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 
                  'contact_form.html', 
                  {'errors':errors, 
                   'subject': request.POST.get('subject', ''), 
                   'e_mail': request.POST.get('e_mail', ''),
                   'message': request.POST.get('message', '')})


def contact(request, num=0):
    
    if request.method=='POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for el in cd.keys():
                print(cd[el])
            print('sending...')
            return HttpResponseRedirect('/contact/thanks/')

    else:

        form = ContactForm(initial={'subject': 'choose a subject...', 'e_mail': 'your e-mail...'})

    return render(request, 'contact_form.html', {'form': form,})
    

def contact_thanks(request):
    return HttpResponse('THANKS!!!')


def pushed_button(request, item_category=""):
    
    message = 'HERE ARE ALL THE '+item_category.upper()
    
    return render(request, 'pushed_button.html', {'message':message,})

def exp(request, num=0):
    print('cp1')
    if request.method=='POST':
        print('cp2')
        form = ContactForm()
        print('cp3')
        return render(request, 'pushed_button.html', {'message':'THANKS!!!',})
    else:
        form = ContactForm(initial={'subject': 'choose a subject...', 'e_mail': 'your e-mail...'})
            
    return render(request, 'exp.html', {'form': form,})
