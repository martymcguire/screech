from flask import Blueprint, redirect, render_template, request, session, url_for

from ..extensions import micropub, micropub_config
from ..auth import login_required, login_save_session

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.jinja2')

@views.route('/authorize')
def authorize():
    return micropub.authorize(
        request.args.get('me'), next_url=url_for('.index'),
        scope=request.args.get('scope'))

@views.route('/micropub-callback')
@micropub.authorized_handler
def micropub_callback(resp):
    login_save_session(resp)
    mp_config = micropub_config(resp.micropub_endpoint, resp.access_token)
    session['_micropub_config'] = mp_config.mp_config
    return redirect(url_for('.new'))

@views.route('/new')
@login_required
def new():
    me = session.get('_micropub_me')
    endpoint = session.get('_micropub_endpoint')
    access_token = session.get('_micropub_access_token')
    mp_config = session.get('_micropub_config')
    return render_template(
      'new.jinja2', me=me,
      endpoint=endpoint, access_token=access_token,
      config=mp_config
    )

