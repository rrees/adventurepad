from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
import os

import webapp2
import jinja2

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


from queries import all_titles
from forms import DestinyQuestFightForm
from destiny_quest.fight import resolve_fight
from destiny_quest.models import Combatant

templates = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def find_template(template_name):
	return os.path.join(os.path.dirname(__file__), 'templates', template_name)


class MainHandler(webapp.RequestHandler):

	def get(self):
		template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
		self.response.out.write(template.render(template_path, {}))

class AdventuresHandler(webapp.RequestHandler):
	
	def get(self):
		template_path = os.path.join(os.path.dirname(__file__), 'templates', 'titles.html')
		self.response.out.write(template.render(template_path, {'titles' : all_titles()}))
		
class DestinyQuestFightHandler(webapp.RequestHandler):
	
	def get(self):
		template_path = find_template('dq-fight.html')
		self.response.out.write(template.render(template_path, {'form' : DestinyQuestFightForm()}))
		
	def post(self):
		template_path = find_template('dq-fight.html')
		form = DestinyQuestFightForm(self.request.POST)
		if form.is_valid():
			hero = Combatant('Player', form.cleaned_data['player_health'],
				speed = form.cleaned_data['player_speed'],
				brawn = form.cleaned_data['player_brawn'],
				armour = form.cleaned_data['player_armour'])
			monster = Combatant(form.cleaned_data['monster_name'], form.cleaned_data['monster_health'],
				speed = form.cleaned_data['monster_speed'],
				brawn = form.cleaned_data['monster_brawn'],
				armour = form.cleaned_data['monster_armour'])
			results = resolve_fight(hero, monster)
			
		template_data = {
			'form' : form,
			'results' : results,
			'winner' : "player" if results[-1]['player']['health'] > results[-1]['monster']['health'] else form.cleaned_data['monster_name'] 
		}

		self.response.out.write(template.render(template_path, template_data))

class DiceHandler(webapp.RequestHandler):
	def get(self):
		template_path = find_template('dice.html')
		self.response.out.write(template.render(template_path, {}))

app = webapp2.WSGIApplication([
		('/', MainHandler),
		('/destiny-quest/fight', DestinyQuestFightHandler),
		('/dice', DiceHandler), ],
		debug=True)
