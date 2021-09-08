from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.generic import ListView

from .models import Weather, Summary
from .forms import AddWeatherForm


def add_weather(request):
    """
    Add new weather record.
    """
    if request.method == "POST":
        form = AddWeatherForm(request.POST)
        if form.is_valid():
            form.save()
            # Display success message.
            messages.success(request, f'New weather record has been added successfully.', extra_tags='add-weather')
            return redirect('weather:weather-list')
    else:
        form = AddWeatherForm()          
    context = {'form':form}
    return render(request, 'weather/add_weather.html', context)


def weather_list(request):
    """
    Display weather records list.
    """
    qs = Weather.objects.all()
    context = {'weather_records': qs}
    return render(request, 'weather/weather_list.html', context)


def summary_list(request):
    """
    Display summary records list.
    """
    qs = Summary.objects.all()
    context = {'summary_records': qs}
    return render(request, 'weather/summary_list.html', context)


def delete_summary(request, summary_id):
    """
    Take summary's id, and get its summary and delete it.
    """
    # get summary by its id. 
    summary = get_object_or_404(Summary, pk=summary_id)
    data = dict()
    if request.method == 'POST':
        # delete summary.
        summary.delete()
        data['form_is_valid'] = True
        qs = Summary.objects.all()
        context = {'summary_records': qs, 'request':request}
        data['html_summary_list'] = render_to_string('weather/includes/partial_summary_list.html', context, request=request)
    else:
        context = {'summary': summary}
        data['html_form'] = render_to_string('weather/includes/partial_summary_delete.html', context, request=request)
    return JsonResponse(data)    


# class WeatherListView(ListView):
#     """
#     """
#     model = Weather
#     context_object_name = 'weather_records'
#     template_name = 'weather/weather_list.html'

