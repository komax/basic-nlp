#! /usr/bin/env python

import argparse
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import nltk


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile',
                        help="input text file")
    parser.add_argument("-o", "--output",
                        help="output file")
    return parser


def stopwords_per_line(words):
    stopwords = nltk.corpus.stopwords.words('english')
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
    return number_alphabetic_words - number_stopwords, number_stopwords, \
           total_number_words - number_alphabetic_words
#  return number_alphabetic_words, number_stopwords, total_number_words


def parse_text(text_file_name):
    path = Path(text_file_name)
    path.expanduser()

    stats_lines = []

    with open(path, 'r') as text_file:
        for i, line in enumerate(text_file):
            stats_line = generate_stats(line)
            stats_lines.append(stats_line)
            print(f"{i}:{line}")
            print(generate_stats(line))
            # if stats_line[0] == 0 == stats_line[1]:
            #     print(f"{i}:{line}")
            #     print(generate_stats(line))
    return stats_lines


def plot_histogram(stats_lines, axis):
    axis.set_title('word lengths as a stacked histogram')
    number_bins = round(len(stats_lines)/5)
    print(number_bins)

    stats = np.array(stats_lines)
    print(stats.shape)

    axis.hist(stats, histtype='bar')


def plot_stacked_graph(stats_lines, axis):
    axis.set_title('Distribution of words as a stacked graph')
    line_numbers = list(range(0, len(stats_lines)))
    alphabetic_words = list(map(lambda elem: elem[0], stats_lines))
    stopwords = list(map(lambda elem: elem[1], stats_lines))
    nonalphabetic_words = list(
        map(lambda elem: elem[2], stats_lines))
    # total_number_words = list(map(lambda elem: elem[2], stats_lines))

    axis.stackplot(line_numbers, alphabetic_words, stopwords, nonalphabetic_words)


def plot_index_graph(stats_lines, axis):
    axis.set_title('Line chart for word distribution')
    line_numbers = list(range(0, len(stats_lines)))
    alphabetic_words = list(map(lambda elem: elem[0], stats_lines))
    stopwords = list(map(lambda elem: elem[1], stats_lines))
    total_number_words = list(
        map(lambda elem: elem[0] + elem[1] + elem[2], stats_lines))

    axis.plot(line_numbers, alphabetic_words, label='# alphabetic words')
    axis.plot(line_numbers, stopwords, label='# stopwords')
    axis.plot(line_numbers, total_number_words, label='# words')
    axis.legend(prop={'size': 7})

    # alphabetic_words = list(map(lambda elem: elem[0] - elem[1], stats_lines))
    # stopwords = list(map(lambda elem: elem[1], stats_lines))
    # nonalphabetic_words = list(
    #     map(lambda elem: elem[2] - elem[0], stats_lines))
    # total_number_words = list(map(lambda elem: elem[2], stats_lines))


def plot_statistics(stats_lines, plot_name):
    fig, axes = plt.subplots(nrows=3, ncols=1)

    axis0, axis1, axis2 = axes.flatten()

    plot_histogram(stats_lines, axis0)
    plot_stacked_graph(stats_lines, axis1)
    plot_index_graph(stats_lines, axis2)

    line_numbers = list(range(0, len(stats_lines), 5))
    print(line_numbers)

    fig.tight_layout()
    fig.savefig(plot_name, bbox_inches='tight')

    #plt.show()
    #plt.close(fig)
    return


def main():
    parser = set_up_argparser()
    args = parser.parse_args()
    stats = parse_text(args.inputfile)
    outfile = "word_statistics.png"
    if args.output:
        outfile = args.output
    plot_statistics(stats, plot_name=outfile)


if __name__ == "__main__":
    main()
