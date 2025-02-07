import unittest
from rdflib import Graph, Namespace, RDF
from rdflib.compare import graph_diff, isomorphic
from cords_semantics.semantics import MlSemanticManager, FlSemanticManager
from cords_semantics.mlflow import convert_tags_to_dictionary
import json

tags = [{
    "cords.FLSession.sessionID": "12345",
    "cords.FLSession.sessionStartTime": "2024-01-30T12:00:00Z",
    "cords.FLSession.sessionEndTime": "2024-01-30T15:00:00Z",
    "cords.FLSession.numMinClients": 5,
    "cords.FLSession.numMaxClients": 100,
    "cords.FLSession.participationRatio": 1,
    
    "cords.FLAggregation.aggregationAlgorithm": "fed_avg",
    "cords.FLAggregation.aggregationFrequency": 10,
    
    "cords.FLCommunication.communicationProtocol": "grpc",
    "cords.FLCommunication.secureAggregationEnabled": True,
    
    "cords.FLSecurity.differentialPrivacyEnabled": False,
    "cords.FLSecurity.encryptionMethod": "aes_256",
    
    "cords.FLTraining.trainingRounds": 50,
    "cords.FLTraining.localEpochs": 5,
    "cords.FLTraining.lossFunction": "categorical_crossentropy"
}]


# tags1 =  [{'cords.ModelEvaluation': 'modelEvaluation_loss', 'cords.ModelEvaluation.specifiedBy': 'loss', 'cords.ModelEvaluation.hasValue': '0.0010636363664562006'}, {'cords.ModelEvaluation': 'modelEvaluation_mae', 'cords.ModelEvaluation.specifiedBy': 'mae', 'cords.ModelEvaluation.hasValue': '0.0046593861042960065'}, {'cords.Implementation': 'python', 'cords.Model.hasHyperParameter': 'Adam (\nParameter Group 0\n    amsgrad: False\n    betas: (0.9, 0.999)\n    capturable: False\n    differentiable: False\n    eps: 1e-08\n    foreach: None\n    fused: None\n    lr: 0.003\n    maximize: False\n    weight_decay: 0\n)', 'cords.Run': 'ded583e180134bbc8567b8ee644560a6', 'cords.Run.executes': 'LSTM', 'cords.Software': 'pytorch'}]

# MLmanager = MlSemanticManager("data/cordsml.rdf")
# tags_dictionary = convert_tags_to_dictionary(tags1)
# print(tags_dictionary)
# semantic_graph = MLmanager.create_model_semantics(tags_dictionary)
# jsonld_output = MLmanager.convert_to_json_ld()
# print(jsonld_output)


print("\n\n\n\n")


FLmanager = FlSemanticManager("data/cords_federated_learning.rdf")
tags_dictionary = convert_tags_to_dictionary(tags)

semantics = FLmanager.create_fl_semantics(tags_dictionary)

print(semantics)
# semantic_graph = FLmanager.create_model_semantics(tags_dictionary)
# jsonld_output = FLmanager.convert_to_json_ld()
# print(jsonld_output)
