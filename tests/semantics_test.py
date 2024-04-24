import unittest
from rdflib import Graph, Namespace, RDF
from rdflib.compare import graph_diff, isomorphic
from ..cords_semantics.semantics import MlSemanticManager 

# Assuming MlSemanticManager is defined in the same file or properly imported
class TestMlSemanticManager(unittest.TestCase):
    def setUp(self):
        self.manager = MlSemanticManager()

    def test_initial_namespace_uris(self):
        """Test initial URIs are correctly set."""
        self.assertEqual(self.manager.cords_namespace_uri, "http://www.w3.org/ns/cordsns#")
        self.assertEqual(self.manager.scenario_uri, "http://example.org#")

    def test_set_cords_namespace_uri(self):
        """Test setting the CORDS namespace URI."""
        new_uri = "http://newcordsnamespace.org#"
        self.manager.set_cords_namespace_uri(new_uri)
        self.assertEqual(self.manager.cords_namespace_uri, new_uri)

    def test_set_scenario_namespace_uri(self):
        """Test setting the scenario namespace URI."""
        new_uri = "http://newscenarionamespace.org#"
        self.manager.set_scenario_namespace_uri(new_uri)
        self.assertEqual(self.manager.scenario_uri, new_uri)

    def test_create_model_semantics(self):
        """Test creating the RDF graph from metadata."""
        meta_data = {'ModelEvaluation': [{'type': 'modelEvaluation_test_MAE', 'specifiedBy': 'test_MAE', 'hasValue': '1.5492494294763557'}, 
                                         {'type': 'modelEvaluation_test_R2_Score', 'specifiedBy': 'test_R2_Score', 'hasValue': '0.858882955307253'}, 
                                         {'type': 'modelEvaluation_test_RMSE', 'specifiedBy': 'test_RMSE', 'hasValue': '2.7181378412972808'}], 
                                         'Implementation': [{'type': 'python'}], 'Run': [{'type': 'c4e20b0629c14dd2bb46780310f3fbeb', 'executes': 'K-Neighbors Regressor'}],
                                           'Software': [{'type': 'sklearn'}]}

        # expected_graph = Graph()
        # cords = Namespace("http://www.w3.org/ns/cordsns#")
        # ex = Namespace("http://example.org#")
        # expected_graph.add((ex['Instance1'], RDF.type, cords['Class']))
        # expected_graph.add((ex['Instance1'], cords['property'], ex['Value1']))
        # expected_graph.add((ex['Instance2'], RDF.type, cords['Class']))
        # expected_graph.add((ex['Instance2'], cords['property'], ex['Value2']))
        # expected_graph.add((ex['Instance2'], cords['property'], ex['Value3']))

        # created_graph = self.manager.create_model_semantics(meta_data)

        # # Check if the created graph is isomorphic to the expected graph
        # self.assertTrue(isomorphic(created_graph, expected_graph))

    # def test_serialize_model_semantics(self):
    #     """Test serialization of RDF graph."""
    #     import os
    #     import tempfile
    #     self.manager.create_model_semantics({'Class': [{'type': 'Instance'}]})  # Create a minimal graph
    #     with tempfile.TemporaryDirectory() as tmpdirname:
    #         file_path = os.path.join(tmpdirname, 'test.rdf')
    #         self.manager.serialize_model_semantics(destination=file_path, form="xml")
    #         self.assertTrue(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main()