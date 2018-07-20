#!/usr/bin/env python3

import argparse
from subprocess import call
from calling_spacy import nlp_spacy


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('textfile', type=argparse.FileType('r'), help="input text file that will be processed")
    parser.add_argument("-o", "--output-directory", type=str, help="output directory from the nlp")
    parser.add_argument("-m", "--method", type=str, choices=["spacy", "corenlp"], default="corenlp")
    return parser


def main():
    parser = set_up_argparser()
    args = parser.parse_args()

    out_dir = "."
    if args.output_directory:
        out_dir = args.output_directory

    if args.method == "corenlp":
        call_corenlp(input_file=args.textfile, class_path="/Users/mk21womu/prog/stanford-corenlp-full-2018-02-27", output_dir=out_dir)
    elif args.method == "spacy":
        call_spacy(input_file=args.textfile, output_dir=out_dir)
    else:
        raise Exception("Not yet supported")


def call_corenlp(input_file, class_path, output_dir=".", is_java_8=False):
    func_call = ["java", "-cp", f'{class_path}/*', "-Xmx3g"]
    if not is_java_8:
        func_call.extend(["--add-modules", "java.se.ee"])
    main_class = "edu.stanford.nlp.pipeline.StanfordCoreNLP"
    corenlp_parameters = [main_class, "-annotators", "tokenize,ssplit,pos,lemma,ner,depparse", '-file', input_file.name,
                          '-outputDirectory', output_dir]
    func_call.extend(corenlp_parameters)
    print(" ".join(func_call))
    call(func_call)


def call_spacy(input_file, output_dir="."):
    return nlp_spacy(input_file, output_dir)


if __name__ == "__main__":
    main()