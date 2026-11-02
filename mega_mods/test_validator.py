import copy
import json
import unittest
from pathlib import Path
from validate_manifest import validate

class ManifestValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.good = json.loads((Path(__file__).parent / "vehicle-manifest.example.json").read_text())

    def test_example_is_valid(self):
        self.assertEqual(validate(self.good), [])

    def test_rejects_traversal(self):
        bad = copy.deepcopy(self.good)
        bad["files"][0]["path"] = "../private/secret"
        self.assertTrue(validate(bad))

    def test_rejects_bad_type(self):
        bad = copy.deepcopy(self.good)
        bad["installType"] = "unknown"
        self.assertTrue(validate(bad))

if __name__ == "__main__":
    unittest.main()
