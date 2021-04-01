# vxl-flask
Voxa Flask Template Design

## Overview

This is an example template for rapid construction of a Voxa Device UI. At a minimum, this project uses:
1. Flask WSGI micro-framework - [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
2. Jinja2 for HTML templating - [Jinja2 Documentation](https://jinja2docs.readthedocs.io/en/stable/)
3. HTML5 for structure/content - Flexbox / Grid - [HTML MDN](https://developer.mozilla.org/en-US/docs/Web/HTML)
4. CSS3 for styling - [CSS MDN](https://developer.mozilla.org/en-US/docs/Web/CSS)
5. Websockets for real-time communications between client & server - [flask-socketio](https://flask-socketio.readthedocs.io/en/latest/)

The goal for this UI is:
1. Lightweight with minimal dependencies
2. Allows rapid prototyping and digital control of physical devices 

## Installation & Setup
1. Install at least python3.7 (can check `python3 --version`): `sudo apt install python3.7`
2. Set up virtual environment: `python3 -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies in virtual environment: `pip install -r requirements.txt`
5. Optional - Install local grafana & influxDB [Guide](https://simonhearne.com/2020/pi-influx-grafana/)
6. Optional - Configure grafana & influxDB (work in progress, reference tutorial to be added)
7. Optional - Set up grafana config to allow iFrame access (work in progress, reference tutorial to be added)

## Start Flask Development Environment
* Enter the virtual environment if not already: `source venv/bin/activate`
* For quick start of the development environment with DEBUG=TRUE, can run script: `./flask_run.sh`

## Project Organization
* vxl-flask.py : Core WSGI Flask framework code. We use this as an entry point for starting up the web application.
* Folder templates : Contains html pages. Pages use jinja2 templating, with base.html as the base template upon which all other pages are built.
  * index.html is general multi-panel example of 6-panels with dynamic size scaling.
  * grafana.html is an example for integrating grafana into the UI using iframe. See Voxa OneNote for examples of setting up grafana / iframe. User login is admin & the password is standard voxa pwd. This requires grafana services to be running and serving.
  * websocket.html is an example for setting up a socket between the client and server.
* Folder static : Contains css, images, and scripts.

## General Syntax & Formatting Rules
* CSS: Follow BEM styling conventions for flat hiearchy and ease of maintenance
* HTML: Use templating & stay within the grid / flexbox structure of organizing web pages.
* Javascript: Keep outside script dependencies at a MINIMUM. If needed, maintain a local copy so UI does not break if device is not connected to internet and only on intranet.

### Useful Resources
* CSS code maintenance - [Block Elements & Modifiers](http://getbem.com/introduction/)
* MDN Web Developer - [MDN Web](https://developer.mozilla.org/en-US/docs/Web)

### Reference UI Images
#### Home Tab - Web
![Image of Home - Web UI](https://github.com/lsown/vxl-flask/blob/main/images/WebUI%20-%20Home%201.jpg)
#### Home Tab - Mobile - Media breaks
![Image of Home - Mobile UI](https://github.com/lsown/vxl-flask/blob/main/images/WebUI%20-%20Home%202.jpg)
#### Grafana Tab
![Image of Grafana UI](https://github.com/lsown/vxl-flask/blob/main/images/WebUI%20-%20Grafana.jpg)
#### Websocket Tab
![Image of Websocket UI](https://github.com/lsown/vxl-flask/blob/main/images/WebUI%20-%20Websocket.jpg)
