# vxl-flask
Voxa Flask Template Design

vxl-flask.py is the backend
html static pages in templates directory. Uses Jinja2 base template (base.html). Other html pages import from this base structure.
css & js in static directory. Structure uses grid & flex CSS.

Web communication is using websocket.io.

Dependencies in requirements.txt. Run with a virtual environment for dependencies.
- pip3 install requirements.txt

Run ./run_flask.sh to startup server. This is a development server with DEBUG=TRUE.
