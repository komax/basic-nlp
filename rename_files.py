#!/usr/bin/env python

import argparse
from shutil import copyfile

from pathlib import Path


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdir', help="input directory containing files")
    parser.add_argument('outputdir',
                        help="output directory containing the renamed files")
    parser.add_argument("ext", type=str,
                        help="filetype extension",
                        choices=['pdf', 'html', 'txt'])
    return parser


def select_files(input_dir, ext):
    return sorted(Path(input_dir).glob(f'*.{ext}'))


def transform_file_name(path):
    file_name = path.resolve().name
    return file_name.replace(" ", "_").replace("'", "").replace(",", "")\
        .replace("(", "").replace(")", "")


def rename_file(file, out_dir):
    file_name = transform_file_name(file)
    out_file_name = out_dir / file_name
    copyfile(file, out_file_name)


def main():
    parser = set_up_argparser()
    args = parser.parse_args()

    # Ensure that the out dir exists. Otherwise create it
    out_dir = Path(args.outputdir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Select files to rename them.
    files = select_files(args.inputdir, args.ext)

    for file in files:
        rename_file(file, out_dir)


if __name__ == '__main__':
    main()
