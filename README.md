Screech (has moved)
===================

Screech is a [micropub](https://www.w3.org/TR/micropub/) client for posting
audio content (such as podcasts) to your website.

It's been reworked from Python to PHP and the new source lives at: https://git.schmarty.net/schmarty/screech-php

As of 2023, Screech can be found at: https://screech.bayside.pub/

This repository has been archived due to security updates for Flask that I don't intend to apply, as I'm no longer maintaining this version of Screech.

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
