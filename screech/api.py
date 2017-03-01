from flask import Blueprint, request, session, redirect
from .auth import login_required
import requests

api = Blueprint('api', __name__)

@api.route('/publish', methods=['POST'])
@login_required
def publish():
    endpoint = session.get('_micropub_endpoint')

    # pass along file uploads, if present
    files = {}
    for file_key in ['audio','photo']:
      if file_key in request.files:
        f = request.files[file_key]
        if f.filename != '':
          # TODO: if media endpoint, upload there and replace value w/ URL
          # otherwise, pass the file along to the micropub endpoint
          files[file_key] = (f.filename, f, f.mimetype)

    # TODO: data validation?

    # iterate over keys to allow multiple values from Flask multidict
    data = {}
    for k in request.form.keys():
      data[k] = request.form.getlist(k)

    headers = { 'Authorization': "Bearer %s" % session.get('_micropub_access_token') }

    r = requests.post(
      endpoint,
      data=data,
      headers=headers,
      files=files
    )

    # check for a 201 or 202 and Location: header for success
    # redirect to Location!
    if (r.status_code == requests.codes.created) or (r.status_code == request.codes.accepted):
      return redirect(r.headers.get('location'))
    else:
      return "Micropub endpoint did not return a Location. %s" % r.text
