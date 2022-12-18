import unittest
import requests
import config


class TranslateTestCase(unittest.TestCase):
    URL = config.TEST_URL_TRANSLATE

    def test_translate(self):
        files = {'image': open(config.TEST_IMAGE_PATH_2, 'rb')}
        payload = {'translation_language': config.TEST_TRANSLATION_LANGUAGE}
        self.response = requests.post(self.URL, files = files, data = payload)
        self.assertEqual(self.response.status_code, config.SUCCESS_CODE)                      # Testing the status code
        self.assertEqual(self.response.headers["Content-Type"], config.CONTENT_TYPE_JSON)     # Testing the content-type
        self.assertTrue('extracted_text' in self.response.json())                             # Testing the content json 
        self.assertTrue('translated_text' in self.response.json())



if __name__ == "__main__":
    unittest.main()