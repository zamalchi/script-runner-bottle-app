#!/usr/bin/env python

########################################################################################################
########################################################################################################
########################################################################################################

### IMPORTS ############################################################################################

from __future__ import print_function
import os
import sys
import argparse

import modu.bottle as bottle
import modu.slurm as slurm
import modu.color_printer as cp

app = bottle.Bottle()

### ARG PARSING ########################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('-a', help="Host address", action="store", dest="a", required=True)
parser.add_argument('-p', help="Port number", action="store", dest="p", required=True)
parser.add_argument('-d', help="Dev mode", action="store_true", required=False)
parser.add_argument('-r', help="Live reloading", action="store_true", required=False)

args = parser.parse_args()

# GLOBAL ENVIRONMENT VARIABLES
ENV = argparse.Namespace()
ENV.HOST = args.a
ENV.PORT = args.p
ENV.DEBUG = True if args.d else False
ENV.RELOAD = True if args.r else False
ENV.ROOT = os.path.dirname(os.path.realpath(__file__))

### APACHE #############################################################################################

os.chdir(ENV.ROOT)
sys.path.insert(1, ENV.ROOT)

### FOR CSS READING IN TEMPLATES #######################################################################

bottle.SimpleTemplate.defaults["url"] = bottle.url

### STATIC ROUTING ########################################################################################

# CSS
@app.get('/css/<filename:re:.*\.css(.map)?>')
def stylesheets(filename):
    return bottle.static_file(filename, root='static/css')

# JAVASCRIPT
@app.get('/js/<filename:re:.*\.js(.map)?>')
def javascripts(filename):
    return bottle.static_file(filename, root='static/js')

# IMAGES
@app.get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='static/img')

# FONTS
@app.get('/fonts/<filename:re:.*\.(eot|ttf|woff|woff2|svg)>')
def fonts(filename):
    return bottle.static_file(filename, root='static/fonts')

@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

########################################################################################################
########################################################################################################
########################################################################################################
#
# ^^^ FUNCTIONS, SETTINGS ^^^
#
# vvv ROUTES vvv
#
########################################################################################################
##################################### SLURM ROUTES START ###############################################
########################################################################################################

@app.get('/')
@app.get('/slurm')
def slurm_nodes():
    # get and delete anchor cookie
    anchor = bottle.request.cookies.get("anchor", -1)
    bottle.response.delete_cookie("anchor")

    # get and delete requested node cookie
    requested = bottle.request.cookies.get("requested", "")
    bottle.response.delete_cookie("requested")

    # dict of (state --> obj) pairs
    states = slurm.Slurm.getNonEmptyStates()

    # if a specific node was requested, get the scontrol info for that node
    node = slurm.Slurm.Node(requested)

    #################################################

    return bottle.template('slurm', anchor=anchor, states=states, node=node)

########################################################################################################
########################################################################################################

@app.post('/node')
def scontrol_show_node():
    anchor = bottle.request.forms.get('anchor') or -1
    bottle.response.set_cookie("anchor", anchor)

    requested = bottle.request.forms.get('node') or -1
    bottle.response.set_cookie("requested", str(requested))

    bottle.redirect('/slurm#' + anchor)


########################################################################################################
########################################################################################################

@app.post('/search')
def search_for_node():
    # get requested node and parse out the number
    requested = slurm.Slurm.normalizeNodeName(bottle.request.forms.get('search'))

    # set the cookie to be used in /slurm
    bottle.response.set_cookie("requested", str(requested))

    bottle.redirect("/slurm")

########################################################################################################
##################################### SLURM ROUTES END #################################################
########################################################################################################

border = "* * * * * * * * * * * * * * * * * * * * * * * * * * * "

cp.printHeader(border)

print("APP RUNNING FROM : {project_dir}".format(project_dir=ENV.ROOT))
print("HOST ADDRESS     : {hostAddr}".format(hostAddr=ENV.HOST))
print("HOST PORT        : {hostPort}".format(hostPort=ENV.PORT))

debug = "DEBUG            : {devMode}".format(devMode=ENV.DEBUG)
reloader = "LIVE RELOAD      : {liveReload}".format(liveReload=ENV.RELOAD)

cp.printOK(debug) if ENV.DEBUG else print(debug)
cp.printOK(reloader) if ENV.RELOAD else print(reloader)

cp.printHeader(border)

if ENV.DEBUG:
    app.TEMPLATES.clear()
    print("CLEARED CACHE??")

app.run(host=ENV.HOST, port=ENV.PORT, debug=ENV.DEBUG, reloader=ENV.RELOAD)

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
