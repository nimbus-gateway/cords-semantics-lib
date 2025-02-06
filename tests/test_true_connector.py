import unittest
from unittest.mock import patch, MagicMock
from true_connector import TrueConnector

class TestTrueConnector(unittest.TestCase):

    def setUp(self):
        self.connector = TrueConnector("http://example.com", "http://proxyserver.com")
    
    def test_initialization(self):
        """Test if the constructor correctly initializes the object."""
        self.assertEqual(self.connector.connector_url, "http://example.com")
        self.assertEqual(self.connector.connector_proxyurl, "http://proxyserver.com")
    
    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data='{"key": "value"}')
    @patch("json.load")
    def test_create_resource_description_template_success(self, mock_json_load, mock_open):
        """Test successful creation of a resource description template."""
        mock_json_load.return_value = {"key": "value"}
        result = self.connector.create_resource_description_template()
        self.assertEqual(result, {"key": "value"})
    
    @patch("builtins.open", side_effect=FileNotFoundError())
    def test_create_resource_description_template_file_not_found(self, mock_open):
        """Test error handling when the template file is not found."""
        with self.assertRaises(FileNotFoundError):
            self.connector.create_resource_description_template()
    
    @patch("true_connector.TrueConnector.create_resource_description_template")
    def test_create_model_resource_description(self, mock_create_template):
        """Test creation of a model resource description."""
        mock_create_template.return_value = {
            "@id": "",
            "ids:created": {"@value": ""},
            "ids:description": [{"@value": ""}],
            "ids:title": [{"@value": ""}],
            "ids:keyword": [],
            "@context": {},
            "cords:mlmetadata": {}
        }
        description = self.connector.create_model_resource_description(
            "123", "Test Model", "A test model description.", ["AI", "ML"], {"@context": {}, "cords:mlmetadata": {}}
        )
        self.assertIn("Test Model", description["ids:title"][0]["@value"])
    
    @patch("requests.post")
    def test_register_resource(self, mock_post):
        """Test registering a resource and handling different responses."""
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"status": "success"})
        result = self.connector.register_resource({"key": "value"})
        self.assertEqual(result, {"status": "success"})
        
        mock_post.return_value = MagicMock(status_code=404, text="Not found")
        result = self.connector.register_resource({"key": "value"})
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
