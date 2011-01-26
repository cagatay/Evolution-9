from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
import constants
import pickle
import math
from pybrain.auxiliary import GradientDescent
from pybrain.structure import RecurrentNetwork, LinearLayer, SigmoidLayer, FullConnection
import random
from util import rttl
import math

class neural_network(object):
    def __init__(self, name, dataset, trained, store):
        self.name = name
        self.store = store
        self.trained = trained
        self.dataset = dataset

        self.net = RecurrentNetwork()
        self.net.addInputModule(LinearLayer(2, name='in'))
        self.net.addModule(SigmoidLayer(3, name='hidden'))
        self.net.addOutputModule(LinearLayer(2, name='out'))
        self.net.addConnection(FullConnection(self.net['in'], self.net['out'], name='c1'))
        self.net.addConnection(FullConnection(self.net['hidden'], self.net['out'], name='c2'))
        self.net.addRecurrentConnection(FullConnection(self.net['hidden'], self.net['hidden'], name='c3'))
        self.net.sortModules()
        '''
        self.net = buildNetwork(2, 3, 2)
        '''
        if not self.trained:
            self.train()

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
        print result
        return [x for x in result]

    @classmethod
    def new(cls, name, store, ds_file_uri):
        dataset = rttl.dataset_from_file(ds_file_uri)

        store.new_neural_network(name, dataset)
        return

    def evaluate(self, genome):
        err = 0.0
        for i in range(len(genome) - 1):
            print '---------- input ------------'
            print genome[i]
            output = self.net.activate(genome[i])
            print '--------- output ------------'
            print output
            target = genome[i + 1]
            err += (math.fabs(output[0] - target[0]) + math.fabs(output[1] - target[1]))

        return 1/err

    def train(self):
        ds_store = []
        for song in self.dataset:
            ds_in = song[:len(song) - 1]
            ds_out = song[1:]

            ds = SupervisedDataSet(2, 2)

            for i in range(len(song) -1):
                #if ds_in[i] not in ds_store:
                ds.addSample(ds_in[i], ds_out[i])
                ds_store.append(ds_in[i])

            if len(ds):
                trainer = BackpropTrainer(self.net, ds, verbose=True)
                trainer.trainUntilConvergence() 
        self.save()
