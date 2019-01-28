#! /usr/bin/env python

import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup
import nltk


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdir', help="input directory containing hocr files")
    parser.add_argument("-o", "--output", help="output file containing the method section")
    return parser


def select_hocr_files(input_dir):
    return sorted(Path(input_dir).glob('*.html'))


stopwords = nltk.corpus.stopwords.words('english')


def build_methods_regex():
    terms = ["Method", "METHOD", "Materials and Methods",
             "MATERIALS AND METHODS", "Materials methods",
             "Material and methods",
             "Study site and methods", "Study Area and Methods",
             "M E T H O D S", "Material and Methods", "STUDY SITE AND METHODS",
             "Materials and Methods", "Study area and methods",
             "Study sites and methods", "MATERIAL AND METHODS",
             "MATERIALS AN D METHODS", "Sample sites and methods"]
    regex = re.compile(r'^([0-9]+.?\s*)?({})'.format("|".join(terms)))
    return regex


def build_end_methods_regex():
    terms = ["Discussion", "Conclusion", "Results", "Acknowledgements",
             "Appendix", "Appendices"]
    return re.compile(r'^([0-9]+.?\s*)?({})'.format("|".join(terms)))


def build_literature_heading_regex():
    terms = ["References", "Bibliography", "Literature", "LITERATURE",
             "REFERENCES", "R E F E R E N C E S"]
    return re.compile(r'^([0-9]+.?\s*)?({})'.format("|".join(terms)))


def soup_generator(hocr_files):
    for hocr_file in hocr_files:
        with open(hocr_file) as hocr:
            page_soup = BeautifulSoup(hocr.read(), 'html.parser')
            yield page_soup


def main():
    parser = set_up_argparser()
    args = parser.parse_args()
    hocr_files = select_hocr_files(args.inputdir)
    # Sort files by page number.
    hocr_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f.stem))))
    print(hocr_files)


if __name__ == "__main__":
    main()