
########################################################################################################
########################################################################################################
########################################################################################################

class Slurm:
    """
    State : getNonEmptyStates() | State(stateName)
    Reservation : getReservations()
    Node : Node(nodeName)
    """
    # X
    ####################################################################################################
    ### STATIC VARIABLES START
    ####################################################################################################

    STATES = ['allocated', 'completing', 'down', 'drained', 'draining', 'error', 'fail', 'future', 'idle', 'maint',
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
        """ PUBLIC & PRIVATE
        Normalizes a node name for use by other methods (ex. 'node034' | 34 --> '034')
        :param nodeName: <int|str> containing the node number
        :return: <str> 3-char normalized node number (filled w/ leading 0s)
        """
        # chars to be removed from nodeName
        REPLACE_CHARS = 'node'

        return str(nodeName).strip().translate(None, REPLACE_CHARS).zfill(3)

    @staticmethod
    def parseNodeNames(rawNodeNames):
        """ PUBLIC & PRIVATE
        Parses Slurm node lists (from `sinfo` and `scontrol` commands)
        :param rawNodeNames: <str> human-readable list of single nodes/ranges of nodes (ex. 'node[34, 45-67]') |
            single node name (ex. 'node034')
        :return: <list[str]> sorted list of normalized nodes (ex. [34, 45, 46, ...], [34])
        """
        REPLACE_CHARS = 'node[]'
        parsedNodeList = []

        # creates list of one or more node (numbers | ranges)
        nodeList = str(rawNodeNames).strip().translate(None, REPLACE_CHARS).split(',')

        # expands any ranges that exist (ex. "018-021")
        for node in nodeList:
            # single node
            if '-' not in node:
                parsedNodeList.append(Slurm.normalizeNodeName(node))
            # range of nodes
            else:
                start, end = node.split('-')
                for i in range(int(start), int(end) + 1):
                    parsedNodeList.append(Slurm.normalizeNodeName(i))

        return sorted(parsedNodeList)

    ###### SLURM METHODS

    @staticmethod
    def getNonEmptyStates():
        """ PUBLIC
        Calls Slurm.State(name) for each state in Slurm.STATES
        :return: <dict[str -> Slurm.State]> dictionary of state names to non-empty (State.hasEntries()) State objects
        """
        result = {}

        for s in Slurm.STATES:
            # Slurm.State constructor makes the `sinfo` call
            obj = Slurm.State(s)

            if obj.hasEntries():
                result[s] = obj

        return result

    @staticmethod
    def getReservations():
        """ PUBLIC
        Calls and parses `scontrol show reservation`
        :return: <list[Slurm.Reservation]> list of Reservation objects
        """
        from commands import getstatusoutput
        cmd = "scontrol -o show reservation"

        output = filter(None, getstatusoutput(cmd)[1].split("\n"))

        return [Slurm.Reservation(each) for each in output]

    ####################################################################################################
    ### STATIC METHODS END
    ####################################################################################################
    # X
    ####################################################################################################
    ### INNER CLASSES START
    ####################################################################################################
    # X
    ### State : INNER CLASS START

    class State:
        """ PUBLIC
        Describes a group of entries which share a common Slurm state
        """
        @property
        def name(self):
            """<str>"""
            return self.__name

        @property
        def entries(self):
            """<list[Slurm.Entry]>"""
            return self.__entries

        def __init__(self, state):
            """ PUBLIC
            Calls `sinfo` on the state name provided and creates a Slurm.State object from the data received
            :param state: <str> state name (all options are in Slurm.STATES)
            """
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
            # for each state, get an output conforming to output_format
            output = filter(None, getstatusoutput(cmd)[1].split("\n"))

            self.__name = str(state)
            self.__entries = [Slurm.Entry(each) for each in output]

        ### CLASS METHODS

        def findNodeInEntries(self, nodeName):
            """ PUBLIC
            Searches a Slurm.State object's entries to see if a specific node is present
            :param nodeName: <str|int> name of node to find
            :return: <int> index of entry containing the node | -1 if not found
            """

            node = Slurm.normalizeNodeName(nodeName)

            i = 0
            for entry in self.entries:
                if node in entry.nodes:
                    return i
                i += 1
            return -1

        def hasEntries(self):
            """ PUBLIC
            Determines if a Slurm.State is empty / devoid of entries
            :return: <bool>
            """
            return bool(self.__entries)

    ### State : INNER CLASS END
    # X
    ### Entry : INNER CLASS START

    class Entry:
        """ PRIVATE-PUBLIC : accessed through a Slurm.State object
        Describes a group of nodes which share a time and reason for being in a Slurm state
        """
        @property
        def nodes(self):
            """<list[str]> : list of nodes numbers which share the same time and reason"""
            return self.__nodes

        @property
        def time(self):
            """<str> : starting time for the nodes being in their current state"""
            return self.__time

        @property
        def reason(self):
            """<str> : reason the nodes are in their current state"""
            return self.__reason

        def __init__(self, entry):
            """ PRIVATE : used by Slurm.State()
            Receives a line of output from `sinfo` on a single Slurm state ; parses data into a Slurm.Entry object
            :param entry: <str> tab-separated string (format: "*nodes*\t*time*\t*reason*")
            """
            nodes, time, reason = entry.split('\t')
            self.__nodes = Slurm.parseNodeNames(nodes)
            self.__time = time.strip()
            self.__reason = reason.strip()

    ### Entry : INNER CLASS END
    # X
    ### Reservation : INNER CLASS START
    
    class Reservation:
        """ PUBLIC
        Describes a Slurm reservation
        """
        @property
        def name(self):
            """<str> : name of the reservation"""
            return self.__name

        @property
        def nodes(self):
            """<list[str]> : list of node numbers under the reservation"""
            return self.__nodes

        @property
        def state(self):
            """<str> : 'ACTIVE'|'INACTIVE'"""
            return self.__state

        @property
        def data(self):
            """<dict[str -> str]> : dictionary of key->vals from the Slurm reservation output"""
            return self.__data

        def __init__(self, raw):
            """ PRIVATE : used by Slurm.getReservations()
            Receives raw data and parses into a Slurm.Reservation object
            :param raw: <str> `scontrol` output about a single reservation
            """
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

                # add all fields to data
                data[key] = val

            self.__data = data

    ### Entry : INNER CLASS END
    # X
    ### Reservation : INNER CLASS START

    class Node:
        """ PUBLIC
        Describes a single Slurm node
        """
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

        def __init__(self, nodeName):
            """ PUBLIC
            Calls `scontrol show node` and parses data into a Slurm.Node object
            :param nodeName: <str|int> name / number of target node
            """
            from commands import getstatusoutput
            node = Slurm.normalizeNodeName(nodeName)

            cmd = "scontrol -a -o show node node{}".format(nodeName)
            output = getstatusoutput(cmd)[1]

            self.__name = node

            if "not found" in output:
                self.__found = False
                self.__state = ""
                self.__data = {}
            else:
                self.__found = True

                data = {}
                fields = ''

                #### PRE-PARSING (for outlying cases)
                if "Reason=" in output:
                    # parse out reason because it can contain spaces and will break splitting on ' '
                    fields, reason = output.split("Reason=")
                    # add reason back into data
                    data["Reason"] = reason
                ####

                # split fields on ' ' and filter empty elements
                fields = filter(None, fields.split(' '))

                for f in fields:
                    key, val = f.strip().split('=')

                    if key == "State":
                        self.__state = val

                    # add all fields to data
                    data[key] = val

                self.__data = data

    ### Node : INNER CLASS END
    # X
    ####################################################################################################
    ### INNER CLASSES END
    ####################################################################################################
    # X
########################################################################################################
########################################################################################################
########################################################################################################
