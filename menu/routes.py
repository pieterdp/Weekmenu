from flask import Blueprint, render_template
from flask_login import login_required
from datetime import datetime


gui = Blueprint('gui', __name__)


@gui.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@gui.route('/week', methods=['GET'])
@gui.route('/week/<string:week>', methods=['GET'])
def week_overview(week=None):
    if not week:
        week = datetime.now().strftime('%U')
    return render_template('weekmenu/week.html', week=week, title='Week {0}'.format(week))


@gui.route('/recipe/<string:recipe_id>', methods=['GET'])
def recipe(recipe_id):
    return render_template('weekmenu/recipe.html', recipe_id=recipe_id, title='Recept')
