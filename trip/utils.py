from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Trip, Location

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None,location=None,firstweekday=5):
		self.year = year
		self.month = month
		self.location  = location
		self.firstweekday  = firstweekday

		super(Calendar, self).__init__(firstweekday=5)

	# formats a day as a td
	# filter events by day
	def formatday(self, day, trips):
		trips_per_day = trips.filter(start_time__day=day)
		d = ''
		for trip in trips_per_day:
			d += f'<li> {trip.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, trips):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, trips)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter trips by year and month
	def formatmonth(self, withyear=True):
		trips = Trip.objects.filter(start_time__year=self.year, start_time__month=self.month)



		if self.location:
			trips = trips.filter(cityFrom__location=self.location)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar w-100 table-bordered">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, trips)}\n'
		cal += 	f'</table>'
		return cal
