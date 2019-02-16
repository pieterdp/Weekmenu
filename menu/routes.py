from flask import Blueprint, render_template
from flask_login import login_required


gui = Blueprint('gui', __name__)


@gui.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@gui.route('/week', methods=['GET'])
@gui.route('/week/<string:week>', methods=['GET'])
def week_overview(week=None):
    return render_template('weekmenu/week.html', week=week)