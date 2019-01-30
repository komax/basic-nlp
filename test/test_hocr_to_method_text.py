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

    def test_areas_to_text_generates_a_str(self):
        soup = BeautifulSoup("""
        <div class="ocr_page" id="page_1" title='image "/foobar.png"; bbox 0 0 4961 6591; ppageno 0'>
        <div class="ocr_carea" id="block_1_7" title="bbox 2552 5270 4531 5759" ts:table-score="2" ts:type="other">
<p class="ocr_par" id="par_1_10" lang="eng" title="bbox 2552 5270 4531 5759">
<span class="ocr_line" id="line_1_102" title="bbox 2552 5270 2858 5327; baseline 0.003 -1; x_size 74.650894; x_descenders 17.650898; x_ascenders 17"><span class="ocrx_word" id="word_1_824" title="bbox 2552 5270 2858 5327; x_wconf 91">Methods</span>
</span>
<span class="ocr_line" id="line_1_103" title="bbox 2555 5478 2912 5552; baseline 0 -17; x_size 74; x_descenders 17; x_ascenders 18"><span class="ocrx_word" id="word_1_825" title="bbox 2555 5478 2742 5552; x_wconf 92">Study</span> <span class="ocrx_word" id="word_1_826" title="bbox 2776 5496 2912 5535; x_wconf 98">area</span>
</span>
<span class="ocr_line" id="line_1_104" title="bbox 2552 5684 4531 5759; baseline 0 -17; x_size 75; x_descenders 17; x_ascenders 19"><span class="ocrx_word" id="word_1_827" title="bbox 2552 5685 2679 5742; x_wconf 99">The</span> <span class="ocrx_word" id="word_1_828" title="bbox 2711 5685 2898 5742; x_wconf 98">urban</span> <span class="ocrx_word" id="word_1_829" title="bbox 2933 5703 3068 5742; x_wconf 98">area</span> <span class="ocrx_word" id="word_1_830" title="bbox 3101 5684 3172 5742; x_wconf 88">of</span> <span class="ocrx_word" id="word_1_831" title="bbox 3198 5685 3297 5742; x_wconf 99">the</span> <span class="ocrx_word" id="word_1_832" title="bbox 3330 5685 3503 5742; x_wconf 92">Perth</span> <span class="ocrx_word" id="word_1_833" title="bbox 3535 5684 3960 5759; x_wconf 90">metropolitan</span> <span class="ocrx_word" id="word_1_834" title="bbox 3991 5684 4202 5759; x_wconf 85">region</span> <span class="ocrx_word" id="word_1_835" title="bbox 4234 5684 4296 5741; x_wconf 99">in</span> <span class="ocrx_word" id="word_1_836" title="bbox 4331 5685 4531 5742; x_wconf 99">south—</span>
</span>
</p>
</div>
<div class="ocr_carea" id="block_1_8" title="bbox 2552 5788 4535 5967" ts:table-score="1" ts:type="text block">
<p class="ocr_par" id="par_1_11" lang="eng" title="bbox 2552 5788 4535 5967">
<span class="ocr_line" id="line_1_105" title="bbox 2553 5788 4535 5863; baseline 0 -17; x_size 75; x_descenders 17; x_ascenders 19"><span class="ocrx_word" id="word_1_837" title="bbox 2553 5797 2703 5846; x_wconf 99">west</span> <span class="ocrx_word" id="word_1_838" title="bbox 2756 5790 3032 5846; x_wconf 92">Western</span> <span class="ocrx_word" id="word_1_839" title="bbox 3086 5788 3390 5846; x_wconf 85">Australia</span> <span class="ocrx_word" id="word_1_840" title="bbox 3444 5788 3495 5846; x_wconf 99">is</span> <span class="ocrx_word" id="word_1_841" title="bbox 3553 5807 3627 5846; x_wconf 99">an</span> <span class="ocrx_word" id="word_1_842" title="bbox 3682 5789 3961 5863; x_wconf 78">example</span> <span class="ocrx_word" id="word_1_843" title="bbox 4017 5788 4089 5846; x_wconf 90">of</span> <span class="ocrx_word" id="word_1_844" title="bbox 4139 5807 4173 5846; x_wconf 99">a</span> <span class="ocrx_word" id="word_1_845" title="bbox 4227 5788 4535 5846; x_wconf 93">disturbed</span>
</span>
<span class="ocr_line" id="line_1_106" title="bbox 2552 5892 4533 5967; baseline 0 -17; x_size 75; x_descenders 18; x_ascenders 18"><span class="ocrx_word" id="word_1_846" title="bbox 2552 5893 2895 5967; x_wconf 88">landscape.</span> <span class="ocrx_word" id="word_1_847" title="bbox 2931 5892 3096 5950; x_wconf 92">Prior</span> <span class="ocrx_word" id="word_1_848" title="bbox 3126 5901 3188 5950; x_wconf 99">to</span> <span class="ocrx_word" id="word_1_849" title="bbox 3220 5894 3537 5967; x_wconf 90">European</span> <span class="ocrx_word" id="word_1_850" title="bbox 3572 5893 3910 5950; x_wconf 99">settlement</span> <span class="ocrx_word" id="word_1_851" title="bbox 3942 5893 4040 5950; x_wconf 99">the</span> <span class="ocrx_word" id="word_1_852" title="bbox 4075 5893 4254 5950; x_wconf 92">Swan</span> <span class="ocrx_word" id="word_1_853" title="bbox 4287 5893 4533 5950; x_wconf 93">Coastal</span>
</span>
</p>
</div>
</div>
""", 'html.parser')
        generated_text = hocr_met.areas_to_text(soup)
        expected_text = """Methods
Study area
The urban area of the Perth metropolitan region in south—
west Western Australia is an example of a disturbed
landscape. Prior to European settlement the Swan Coastal"""
        self.assertIn(expected_text, generated_text)

    def test_areas_to_text_start_slice(self):
        soup = BeautifulSoup("""
                <div class="ocr_page" id="page_1" title='image "/foobar.png"; bbox 0 0 4961 6591; ppageno 0'>
                <div class="ocr_carea" id="block_1_7" title="bbox 2552 5270 4531 5759" ts:table-score="2" ts:type="other">
        <p class="ocr_par" id="par_1_10" lang="eng" title="bbox 2552 5270 4531 5759">
        <span class="ocr_line" id="line_1_102" title="bbox 2552 5270 2858 5327; baseline 0.003 -1; x_size 74.650894; x_descenders 17.650898; x_ascenders 17"><span class="ocrx_word" id="word_1_824" title="bbox 2552 5270 2858 5327; x_wconf 91">Methods</span>
        </span>
        <span class="ocr_line" id="line_1_103" title="bbox 2555 5478 2912 5552; baseline 0 -17; x_size 74; x_descenders 17; x_ascenders 18"><span class="ocrx_word" id="word_1_825" title="bbox 2555 5478 2742 5552; x_wconf 92">Study</span> <span class="ocrx_word" id="word_1_826" title="bbox 2776 5496 2912 5535; x_wconf 98">area</span>
        </span>
        <span class="ocr_line" id="line_1_104" title="bbox 2552 5684 4531 5759; baseline 0 -17; x_size 75; x_descenders 17; x_ascenders 19"><span class="ocrx_word" id="word_1_827" title="bbox 2552 5685 2679 5742; x_wconf 99">The</span> <span class="ocrx_word" id="word_1_828" title="bbox 2711 5685 2898 5742; x_wconf 98">urban</span> <span class="ocrx_word" id="word_1_829" title="bbox 2933 5703 3068 5742; x_wconf 98">area</span> <span class="ocrx_word" id="word_1_830" title="bbox 3101 5684 3172 5742; x_wconf 88">of</span> <span class="ocrx_word" id="word_1_831" title="bbox 3198 5685 3297 5742; x_wconf 99">the</span> <span class="ocrx_word" id="word_1_832" title="bbox 3330 5685 3503 5742; x_wconf 92">Perth</span> <span class="ocrx_word" id="word_1_833" title="bbox 3535 5684 3960 5759; x_wconf 90">metropolitan</span> <span class="ocrx_word" id="word_1_834" title="bbox 3991 5684 4202 5759; x_wconf 85">region</span> <span class="ocrx_word" id="word_1_835" title="bbox 4234 5684 4296 5741; x_wconf 99">in</span> <span class="ocrx_word" id="word_1_836" title="bbox 4331 5685 4531 5742; x_wconf 99">south—</span>
        </span>
        </p>
        </div>
        <div class="ocr_carea" id="block_1_8" title="bbox 2552 5788 4535 5967" ts:table-score="1" ts:type="text block">
        <p class="ocr_par" id="par_1_11" lang="eng" title="bbox 2552 5788 4535 5967">
        <span class="ocr_line" id="line_1_105" title="bbox 2553 5788 4535 5863; baseline 0 -17; x_size 75; x_descenders 17; x_ascenders 19"><span class="ocrx_word" id="word_1_837" title="bbox 2553 5797 2703 5846; x_wconf 99">west</span> <span class="ocrx_word" id="word_1_838" title="bbox 2756 5790 3032 5846; x_wconf 92">Western</span> <span class="ocrx_word" id="word_1_839" title="bbox 3086 5788 3390 5846; x_wconf 85">Australia</span> <span class="ocrx_word" id="word_1_840" title="bbox 3444 5788 3495 5846; x_wconf 99">is</span> <span class="ocrx_word" id="word_1_841" title="bbox 3553 5807 3627 5846; x_wconf 99">an</span> <span class="ocrx_word" id="word_1_842" title="bbox 3682 5789 3961 5863; x_wconf 78">example</span> <span class="ocrx_word" id="word_1_843" title="bbox 4017 5788 4089 5846; x_wconf 90">of</span> <span class="ocrx_word" id="word_1_844" title="bbox 4139 5807 4173 5846; x_wconf 99">a</span> <span class="ocrx_word" id="word_1_845" title="bbox 4227 5788 4535 5846; x_wconf 93">disturbed</span>
        </span>
        <span class="ocr_line" id="line_1_106" title="bbox 2552 5892 4533 5967; baseline 0 -17; x_size 75; x_descenders 18; x_ascenders 18"><span class="ocrx_word" id="word_1_846" title="bbox 2552 5893 2895 5967; x_wconf 88">landscape.</span> <span class="ocrx_word" id="word_1_847" title="bbox 2931 5892 3096 5950; x_wconf 92">Prior</span> <span class="ocrx_word" id="word_1_848" title="bbox 3126 5901 3188 5950; x_wconf 99">to</span> <span class="ocrx_word" id="word_1_849" title="bbox 3220 5894 3537 5967; x_wconf 90">European</span> <span class="ocrx_word" id="word_1_850" title="bbox 3572 5893 3910 5950; x_wconf 99">settlement</span> <span class="ocrx_word" id="word_1_851" title="bbox 3942 5893 4040 5950; x_wconf 99">the</span> <span class="ocrx_word" id="word_1_852" title="bbox 4075 5893 4254 5950; x_wconf 92">Swan</span> <span class="ocrx_word" id="word_1_853" title="bbox 4287 5893 4533 5950; x_wconf 93">Coastal</span>
        </span>
        </p>
        </div>
        </div>
        """, 'html.parser')
        generated_text = hocr_met.areas_to_text(soup, 1)
        expected_text = """west Western Australia is an example of a disturbed
landscape. Prior to European settlement the Swan Coastal"""
        self.assertIn(expected_text, generated_text)


if __name__ == '__main__':
    unittest.main()
