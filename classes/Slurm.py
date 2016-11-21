
########################################################################################################
########################################################################################################
########################################################################################################

class Slurm:
    # X
    ####################################################################################################
    ### STATIC VARIABLES START
    ####################################################################################################

    states = ['allocated', 'completing', 'down', 'drained', 'draining', 'error', 'fail', 'future', 'idle', 'maint',
              'mixed', 'no_respond', 'npc', 'perfctrs', 'power_down', 'power_up', 'reserved', 'unknown']

    ####################################################################################################
    ### STATIC VARIABLES END
    ####################################################################################################
    # X
    ####################################################################################################
    ### STATIC METHODS START
    ####################################################################################################

    ###### SINFO METHODS

    # used by : Slurm.parseNodeNames
    @staticmethod
    def normalizeNodeName(nodeName):
        # receives a single-node name (ex. 32)
        # returns a string containing the node number (ex. '032')

        nodeName = str(nodeName)

        replace_chars = ['node']
        for c in replace_chars:
            nodeName = nodeName.replace(c, '')

        return nodeName.strip().zfill(3)

    # used by : Slurm.parseStateOutputToList
    @staticmethod
    def parseNodeNames(rawNodeNames):
        # recieves an unparsed string of nodes (ex. "node[018-021, 34, 45-67]")
        # or receives a single node string (ex. "node32")
        # returns a sorted list (of strings) of node names

        parsedNodeNames = []
        replace_chars = ['node', '[', ']']

        for c in replace_chars:
            rawNodeNames = str(rawNodeNames).replace(c, '')

        # may be one or more nodes / ranges at this point
        units = rawNodeNames.split(',')

        # expands any ranges that exist (ex. 018-021)
        for u in units:
            # single node
            if '-' not in u:
                parsedNodeNames.append(Slurm.normalizeNodeName(u))
            # range of nodes
            else:
                start, end = u.split('-')
                for i in range(int(start), int(end) + 1):
                    parsedNodeNames.append(Slurm.normalizeNodeName(i))

        return sorted(parsedNodeNames)

    # used by : Slurm.getSingleStateOutput
    @staticmethod
    def parseStateOutputToList(raw):
        # param raw <str> : raw output from sinfo command
        # return <[ ([str], str, str) | str ]> : a parsed list of output tuples for one state
        # [ ( [nodenames], time, reasons ), ... ]
        # list may also contain a string element, if the line parse was unsuccessful

        parsedList = []

        # for every line in this state
        for line in raw:

            # if there are 3 fields available to parse, continue...
            if len(line.split("\t")) == 3:
                nodes, time, reasons = line.split("\t")

            elif type(line) is list and len(line) == 3:

                nodes, time, reasons = line

                nodes = Slurm.parseNodeNames(nodes)

                parsedList.append((nodes, time, reasons))

            # if there are not 3 fields to parse, append the original line
            else:
                parsedList.append(line)

        return parsedList

    ### ^ PRIVATE | PUBLIC v

    # used by : Slurm.__init__
    @staticmethod
    def getSingleStateOutput(state):
        # FOR PUBLIC USE
        # param state <str> : state name
        # return <[ ([str], str, str) | str ]> : lines of output for state
        # return is passed directly from Slurm.parseStateOutputToList

        from commands import getstatusoutput

        # %E : reasons for state
        # %H : timestamp
        # %N : node list
        output_format = '"%N\t%20H\t%E"'

        # -a : all
        # -h : no header
        # -N : node format
        # -R : list reasons
        # -t : states
        # -o : output format
        cmd = "sinfo -a -h -N -o {0} -R -t {1}".format(output_format, state)

        # getstatusoutput attaches [0] field (return flag?)
        # for each state, get a list of output lines (each line conforms to output_format)
        output = getstatusoutput(cmd)[1].split("\n")

        # modify each line in this state
        # if the line has a long nodelist (length > 35),
        #   it will display the nodelist on a separate line with the other information aligned on the next line
        # if the line has a short nodelist (length <= 35), it will not modify the line
        # output = getModifiedOutput(output)

        return Slurm.parseStateOutputToList(output)

    @staticmethod
    def getNonEmptyStates():
        # FOR PUBLIC USE
        # return <{ str -> Slurm }> : state name --> Slurm object
        # returns only non-empty Slurm objects

        result = {}

        for s in Slurm.states:
            obj = Slurm.State(s)

            if obj.hasEntries():
                result[s] = obj

        return result

    ###### SCONTROL METHODS

    @staticmethod
    def getScontrolShowNode(node):
        # FOR PUBLIC USE
        # param node <str | int> : node name/number
        # return <str> : output from scontrol

        from commands import getstatusoutput

        node = "node" + Slurm.normalizeNodeName(node)

        cmd = "scontrol -a show node {0}".format(node)

        return getstatusoutput(cmd)[1]

    @staticmethod
    def getScontrolShowReservation():
        # FOR PUBLIC USE
        # return <list[Reservation]> : output from scontrol

        from commands import getstatusoutput

        cmd = "scontrol -o show reservation"

        output = getstatusoutput(cmd)[1]

        reservations = []

        for each in output.split("\n"):
            reservations.append(Slurm.Reservation(each))

        return reservations

    ####################################################################################################
    ### STATIC METHODS END
    ####################################################################################################
    # X
    ####################################################################################################
    ### CLASS METHODS / INNER CLASSES START
    ####################################################################################################
    # X
    ### State : INNER CLASS START

    class State:

        @property
        def name(self):
            return self.__name

        @property
        def entries(self):
            return self.__entries

        # used by : Slurm.getNonEmptyStates
        def __init__(self, state, output=None):
            if state.__class__.__name__ == "State":
                self = state
            else:
                if output is not None:
                    raw = output.split("\n")
                else:
                    raw = Slurm.getSingleStateOutput(state)

                entries = []

                for each in raw:
                    entry = Slurm.Entry(each)

                    if entry.nodes:
                        entries.append(entry)

                self.__name = state
                self.__entries = entries

        def findNodeInEntries(self, node):
            # return <int> : index (in self.__entries) where the node is located (or -1 if not found)

            node = Slurm.normalizeNodeName(node)
            i = 0

            for entry in self.entries:
                if node in entry.nodes:
                    return i
                i += 1

            return -1

        def hasEntries(self):
            return bool(self.__entries)

    ### State : INNER CLASS END
    # X
    ### Entry : INNER CLASS START

    class Entry:

        @property
        def nodes(self):
            return self.__nodes

        @property
        def time(self):
            return self.__time

        @property
        def reason(self):
            return self.__reason

        def __init__(self, entry):
            if type(entry) is str:
                entry = entry.split("\t")

            if type(entry) is list and len(entry) == 3:
                self.__nodes, self.__time, self.__reason = entry
            else:
                self.__nodes = []
                self.__time = ""
                self.__reason = ""

    ### Entry : INNER CLASS END
    # X
    ### Reservation : INNER CLASS START
    
    class Reservation:

        @property
        def name(self):
            return self.__name

        @property
        def nodes(self):
            return self.__nodes
        
        @property
        def data(self):
            return self.__data

        @property
        def state(self):
            return self.__state

        def __init__(self, raw):
            if raw.__class__.__name__ == "Reservation":
                self = raw
            else:
                fields = filter(None, raw.split(' '))
                data = {}

                for f in fields:
                    key, val = f.strip().split('=')

                    if key == "ReservationName":
                        self.__name = val

                    elif key == "Nodes":
                        self.__nodes = Slurm.parseNodeNames(val)

                    elif key == "State":
                        self.__state = val

                    else:
                        data[key] = val

                self.__data = data
    
    
    ####################################################################################################
    ### CLASS METHODS / INNER CLASSES END
    ####################################################################################################
    # X
########################################################################################################
########################################################################################################
########################################################################################################
