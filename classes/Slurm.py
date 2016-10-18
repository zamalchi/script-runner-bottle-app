
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

    @staticmethod
    def normalizeNodeName(nodeName):
        # receives a single-node name (ex. 'node032')
        # returns a string containing the node number (ex. '032')

        nodeName = str(nodeName)

        replace_chars = ['node']
        for c in replace_chars:
            nodeName = nodeName.replace(c, '')

        return nodeName.strip().zfill(3)

    @staticmethod
    def parseNodeNames(rawNodeNames):
        # recieves an unparsed string of nodes (ex. node[018-021, 34, 45-67])
        # returns a sorted list (of strings) of normalized node names

        parsedNodeNames = []

        replace_chars = ['node', '[', ']']
        for c in replace_chars:
            rawNodeNames = rawNodeNames.replace(c, '')

        units = rawNodeNames.split(',')

        # expands any ranges that exist (ex. 018-021)
        for u in units:
            # single node
            if '-' not in u:
                Slurm.normalizeNodeName()
            # range of nodes
            else:
                start, end = u.split('-')
                for i in range(int(start), int(end) + 1):
                    Slurm.normalizeNodeName(i)

        return sorted(parsedNodeNames)

    @staticmethod
    def getNonEmptyStates():
        result = {}
        for s in Slurm.states:
            obj = Slurm(s)
            if obj.hasNodes():
                result[s] = obj
        return result



    ####################################################################################################
    ### STATIC METHODS END
    ####################################################################################################
    # X
    ####################################################################################################
    ### CLASS METHODS START
    ####################################################################################################

    def getEntry(self, entryIndex):
        if type(entryIndex) is int and entryIndex < len(self.parsed_entries):
            return self.parsed_entries[entryIndex]
        else:
            return None

    def findNodeIndex(self, nodeNumber):
        i = 0
        for entry in self.parsed_entries:
            if str(nodeNumber).strip().zfill(3) in entry[0]:
                return i
            i += 1
        return -1

    def hasNodes(self):
        return bool(self.parsed_entries)

    def __init__(self, state):

        from scripts.states_iterator import getSingleStateOutput
        from pickle import load

        self.state = state

        # self.raw_entries = getSingleStateOutput(state)
        self.raw_entries = load(open('local_example.p', 'rb'))[state]

        self.parsed_entries = []

        if type(self.raw_entries) is list:

            for each in self.raw_entries:
                entry = each.split("\t")

                if len(entry) == 3:
                    names, time, reason = entry

                    self.parsed_entries.append([Slurm.parseNames(names), time, reason])

    ####################################################################################################
    ### CLASS METHODS END
    ####################################################################################################
    # X
########################################################################################################
########################################################################################################
########################################################################################################
