
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

    ###### HELPER METHODS

    @staticmethod
    def normalizeNodeName(nodeName):
        # receives a single-node name (ex. 32)
        # returns a string containing the node number (ex. '032')

        nodeName = str(nodeName)

        replace_chars = ['node']
        for c in replace_chars:
            nodeName = nodeName.replace(c, '')

        return nodeName.strip().zfill(3)

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

    ###### SINFO METHODS

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
    def getReservations():
        # FOR PUBLIC USE
        # return <list[Reservation]> : output from scontrol

        from commands import getstatusoutput

        cmd = "scontrol -o show reservation"

        output = filter(None, getstatusoutput(cmd)[1].split("\n"))

        return [Slurm.Reservation(each) for each in output]

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
        def __init__(self, state):

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
            cmd = "sinfo -a -h -N -o {} -R -t {}".format(output_format, state)

            # getstatusoutput attaches [0] field (return flag?)
            # for each state, get a list of output lines (each line conforms to output_format)
            output = filter(None, getstatusoutput(cmd)[1].split("\n"))

            self.__name = state
            self.__entries = [Slurm.Entry(each) for each in output]

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
            nodes, time, reason = entry.split("\t")
            self.__nodes = Slurm.parseNodeNames(nodes)
            self.__time = time.strip()
            self.__reason = reason.strip()

            # if type(entry) is str:
            #     nodes, time, reason = entry.split("\t")
            #     self.__nodes = Slurm.parseNodeNames(nodes)
            #     self.__time = time.strip()
            #     self.__reason = reason.strip()
            # elif type(entry) is list and len(entry) == 3:
            #     self.__nodes, self.__time, self.__reason = entry
            # else:
            #     self.__nodes = []
            #     self.__time = ""
            #     self.__reason = ""

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
        def state(self):
            return self.__state

        @property
        def data(self):
            return self.__data

        def __init__(self, raw):
            # if raw.__class__.__name__ == "Reservation":
            #     self = raw
            # else:
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

    ### Entry : INNER CLASS END
    # X
    ### Reservation : INNER CLASS START

    class Node:

        @property
        def name(self):
            return self.__name

        @property
        def state(self):
            return self.__state

        @property
        def data(self):
            return self.__data

        @property
        def found(self):
            return self.__found

        def __init__(self, node):
            from commands import getstatusoutput
            nodeName = "node" + Slurm.normalizeNodeName(node)
            cmd = "scontrol -a -o show node {}".format(nodeName)
            output = getstatusoutput(cmd)[1]

            if "not found" in output:
                self.__found = False
                self.__name = nodeName
                self.__state = ""
                self.__data = {}
            else:
                self.__found = True

                data = {}
                fields = ''

                if "Reason=" in output:
                    # parse out reason because it contains spaces and will break splitting on ' '
                    fields, reason = output.split("Reason=")
                    # add reason back into data
                    data["Reason"] = reason

                fields = filter(None, fields.split(' '))

                for f in fields:
                    key, val = f.strip().split('=')

                    if key == "NodeName":
                        self.__name = val

                    elif key == "State":
                        self.__state = val

                    data[key] = val

                self.__data = data

    ####################################################################################################
    ### CLASS METHODS / INNER CLASSES END
    ####################################################################################################
    # X
########################################################################################################
########################################################################################################
########################################################################################################
