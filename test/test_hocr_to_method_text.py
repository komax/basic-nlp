import unittest

import hocr_to_method_text as hocr_met

from bs4 import BeautifulSoup


class HOCR2MethodTextTestCase(unittest.TestCase):

    def setUp(self):
        paper_name = "Williams_2011"
        self.hocr_directory = f"~/test_data/{paper_name}/tesseract"

    def test_get_hocr_files_from_directory(self):
        hocr_files = hocr_met.select_hocr_files(self.hocr_directory)
        self.assertIsNotNone(hocr_files)
        for hocr_file in hocr_files:
            self.assertEqual(hocr_file.suffix, '.html')

    def test_generation_soups(self):
        hocr_files = hocr_met.select_hocr_files(self.hocr_directory)
        length = len(hocr_files)
        soups = list(hocr_met.soup_generator(hocr_files, start_page=2))
        self.assertEqual(len(soups), length-2)
        for soup in soups:
            self.assertIsInstance(soup, BeautifulSoup)



if __name__ == '__main__':
    unittest.main()
