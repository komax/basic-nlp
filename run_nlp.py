import argparse
from subprocess import call


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('textfile', type=argparse.FileType('r'), help="input text file that will be processed")
    parser.add_argument("-o", "--output-directory", type=str, help="output directory from the nlp")
    parser.add_argument("-m", "--method", type=str, choices=["spacy, corenlp"], default="corenlp")
    return parser


def main():
    parser = set_up_argparser()
    args = parser.parse_args()

    out_dir = "."
    if "output_directory" in args:
        out_dir = args.output_directory

    if args.method == "corenlp":
        call_corenlp(input_file=args.textfile, class_path="corenlppath", output_dir=out_dir)
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


if __name__ == "__main__":
    main()