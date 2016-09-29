#!/usr/bin/python

# iterates through the states, each time calling `sinfo` and saving the output

import commands

# from `sinfo` man pages
states = ['allocated', 'completing', 'down', 'drained', 'draining', 'error', 'fail', 'future', 'idle', 'maint', 'mixed', 'no_respond', 'npc', 'perfctrs', 'power_down', 'power_up', 'reserved', 'unknown']

line_sep_char = '*'
line_sep_num = 90
line_sep = line_sep_char * line_sep_num

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

# TO BE USED INTERNALLY

# returns a list of lists of strings : [[str, str,...], [str, str,...], ...] for each state 
def getOutputs():
    # list of outputs from each state : each element of this list is a list of lines
    outputs = []

    # %E : reasons for state
    # %H : timestamp
    # %N : node list 
    output_format = '"%N\t%20H\t%E"'

    for s in states:

        # -a : all
        # -h : no header
        # -N : node format
        # -R : list reasons
        # -t : states
        # -o : output format
        cmd = "sinfo -a -h -N -o {0} -R -t {1}".format(output_format, s)

        # getstatusoutput attaches [0] field (return flag?)
        # for each state, get a list of output lines (each line conforms to output_format)
        o = commands.getstatusoutput(cmd)[1].split("\n")

        # modify each line in this state
        # if the line has a long nodelist (length > 35), it will display the nodelist on a separate line with the other information aligned on the next line
        # if the line has a short nodelist (length <= 35), it will not modify the line
        o = getModifiedOutput(o)

        # append to main outputs list
        outputs.append(o)

    return outputs

# zips together states and outputs into a dictionary
def getOutputsDict():
    outputs = getOutputs()
    return dict(zip(states, outputs))

# # print all the states with separators
# def printOutputs(outputDict):
#     print(line_sep)
#
#     for s in states:
#
#         # only print if the state is not empty of nodes
#         if outputDict[s] != ['']:
#
#             print(s.upper())
#             for each in outputDict[s]:
#                 print(each)
#             print(line_sep)

# def saveOutputsToVar(outputDict):
#     text = ""
#     text += line_sep + "\n"
#
#     for s in states:
#         if outputDict[s] != ['']:
#             text += s.upper() + "\n"
#             for each in outputDict[s]:
#                 text += each + "\n"
#             text += line_sep + "\n"
#
#     return text

# modifies formatting of each string in a list (the list represents one state) based on the length of each nodelist
def getModifiedOutput(o):
    mod_o = []

    # for every line in this state
    for line in o:

        # if there are 3 fields available to parse, continue...
        if len(line.split("\t")) == 3:

            # parse fields
            nodelist, time, reasons = line.split("\t")

            if len(nodelist) > 35:
                # if the nodelist is long : print entire nodelist and the other info on the next line (aligned correctly)
                # mod_o.append(nodelist + "\n" + "".ljust(35) + "\t{0}\t{1}".format(time, reasons))

                # if the nodelist is long: do not cut it off and print the other data after it (same delimination)
                mod_o.append(nodelist + "\t{0}\t{1}".format(time,reasons))
            else:
                # else : keep original formatting
                mod_o.append(nodelist.ljust(35) + "\t{0}\t{1}".format(time,reasons))

        # if there are not 3 fields to parse, append the original line
        else:
            mod_o.append(line)

    return mod_o

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

# to run from within python
def run():
    d = getOutputsDict()
    printOutputs(d)
    return d

# USER FUNCTIONS

# returns a string formatted for <pre></pre> display
def saveOutputsToVar():
    
    outputsDict = getOutputsDict()

    text = ""
    text += line_sep + "\n"
    
    for s in states:
        
        # only add if the state is not empty of nodes
        if outputsDict[s] != ['']:
            
            text += s.upper() + "\n"
            for each in outputsDict[s]:
                text += each + "\n"
            text += line_sep + "\n"

    return text


# print all the states with separators
def printOutputs():
    print(saveOutputsToVar())


def parseNodeList(nodelist):
    replace_chars = ['node', '[', ']']
    nodes = []

    n = nodelist
    for c in replace_chars:
        n = n.replace(c, '')

    units = n.split(',')
    for u in units:
        if '-' in u:
            start, end = u.split('-')
            for i in range(int(start), int(end)+1):
                nodes.append(i)

        else:
            nodes.append(i)

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

# allows the script to be run from terminal
if (__name__ == "__main__"):
    run()
