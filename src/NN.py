from pybrain.tools.shortcuts import buildNetwork
from mingus.containers import *
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import constants
import pickle

 
class NN:
    name = ""
    net = buildNetwork(1, 1, 1)
    inputCount = 1
    outputCount = 1
    
    
    def __init__(self, _name, _inputCount, _outputCount):
        self.name= _name
        self.inputCount = _inputCount
        self.outputCount = _outputCount
        self.net = buildNetwork(self.inputCount, 6, self.outputCount)
        
    def saveNetworkToFile(self):
        pickle.dump(self.net, open(constants.SAVE_DIR + self.name + "-" 
                    + str(self.inputCount) + "-" + str(self.outputCount), "w" ) )
        
    def readNetworkFromFile(self):
        self.net = pickle.load( self.net, open(constants.SAVE_DIR + self.name + "-" 
                                               + str(self.inputCount) + "-" + str(self.outputCount), "r" ) )

        
    def train(self, song):
        currentNoteInt = 0
        currentDuration = 0
        currentNote = Note()
       
        song.intList = list()
        for note in song.notes:
            if not note[1]:
                currentNote = None
                currentNoteInt = 0
                currentDuration = note[0]
            else:
                currentNote = Note(note[1], note[2])
                currentNoteInt = int(Note(note[1], note[2]))
                currentDuration = note[0]
                
            insertedDuration = 0
            while insertedDuration < currentDuration:
                song.intList.append(currentNoteInt)
                insertedDuration += 2
           
        
        #prepare dataset
        ds = SupervisedDataSet(self.inputCount, self.outputCount)
        
      
        
        
        i = 0
        z = 0
        
        for intNote in song.intList:
            
            if i + self.inputCount >= len( song.intList ):
                break
            
            sampleList = list()
            sampleOutputList = list()
            
            for j in range( 0, self.inputCount + 1 ):
                    
                if j % self.inputCount == 0 and len( sampleList ) == self.inputCount :
                   
                    
                    if( j + i + self.outputCount < len( song.intList ) ):
                        
                        for z in range( j + i , j + i + self.outputCount ):
                            sampleOutputList.append( song.intList[ z ] )
                        
                        ds.addSample( sampleList, sampleOutputList )
                        
                    sampleList = list()
                    sampleOutputList = list()
                    
                else:
                    sampleList.append( song.intList[ j + i ] )    
            
            i += 1
    
        trainer = BackpropTrainer(self.net, ds, verbose=True)
        for i in range(0,5):
            trainer.trainEpochs(1)
            print '\tvalue after %d epochs: %.2f %.2f'%(i, self.net.activate((64, 64, 64))[0], self.net.activate((64, 64, 64))[1])
            
def fitness(self, song):
    return 10 