Screech
=======

Screech is a [micropub](https://www.w3.org/TR/micropub/) client for posting
audio content (such as podcasts) to your website.

Quick (&amp; Dirty) Start
-------------------------

Create and activate a virtualenv:

	virtualenv --python=/usr/bin/python3 venv
	source venv/bin/activate

or conda:

	conda create -n screech python=3.5
	source activate screech

Install required Python libraries

	pip install -r requirements.txt

Run the dev server

	python run.py

View the app in your browser at `http://localhost:5000`.

TODOs
-----

So many.

* Support for syndication links from silos
* Support for mp-syndicate-to via micropub config or syndication-to query
* Support for micropub media endpoint for audio, photo (as a poster for the audio)
  * upload it
  * replace file field with hidden field w/ Location: URL returned by mp media endpoint
* CORS issues? Use a proxy?
