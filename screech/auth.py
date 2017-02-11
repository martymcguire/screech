from functools import wraps
from flask import session, redirect, url_for, request

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        for attr in ['me', 'endpoint', 'access_token']:
           if (session.get("_micropub_{}".format(attr)) is None):
                return redirect(url_for('views.index', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def login_save_session(resp):
    session['_micropub_me'] = resp.me
    session['_micropub_endpoint'] = resp.micropub_endpoint
    session['_micropub_access_token'] = resp.access_token

