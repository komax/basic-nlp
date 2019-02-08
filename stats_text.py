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
                        help="output directory")
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
    stats = np.array(stats_lines)
    return stats


def plot_histogram(stats_lines, axis):
    axis.set_title('Stopwords per line as stacked histogram')
    axis.set_xlabel('Line number')
    axis.set_ylabel('# stopwords per line')
    axis.margins(x=0)
    rows, cols = stats_lines.shape
    line_numbers = np.arange(start=0, stop=rows, step=1)
    axis.hist2d(line_numbers, stats_lines[:, 1], bins=11)


def plot_stacked_graph(stats_lines, axis):
    axis.set_title('Distribution of words per line as a stacked graph')
    axis.set_xlabel('Line number')
    axis.set_ylabel('# words per line')
    axis.margins(x=0)
    rows, cols = stats_lines.shape
    line_numbers = np.arange(start=0, stop=rows, step=1)
    alphabetic_words = stats_lines[:, 0]
    stopwords = stats_lines[:, 1]
    nonalphabetic_words = stats_lines[:, 2]
    # total_number_words = list(map(lambda elem: elem[2], stats_lines))

    legends = ['# alphabetic words', '# stopwords', '# non-alphabetic words']
    axis.stackplot(line_numbers, alphabetic_words, stopwords,
                   nonalphabetic_words, labels=legends)
    axis.legend(prop={'size': 7})


def plot_index_graph(stats_lines, axis):
    axis.set_title('Line chart for words per line')
    axis.set_xlabel('Line number')
    axis.set_ylabel('# words per line')
    axis.margins(x=0)
    rows, cols = stats_lines.shape
    line_numbers = np.arange(start=0, stop=rows, step=1)
    alphabetic_words = stats_lines[:, 0]
    stopwords = stats_lines[:, 1]
    total_number_words = stats_lines.sum(axis=1)

    axis.plot(line_numbers, total_number_words, label='# words', color='tab:green')
    axis.plot(line_numbers, alphabetic_words, label='# alphabetic words', color='tab:blue')
    axis.plot(line_numbers, stopwords, label='# stopwords', color='tab:orange')


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

    fig.tight_layout()
    fig.savefig(plot_name, bbox_inches='tight')

    #plt.show()
    #plt.close(fig)
    return


def png_name_from_inputfile(inputfile_name):
    path = Path(inputfile_name)
    return f"{path.stem}_stats.png"


def output_file_path(input_file, out_dir):
    out_path = Path(out_dir)
    out_path.expanduser()
    out_path.mkdir(parents=True, exist_ok=True)
    out_file_path = out_path / png_name_from_inputfile(input_file)
    return out_file_path


def main():
    parser = set_up_argparser()
    args = parser.parse_args()
    input_file = args.inputfile
    stats = parse_text(input_file)
    outdir = "stats"
    if args.output:
        outdir = args.output

    outfile = output_file_path(input_file, outdir)
    plot_statistics(stats, plot_name=outfile)


if __name__ == "__main__":
    main()
