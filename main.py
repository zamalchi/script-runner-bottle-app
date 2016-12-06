#!/usr/bin/env python

########################################################################################################
########################################################################################################
########################################################################################################

### IMPORTS ############################################################################################

import os
import sys
import argparse

import modu.bottle as bottle
import modu.slurm as slurm

### APACHE #############################################################################################

os.chdir(os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(__file__))

### ARG PARSING ########################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('-a', help="Host address", action="store", dest="a", required=True)
parser.add_argument('-p', help="Port number", action="store", dest="p", required=True)
parser.add_argument('-d', help="Dev mode", action="store_true", required=False)

args = parser.parse_args()

# GLOBAL ENVIRONMENT VARIABLES
ENV = argparse.Namespace()
ENV.HOST = args.a
ENV.PORT = args.p
ENV.DEV = True if args.d else False
ENV.ROOT = os.path.dirname(os.path.realpath(__file__))

print("ROOT DIR IN MAIN.PY : {}".format(ENV.ROOT))

### FOR CSS READING IN TEMPLATES #######################################################################

bottle.SimpleTemplate.defaults["url"] = bottle.url

### STATIC ROUTING ########################################################################################

# CSS
@bottle.get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='./static/css')

# JAVASCRIPT
@bottle.get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return bottle.static_file(filename, root='./static/js')

# IMAGES
@bottle.get('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='./static/img')

# FONTS
@bottle.get('/fonts/<filename:re:.*\.(eot|ttf|woff|woff2|svg)>')
def fonts(filename):
    return bottle.static_file(filename, root='./static/fonts')

@bottle.error(404)
def error404(error):
    return 'Nothing here, sorry'

### COOKIE GETTERS/SETTERS #############################################################################

# ### ANCHOR ######################################################
# def getAnchorCookie(req):
#     return req.get_cookie("anchor") or "-1"
#
# def setAnchorCookie(res, anchor):
#     res.set_cookie("anchor", str(anchor))
#
# def deleteAnchorCookie(res):
#     res.delete_cookie("anchor")
#
# ### REQUESTED NODE ##############################################
#
# def getRequestedCookie(req):
#     return req.get_cookie("requested") or "-1"
#
# def setRequestedCookie(res, requested):
#     res.set_cookie("requested", str(requested))
#
# def deleteRequestedCookie(res):
#     res.delete_cookie("requested")

########################################################################################################
########################################################################################################
########################################################################################################

#
#
#
# ^^^ FUNCTIONS, SETTINGS ^^^
#
# vvv ROUTES vvv
#
#
#

########################################################################################################
###################################### NODE ROUTES START ###############################################
########################################################################################################

@bottle.get('/slurm')
def slurm_nodes():
    # get and delete anchor cookie
    anchor = bottle.request.cookies.get("anchor", -1)
    bottle.response.delete_cookie("anchor")

    # get and delete requested node cookie
    requested = bottle.request.cookies.get("requested", "")
    bottle.response.delete_cookie("requested")

    # dict of (state --> obj) pairs
    states = slurm.Slurm.getNonEmptyStates()

    # if a specific node was requested
    if requested:
        # get the scontrol info for that node
        node = slurm.Slurm.Node(requested)
    else:
        node = None

    #################################################

    return bottle.template('slurm', anchor=anchor, states=states, node=node)

########################################################################################################
########################################################################################################

@bottle.post('/node')
def scontrol_show_node():
    anchor = bottle.request.forms.get('anchor') or -1
    bottle.response.set_cookie("anchor", anchor)

    requested = bottle.request.forms.get('node') or -1
    bottle.response.set_cookie("requested", requested)

    bottle.redirect('/slurm#' + anchor)


########################################################################################################
########################################################################################################

@bottle.post('/search')
def search_for_node():
    # get requested node and parse out the number
    requested = slurm.Slurm.normalizeNodeName(bottle.request.forms.get('search'))

    # set the cookie to be used in /slurm
    bottle.response.set_cookie("requested", requested)

    bottle.redirect("/slurm")

########################################################################################################
###################################### NODE ROUTES END #################################################
########################################################################################################

bottle.run(host=ENV.HOST, port=ENV.PORT, debug=ENV.DEV)

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
