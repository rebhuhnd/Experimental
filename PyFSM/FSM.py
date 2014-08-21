class StateMachine:
    ## State Machine data structure for use for various purposes.
    def __init__(self):
        self.si = []
        self.outpt = [];
        self.s0 = []
        self.S = set()
        self.I = set()
        self.O = {}
        self.nsts = {}
        
    def disp(self):
        print "Current State: ", self.si
        print "Current Output: ", self.outpt
        print "Initial State: ", self.s0
        print "Defined States ", self.S
        print "Defined Inputs: \t",self.I
        print "Defined Outputs: \t", self.O
        print "NST's: "
        keys = self.nsts.keys()

        for key in keys:
            print "\t", key, "->", self.nsts[key]
            
    def AddOutput(self,state,outpt):
        # Binds an output signal to a given state.
        self.O[state] = outpt;
        
    def AddNST(self, initState, inpt, nextState):
        # Adds a next state transition function
        self.nsts[(initState, inpt)] = nextState;
        self.S.add(initState);
        self.S.add(nextState);
        self.I.add(inpt);
    def AddANST(self,inpt,nextState):
        # Adds an absolute next state transition function.
        self.nsts[(inpt)] = nextState;
        self.S.add(nextState);
        self.I.add(inpt);
        
    def GenOutput(self):
        # Generates an appropriate output signal for a given state.
        keys = self.O.keys()
        if self.si in keys:
            self.outpt = self.O[self.si];          
        
    def Initialize(self,state):
        self.si = state;
        self.s0 = state;
        self.GenOutput();
        
    def SendInpt(self, inpt):
        keys = self.nsts.keys()
        key = (self.si, inpt)
        if (key in keys):
            self.si = self.nsts[key]
        elif ((inpt) in keys):
            self.si = self.nsts[(inpt)]
        self.GenOutput()
        
    def SendInptString(self, inptString):
        outpts = [self.outpt]
        for inpt in inptString:
            self.SendInpt(inpt)
            outpts.append(self.outpt)
        return outpts
