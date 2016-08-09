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

def getHostParam(request):
	return request.query.host or None

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
		result = commands.getstatusoutput('./scripts/reinstall ' + host)
		return result
	
	return hostNotSuppliedMsg()

########################################################################################################
########################################################################################################

@route('/default')
def default_node():
	host = getHostParam(request)
	if host:
		result = commands.getstatusoutput('./scripts/default ' + host)
		return result

	return hostNotSuppliedMsg()

########################################################################################################
########################################################################################################

@route('/slurm')
def slurm_node():
	HOST = "eofe1.mit.edu"
	COMMAND = "/cm/shared/admin/bin/slurm-daily-node-status -t"
	
	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

	result = ssh.stdout.readlines()
	#result = commands.getstatusoutput('./scripts/slurm')
	
	res = ""

	for r in result:
		if "===" in r:
			res += "<h3>" + r + "</h3>"
		else:
			res += "<p>" + r + "</p>"

	return res

########################################################################################################
######################################  	NODE ROUTES END	 #############################################
########################################################################################################
