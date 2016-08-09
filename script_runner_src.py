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

	HOST = ""
	COMMAND = ""

	try:
		f = open(getFileName("slurm"))

		HOST = f.readline().strip()
		COMMAND = f.readline().strip()

		f.close()

	except IOError:
		return "/slurm command file not found."

	#######################################################

	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

	output = ssh.stdout.readlines()
	
	#######################################################

	result = ""

	for line in output:
		if "===" in line:
			result += "<h3>" + line + "</h3>"
		else:
			result += "<p>" + line + "</p>"

	result = getHTMLWrapper(result)

	return result

########################################################################################################
######################################  	NODE ROUTES END	 #############################################
########################################################################################################
