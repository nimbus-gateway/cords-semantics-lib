import unittest
from rdflib import Graph, Namespace, RDF
from rdflib.compare import graph_diff, isomorphic
from cords_semantics_local.semantics import MlSemanticManager 
from cords_semantics_local.mlflow import convert_tags_to_dictionary
import json






tags = [{
    "cords.FLSession": "1",
    "cords.FLSession.sessionId": "12345",
    "cords.FLSession.sessionStartTime": "2024-01-30T12:00:00Z",
    "cords.FLSession.sessionEndTime": "2024-01-30T15:00:00Z",
    "cords.FLSession.numMinClients": 5,
    "cords.FLSession.numMaxClients": 100,
    "cords.FLSession.participationRatio": 1,
    
    "cords.FLAggregation": "2",
    "cords.FLAggregation.aggregationMethod": "fed_avg",
    "cords.FLAggregation.aggregationFrequency": 10,
    
    "cords.FLCommunication": "3",
    "cords.FLCommunication.communicationProtocol": "grpc",
    "cords.FLCommunication.secureAggregationEnabled": True,
    
    "cords.FLSecurity": "4",
    "cords.FLSecurity.differentialPrivacyEnabled": False,
    "cords.FLSecurity.encryptionMethod": "aes_256",
    
    "cords.FLTraining": "5",
    "cords.FLTraining.trainingRounds": 50,
    "cords.FLTraining.localEpochs": 5,
    "cords.FLTraining.lossFunction": "categorical_crossentropy"
}]

import importlib
importlib.reload(MlSemanticManager )

manager = MlSemanticManager("data/cords_federated_learning.rdf")
tags_dictionary = convert_tags_to_dictionary(tags)

# semantic_graph = manager.create_model_semantics(tags_dictionary)

# print(tags_dictionary)

# output = manager.create_model_semantics(payload)


