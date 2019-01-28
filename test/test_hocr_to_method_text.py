import unittest

import hocr_to_method_text as hocr_met


class HOCR2MethodTextTestCase(unittest.TestCase):

    def setUp(self):
        paper_name = "Williams_2011"
        self.hocr_directory = f"~/test_data/{paper_name}/tesseract"

    def test_get_hocr_files_from_directory(self):
        print(self.hocr_directory)
        hocr_files = hocr_met.select_hocr_files(self.hocr_directory)
        print(hocr_files)
        self.assertIsNotNone(hocr_files)


if __name__ == '__main__':
    unittest.main()
