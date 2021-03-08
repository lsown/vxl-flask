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

Dependencies in requirements.txt. Run with a virtual environment for dependencies (setup Venv, install dependencies, and activate)
- *some command for setting up venv
- pip3 install -r requirements.txt
- source venv/bin/activate

Run ./run_flask.sh to startup server. This is a development server with DEBUG=TRUE.
