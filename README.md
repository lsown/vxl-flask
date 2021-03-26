# vxl-flask
Voxa Flask Template Design

<b>Overview</b>

vxl-flask.py is the backend.

html static pages in templates directory. 

Uses Jinja2. Base template (base.html), with child html pages import from this base structure.

The css & js is in static directory. 

Layout structure uses grid & flex CSS.

Web communication is using websocket.io.

index.html is general multi-pane example of potential use case.
grafana tab is example of iframing grafana. See Voxa OneNote for examples of setting up grafana.
websocket is example code for sending and receiving data from UI to backend flask server.

Grafana user is admin, password is standard voxa-pass.

##Overview##

##Installation & Setup##
1. Set up virtual environment: `python3 -m venv venv`
2. Activate virtual environment: `source venv/bin/activate
3. Install dependencies in virtual environment: `pip install -r requirements.txt`

##Running application##
* For quick start of the development environment with DEBUG=TRUE, can run script: `./flask_run.sh`

##Organization##
* vxl-flask.py : Core WSGI Flask framework code
* folder templates : Contains html pages. Structure uses jinja2 templating, with base.html the core example containing overall structure. Child pages are example code.
* folder static : Contains css, images, and scripts.
