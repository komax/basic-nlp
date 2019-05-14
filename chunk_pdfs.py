#!/usr/bin/env python
import argparse
import subprocess
from shutil import copyfile
from multiprocessing import Pool

from pathlib import Path

from more_itertools import chunked



INPUT_DIR = Path('./pdfs')
OUT_DIR = Path('./out')


def set_up_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputdir', help="input directory containing files")
    parser.add_argument('outputdir',
                        help="output directory containing the chunked files")
    parser.add_argument('chunksize',
                        help="number of pdfs in a chunk", type=int, choices=range(0, 6_001))
    return parser


def all_pdfs():
    return iter(sorted(INPUT_DIR.glob('*.pdf')))


def cp_file(file, out_dir):
    file_name = file.resolve().name
    out_file_name = out_dir / file_name
    copyfile(file, out_file_name)


def copy_chunk(param):
    i, chunk = param
    out_dir_chunk = OUT_DIR / f"chunk_{i}"
    out_dir_chunk.mkdir()
    for pdf_file in chunk:
        cp_file(pdf_file, out_dir_chunk)


def main():
    parser = set_up_argparser()
    args = parser.parse_args()

    global INPUT_DIR, OUT_DIR
    # Ensure that the input dir exists. Otherwise create it
    INPUT_DIR = Path(args.inputdir)
    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Ensure that the out dir exists. Otherwise create it
    OUT_DIR = Path(args.outputdir)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    chunk_size = args.chunksize
    assert chunk_size > 0, "Chunk size needs to be a positive integer"


    # Select files to rename them.
    pdfs = all_pdfs()
    assert pdfs, "No pdfs in this directory"

    # Split pdfs into chunks.
    chunks = chunked(pdfs, chunk_size)

    # for i, chunk in enumerate(chunks):
    #     copy_chunk(i,chunk)

    pool = Pool()
    pool.map(copy_chunk, enumerate(chunks))


if __name__ == '__main__':
    main()
