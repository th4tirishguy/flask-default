from flask import render_template, request, redirect, url_for
from . import players
from .. import db
from .forms import PlayerForm
from ..models import Player

@players.route('/', methods=['GET', 'POST'])
def index():
	return "Hello World!"