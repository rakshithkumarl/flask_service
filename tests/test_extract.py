import unittest
import requests
import config


class ExtractTestCase(unittest.TestCase):
    URL = config.TEST_URL_EXTRACT

    def test_extract(self):
        files = {'image': open(config.TEST_IMAGE_PATH_1, 'rb')}
        self.response = requests.post(self.URL, files = files)
        self.assertEqual(self.response.status_code, config.SUCCESS_CODE)                      # Testing the status code
        self.assertEqual(self.response.headers["Content-Type"], config.CONTENT_TYPE_JSON)     # Testing the content-type
        self.assertTrue('extracted_text' in self.response.json())                             # Testing the content json 



if __name__ == "__main__":
    unittest.main()