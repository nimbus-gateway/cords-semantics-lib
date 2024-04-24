from rdflib import Graph, Namespace
from rdflib.namespace import RDF
from urllib.parse import urlparse
import importlib.resources

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

    def __init__(self, ontology_path) -> None:
        """
        Initializes the MlSemanticManager with default namespace URIs.
        """
        self.cords_namespace_uri = "http://www.w3.org/ns/cordsns#"
        self.scenario_uri = "http://example.org#"
        self.semantic_graph = None
        self.ontology_graph = None
        self.ontology_path = ontology_path
        

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

    def is_url(self, string):
        """
        Check if a string is a valid URL.
    
        Args:
        string (str): The string to check.
    
        Returns:
        bool: True if the string is a valid URL, False otherwise.
        """
        try:
            result = urlparse(string)
            # Check if the parsing is successful and if scheme and netloc are present
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    # Function to find a term's URI in the graph
    def _find_term_uri(self, term):
        graph = Graph()

        # Load the RDF file into the graph
        try:
            graph.parse(self.ontology_path, format='application/rdf+xml')  # Adjust the format if necessary
            
        except Exception as e:
            print('Exception Occurred During Parsing')
            print(e)
        
        for s, p, o in graph:
            if term in s:
                if self.is_url(s):
                    return s
                else:
                    # this is a work around for not to cause any issues. 
                    return self.cords_namespace_uri + term
            elif term in o:
                return o
        return None

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
                        uri = self._find_term_uri(cls)
                        g.add((ex[item[key]], RDF.type, uri))
                    else:
                        if isinstance(item[key], list):
                            for value in item[key]:
                                uri = self._find_term_uri(key)
                                g.add((ex[identifier], uri, ex[value]))
                        else:
                            uri = self._find_term_uri(key)
                            g.add((ex[identifier], uri, ex[item[key]]))

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
        