from django.forms import ModelForm, DateInput
from .models import Trip

class TripForm(ModelForm):
  class Meta:
    model = Trip
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    # fields = ('bus','driver1','driver2','cityFrom','cityTo','company')
    fields = '__all__'


  # def __init__(self, *args, **kwargs):
  #   super(TripForm, self).__init__(*args, **kwargs)
  #   # input_formats parses HTML5 datetime-local input to datetime field
  #   self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
  #   self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
