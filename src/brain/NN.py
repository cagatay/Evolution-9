from pybrain.tools.shortcuts import buildNetwork
from mingus.containers.Note import Note
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import constants
import pickle
import math
import random
from util import rttl

class neural_network(object):
    def __init__(self, name, dataset, trained, store):
        self.name = name
        self.store = store
        self.trained = True
        self.dataset = dataset

        return

    def save(self):
        self.store.save_neural_network(self.name, self.dataset, self.trained)
        return

    @classmethod
    def get_saved(cls, name, store):
        result = store.get_neural_network(name)

        return cls(name, result[0], result[1], store) if result else None

    @classmethod
    def get_list(cls, store):
        result = store.get_neural_network_list()
        
        return [x for x in result]

    @classmethod
    def new(cls, name, store, ds_file_uri):
        dataset = rttl.dataset_from_file(ds_file_uri)

        store.new_neural_network(name, dataset)
        return

    def evaluate(self, genome):
        return random.random()

    def train(self):
        self.save()

'''
class NN:
    name = ""
    net = buildNetwork(1, 1, 1)
    inputCount = 1
    outputCount = 1
    hiddenLayerNodeCount = 20
    durationPerNote = 2;
    ds = SupervisedDataSet(inputCount, outputCount)
    
    
    def __init__(self, _name, _inputCount, _outputCount, _durationPerNote = 2):
        self.name= _name
        self.inputCount = _inputCount
        self.outputCount = _outputCount
        self.durationPerNote = _durationPerNote
        self.net = buildNetwork(self.inputCount, self.hiddenLayerNodeCount, self.outputCount)
        self.ds = SupervisedDataSet(self.inputCount, self.outputCount)
        
    def saveNetworkToFile(self):
        pickle.dump(self.net, open(constants.SAVE_DIR + self.name + "-" 
                    + str(self.inputCount) + "-" + str(self.outputCount), "w" ) )
        
    def readNetworkFromFile(self):
        self.net = pickle.load( open(constants.SAVE_DIR + self.name + "-" 
                                               + str(self.inputCount) + "-" + str(self.outputCount), "r" ) )

    def train(self):
        trainer = BackpropTrainer(self.net, self.ds, verbose=True)

        trainer.trainUntilConvergence()
#        for i in range(0,5000):
#            trainer.trainEpochs(1)
#            print '\tvalue after %d epochs: %.2f'%(i, self.net.activate((64, 4, 64))[0])
#            trainer.trainEpochs(1)
#            print '\tvalue after %d epochs: %.2f'%(i, self.net.activate((64, 64, 64))[0])
#            
        
    
    def addSong(self, song):
             
        song = self.attachIntList( song )
        
        
             
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
                            #sampleOutputList.append( song.intList[ z ] )
                            sampleOutputList.append( 1 )
                        
                        self.ds.addSample( sampleList, sampleOutputList )
                        
                    sampleList = list()
                    sampleOutputList = list()
                    
                else:
                    sampleList.append( song.intList[ j + i ] )    
            
            i += 1
    
        
            
    def attachIntList(self, song):
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
        return song


    def fitness(self, song):
        
        returnValue = 0.0
        
        song = self.attachIntList( song )
                
        i = 0
        z = 0
        
        for intNote in song.intList:
            
            if i + self.inputCount >= len( song.intList ):
                break
            
            sampleList = list()
            
            for j in range( 0, self.inputCount + 1 ):
                    
                if j % self.inputCount == 0 and len( sampleList ) == self.inputCount :
                   
                    
                    if( j + i + self.outputCount < len( song.intList ) ):
                        
                        for z in range( j + i , j + i + self.outputCount ):
                            returnValue += math.fabs( self.net.activate( sampleList )[0] - 1)
                        
                    sampleList = list()
                    
                else:
                    sampleList.append( song.intList[ j + i ] )    
            
            i += 1
    
    
        return returnValue 
'''
