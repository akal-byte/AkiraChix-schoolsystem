
from datetime import date
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.safestring import mark_safe
from .forms import EventRegistrationForm
from .models import *
from .utils import Calendar
# Create your views here.
class CalendarView(generic.ListView):
    model = Calendars
    template_name = 'calendars_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def event(request, event_id=None):
    instance = Calendar()
    if event_id:
        instance = get_object_or_404(Calendar, pk=event_id)
    else:
        instance = Calendar()
    form = EventRegistrationForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('cal:calender')
    return render(request, 'calenders_list.html', {'form': form})

def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventRegistrationForm()
    return render(request,"register_event.html",{"form":form})