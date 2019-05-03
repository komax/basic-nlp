#!/usr/bin/env python
import argparse
import subprocess
from shutil import copyfile
from multiprocessing import Pool

from pathlib import Path

from pages_pdf import page_numbers_pdf


OUT_DIR = './valid-pdfs'
ERR_DIR = './invalid-pdfs'


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdir', help="input directory containing files")
    parser.add_argument('outputdir',
                        help="output directory containing the files")
    parser.add_argument('errordir',
                        help="output directory containing the files with errorenous info")
    return parser


def all_pdfs(input_dir):
    return sorted(Path(input_dir).glob('*.pdf'))


def cp_file(file, out_dir):
    file_name = file.resolve().name
    out_file_name = Path(out_dir) / file_name
    copyfile(file, out_file_name)

def trim_pdf(pdf_file):
    global OUT_DIR, ERR_DIR
    try:
        page_numbers_pdf(pdf_file)
        cp_file(pdf_file, OUT_DIR)
    except subprocess.CalledProcessError as e:
        returncode = e.returncode
        print(f"{pdf_file} is erroneous; pdfinfo returns {returncode}")
        cp_file(pdf_file, ERR_DIR)
    except RuntimeError as e:
        print(e)
        cp_file(pdf_file, ERR_DIR)


def main():
    parser = set_up_argparser()
    args = parser.parse_args()

    # Ensure that the out dir exists. Otherwise create it
    out_dir = Path(args.outputdir)
    out_dir.mkdir(parents=True, exist_ok=True)
    global OUT_DIR, ERR_DIR
    OUT_DIR = args.outputdir

    
    # Ensure that the error dir exists. Otherwise create it
    ERR_DIR = args.errordir
    err_dir = Path(args.errordir)
    err_dir.mkdir(parents=True, exist_ok=True)

    # Select files to rename them.
    pdfs = all_pdfs(args.inputdir)
    assert pdfs, "No pdfs in this directory"
    
    # for pdf in pdfs:
    #     trim_pdf(pdf)
    pool = Pool()
    pool.map(trim_pdf, pdfs)


if __name__ == '__main__':
    main()
