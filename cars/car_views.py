from django.shortcuts import render_to_response
from cars.cars_dicts import all_cars
from cars.models import CarSearch
from django.http import HttpResponse


def get_brand(request):

    brand=request.GET['brand']

    if brand=='выберите марку':
        return render_to_response('main.html', {'error': 'марка не выбрана'})
    f1 = CarSearch.objects.filter(id=1)[0]
    f1.brand=brand
    f1.save()
    return render_to_response('choose_mod.html', {'models_set': all_cars[f1.brand]})

def get_mod(request):

    mod = request.GET['model']
    
    if mod=='выберите модель':
        return render_to_response('choose_mod.html', {'models_set': all_cars[f1.brand].keys()})
    f1 = CarSearch.objects.filter(id=1)[0]
    f1.mod=mod
    f1.save()
    return render_to_response('choose_engine.html', {'engines_set': all_cars[f1.brand][f1.mod].keys()})

def get_engine(request):

    engine = request.GET['engine']
    
    if engine=='выберите тип двигателя':
        return render_to_response('choose_engine.html', {'engines_set': all_cars[f1.brand][f1.mod].keys()})
    f1 = CarSearch.objects.filter(id=1)[0]
    f1.engine_type=engine
    f1.save()
    return render_to_response('choose_year.html', {'years_set': all_cars[f1.brand][f1.mod][f1.engine_type]})

def get_year(request):

    year = request.GET['year']
    
    if year=='выберите год выпуска':
        return render_to_response('choose_year.html', {'years_set': all_cars[f1.brand][f1.mod][f1.engine_type]})
    f1 = CarSearch.objects.filter(id=1)[0]
    f1.year_made=year
    f1.save()
    message ='OK'+'\n'+f1.brand+'\n'+f1.mod+'\n'+f1.engine_type+'\n'+f1.year_made
    return HttpResponse(message)
#render_to_response('choose_engine.html', {'brand':brand, 'model': mod, 'engine': engine, 'engines_set': model_engine[mod]})