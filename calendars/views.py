from django.shortcuts import get_object_or_404, redirect, render


from .models import Calendars
from .forms import EventRegistrationForm
import calendar

# Create your views here.

from datetime import date, datetime ,timedelta
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar



# Create your views here.
def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST  ,request.FILES)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventRegistrationForm()
    return render(request,"register_event.html",{"form":form})

class CalendarView(generic.ListView):
    model = Calendars
    template_name = 'calendars_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal=cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month       

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()
    
def event(request, event_id=None):
    instance = Calendars()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Calendars()
    
    form = EventRegistrationForm(request.POST,request.FILES or None, instance=instance)
    form = EventRegistrationForm(instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendars:calendar')
    return render(request, 'calendars_list.html', {'form': form})    