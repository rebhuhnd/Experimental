import Turing
import FSM
import random

## Instantiates FSM
fsm = FSM.StateMachine()

## Adds NSTs
fsm.AddNST('stop','change','go')
fsm.AddNST('go','change','slow')
fsm.AddNST('slow','change','stop')

# Adds ANSTs
fsm.AddANST('err','yield')
fsm.AddANST('reset','stop')

## Adds outputs.
fsm.AddOutput('stop',1);
fsm.AddOutput('go',2);
fsm.AddOutput('slow',3);
fsm.AddOutput('yield',666);

## Initializes the Machine
fsm.Initialize('stop')

## Displays helpful stats
fsm.disp()
#ignals = ['change','err','reset'];

#inptstring = []

#for x in xrange(1, 1000):
#    inptstring.append(signals[random.randint(0,len(signals)-1)])
    
#print fsm.SendInptString(inptstring);
#T = Turing.TuringMachine()

#rfsm = FSM.StateMachine()
#for x in xrange(1,1000):
#    rfsm.AddNST(random.randint(1,10),random.randint(1,10),random.randint(1,10))
#for x in xrange(1,1000):
#    rfsm.AddOutput(random.randint(1,10),random.randint(1,10))
#rfsm.Initialize(random.randint(1,10))

#inptstring = []
#rfsm.disp()
#for x in xrange(1, 1000):
#    inptstring.append(random.randint(1,10))
    
#print rfsm.SendInptString(inptstring);


T = Turing.TuringMachine()
q1 = 1;
q2 = 2;
q3 = 3;
q4 = 4;

T.addAction(q1,'_',q2,0,'R');
T.addAction(q2,'_',q3,'_','R');
T.addAction(q3,'_',q4,1,'R');
T.addAction(q4,'_',q1,'_','R');

T.Initialize(q1,0);
T.ProcessK(10)
print T.tape

L = Turing.TuringMachine();
L.addAction('startup','_','cycleup',666,'R');
L.addAction('cycleup','_','runningl',666,'L');
L.addAction('runningl',666,'runningl',3,'R');
L.addAction('runningl','_','power_off',7,'R');
L.Initialize('startup',0);
L.ProcessK(10)
print L.tape
print('Test 3')
N = Turing.TuringMachine();

for x in xrange(0,10):
    N.tape.append(random.randint(1,4))
N.tape.append('_');
    
N.addAction('startup',1,'runningl',1,'L')
N.addAction('startup',2,'runningl',2,'L')
N.addAction('startup',3,'runningl',3,'L')
N.addAction('startup',4,'runningl',4,'L')
N.addAction('startup','_','runningl','BOUND','L')
N.addAction('runningl',1,'runningl',2,'L')
N.addAction('runningl',2,'runningl',3,'L')
N.addAction('runningl',3,'runningl',4,'L')
N.addAction('runningl',4,'runningl',4,'L')
N.addAction('runningl','_','runningr','BOUND','R')
N.addAction('runningr',1,'runningr',2,'R')
N.addAction('runningr',2,'runningr',3,'R')
N.addAction('runningr',3,'runningr',4,'R')
N.addAction('runningr',4,'runningr',4,'R')
N.addAction('runningr','_','runningr','BOUND','S')
N.addAction('runningr','BOUND','stop','BOUND','S')
N.Initialize('startup',5);
N.ProcessK(100)
print N.tape
