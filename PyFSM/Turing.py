import FSM

class TuringMachine:
    def __init__(self):
        self.tape = ['_'];
        self.idx = 0;
        self.head = [];
        self.stateRegister = [];
        self.actionTable = {};
        self.FSM = FSM.StateMachine();
    def addAction(self, qj, aj, qj1, aj1, dk):
        self.actionTable[(qj, aj)] = (qj1, aj1, dk);
        self.FSM.AddNST(qj, aj, qj1);
        
    def Initialize(self,initState,idx):
        self.stateRegister = initState;
        self.FSM.Initialize(initState);
        self.idx = idx;
        
    def MoveHeadRight(self):
        if self.idx == 0:
            self.tape.insert(0,'_');
        else:
            self.idx = self.idx - 1
    def MoveHeadLeft(self):
        if len(self.tape)==self.idx+1:
            self.tape.append('_');
        self.idx = self.idx+1;

    def Process(self):
        keys = self.actionTable.keys()

        while (self.stateRegister,self.tape[self.idx]) in keys:
            (qj1, aj1, dk) = self.actionTable[(self.stateRegister,self.tape[self.idx])]
            self.tape[self.idx] = aj1;
            self.FSM.SendInpt(self.tape[self.idx])
            self.stateRegister = self.FSM.si;
            if dk is 'R':
                self.MoveHeadRight();
            elif dk is 'L':
                self.MoveHeadLeft();
            elif dk is 'S':
                pass

    def ProcessK(self,numSteps):
        keys = self.actionTable.keys()
        count = 0;
        while count <= numSteps and (self.stateRegister,self.tape[self.idx]) in keys:
            (qj1, aj1, dk) = self.actionTable[(self.stateRegister,self.tape[self.idx])]
            self.FSM.SendInpt(self.tape[self.idx])
            self.tape[self.idx] = aj1;
            self.stateRegister = self.FSM.si;
            if dk is 'R':
                self.MoveHeadRight();
            elif dk is 'L':
                self.MoveHeadLeft();
            print self.tape, self.stateRegister
            count = count + 1;       
