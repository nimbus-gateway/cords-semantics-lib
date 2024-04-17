from rdflib import Graph, Namespace
from rdflib.namespace import RDF

#example meta data
# meta_data = {
#     "Run": [{
#         "type": "acfad45eafa44f7bb31221fb48689cba",
#         "executes": "wekaLogistic",
#         "hasInput": ["credit-a", "wekaLogisticMSetting29", "wekaLogisticRSetting29"],
#         "hasOutput": ["modelEvaluation100241", "wekaLogisticModel100241"],
#         "realizes": "logisticRegression",
#         "archives": "taks29",
#     }],
#     "Implementation": [{"type": "wekaLogistic"}],
#     "Software": [{"type": "weka"}],
#     "Algorithm": [{"type": "logisticRegression"}],
#     "HyperParameter": [{"type": "wekaLogisticC"}],
#     "ModelEvaluation": [{
#                          "type": "modelEvaluation100241",
#                          "specifiedBy": "predictiveAccuracy",
#                          "hasValue": "0.8478"
#                         }]
# }


class MlSemanticManager:
    """
    A manager class for handling ML semantic models using RDF data.
    """

    def __init__(self) -> None:
        """
        Initializes the MlSemanticManager with default namespace URIs.
        """
        self.cords_namespace_uri = "http://www.w3.org/ns/cordsns#"
        self.scenario_uri = "http://example.org#"
        self.semantic_graph = None

    def set_cords_namespace_uri(self, uri: str):
        """
        Sets the CORDS namespace URI used in the RDF graph.
        
        Parameters:
            uri (str): The URI to set as the CORDS namespace.
        """
        self.cords_namespace_uri = uri

    def set_scenario_namespace_uri(self, uri: str):
        """
        Sets the scenario namespace URI used in the RDF graph.
        
        Parameters:
            uri (str): The URI to set as the scenario namespace.
        """
        self.scenario_uri = uri

    def create_model_semantics(self, meta_data: dict) -> Graph:
        """
        Creates an RDF graph based on the provided metadata.
        
        Parameters:
            meta_data (dict): A dictionary containing metadata with classes and properties.
        
        Returns:
            Graph: An RDF graph representing the model semantics.
        """
        g = Graph()

        # Namespace definitions
        cords = Namespace(self.cords_namespace_uri)
        ex = Namespace(self.scenario_uri)

        for cls in meta_data:
            for item in meta_data[cls]:
                identifier = None  # Ensure identifier is defined in case the first key isn't 'type'
                for key in item:
                    if key == 'type':
                        identifier = item[key]
                        g.add((ex[item[key]], RDF.type, cords[cls]))
                    else:
                        if isinstance(item[key], list):
                            for value in item[key]:
                                g.add((ex[identifier], cords[key], ex[value]))
                        else:
                            g.add((ex[identifier], cords[key], ex[item[key]]))

        self.semantic_graph = g
        return g

    def serialize_model_semantics(self, destination: str, form: str = "xml"):
        """
        Serializes the RDF graph to a file in the specified format.
        
        Parameters:
            destination (str): The path to the file where the RDF graph will be serialized.
            form (str): The serialization format (e.g., 'xml', 'turtle').
        """
        self.semantic_graph.serialize(destination=destination, format=form)
