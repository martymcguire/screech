from flask import Blueprint, request, session
from .auth import login_required
import requests

api = Blueprint('api', __name__)

@api.route('/publish', methods=['POST'])
@login_required
def publish():
    endpoint = session.get('_micropub_endpoint')
    # TODO: some validation
    data = request.form.to_dict()

    data['start'] += " " + data['tzoffset']
    data['end']   += " " + data['tzoffset']

    headers = { 'Authorization': "Bearer %s" % session.get('_micropub_access_token') }

    return "%s" % ((endpoint, data, headers), )

    r = requests.post(
      endpoint,
      data=data,
      headers=headers
    )
    return "WHAT'S UP BUTTERCUP %s" % r.text
