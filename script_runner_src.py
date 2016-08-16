if (__name__ == "__main__"):
	print("Run webapp through wrapper.")
	print("Exiting...")
	exit()

### PACKAGES ###########################################################################################

import os
import sys
import commands
import subprocess

### APACHE #############################################################################################

os.chdir(os.path.dirname(__file__))
sys.path.insert(1, os.path.dirname(__file__))

### IMPORTS ############################################################################################

from bottle import Bottle, route, run, request, response, get, post

### HELPER METHODS ##################################################################################### 

def getFileName(scriptName):
	scriptDir = "./scripts/"
	return scriptDir + scriptName

def getHostParam(request):
	return request.query.host or None

def getHTMLHeader():
	return '<body style="font-family: Monospace;">'

def getHTMLFooter():
	return '</body>'

def getHTMLWrapper(html):
	return getHTMLHeader() + str(html) + getHTMLFooter()

def hostNotSuppliedMsg():
	return "Please enter the query parameter: 'host'"

########################################################################################################
########################################################################################################
########################################################################################################

#
#
#
#
#
#
#
#

########################################################################################################
######################################  	NODE ROUTES START	 ###########################################
########################################################################################################

@route('/reinstall')
def reinstall_node():
	host = getHostParam(request)
	if host:
		result = getHTMLWrapper(commands.getstatusoutput(getFileName('reinstall ') + host)[1])
		return result
	
	return hostNotSuppliedMsg()

########################################################################################################
########################################################################################################

@route('/default')
def default_node():
	host = getHostParam(request)
	if host:

		result = getHTMLWrapper(commands.getstatusoutput(getFileName('default ') + host)[1])
		
		return result

	return hostNotSuppliedMsg()

########################################################################################################
########################################################################################################

@route('/slurm')
def slurm_nodes():
	from scripts.states_iterator import *
	
	d = getOutputsDict()

	text = saveOutputsToVar(d)

	#######################################################

	result = "<pre>" + text + "</pre>"

	result = getHTMLWrapper(result)

	return result

########################################################################################################
######################################  	NODE ROUTES END	 #############################################
########################################################################################################
