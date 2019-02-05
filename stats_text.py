#! /usr/bin/env python

import argparse
import re
from pathlib import Path

import nltk

stopwords = nltk.corpus.stopwords.words('english')


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile',
                        help="input text file")
    parser.add_argument("-o", "--output",
                        help="output file")
    return parser


def stopwords_per_line(words):
    count = 0
    for word in words:
        if word in stopwords:
            count += 1
    return count


def alphabet_words_per_line(words):
    count = 0
    for word in words:
        match = re.match("[a-z]+", word)
        if match:
            count += 1
    return count


def generate_stats(line):
    words = line.split()
    words = [word.lower() for word in words]
    number_alphabetic_words = alphabet_words_per_line(words)
    number_stopwords = stopwords_per_line(words)
    total_number_words = len(words)
    return number_alphabetic_words, number_stopwords, total_number_words


def parse_text(text_file_name):
    path = Path(text_file_name)
    path.expanduser()

    with open(path, 'r') as text_file:
        for line in text_file:
            print(line)
            print(generate_stats(line))


def main():
    parser = set_up_argparser()
    args = parser.parse_args()
    parse_text(args.inputfile)


if __name__ == "__main__":
    main()
