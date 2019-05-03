#!/usr/bin/env python
import re
import subprocess


def page_numbers_pdf(pdf_file):
    cmd = ["pdfinfo", pdf_file]
    result_bytes = subprocess.check_output(cmd,stderr=subprocess.STDOUT)
    for line in iter(result_bytes.splitlines()):
        if line.startswith(b'Pages:'):
            match = re.match(r'^Pages:\s+(\d+)$', line.decode('utf-8'))
            if match:
                #print(match.groups())
                groups = match.groups()
                pages_str = groups[0]
                return int(pages_str)
            else:
                raise RuntimeError("Cannot match page numbers in pdfinfo output: {}".format(result_bytes))
        elif line.startswith(b'Syntax Error:') or\
            line.startswith(b'Syntax Warning:'):
            raise RuntimeError('Cannot retrieve page numbers via pdfinfo {}'.format(line))
    raise RuntimeError("Cannot read pages numbers from pdfinfo: {}".format(result_bytes))


def main():
    import sys
    assert len(sys.argv) == 2, "Need to supply a pdf as an argument"
    pdf_file = sys.argv[1]
    try:
        pages = page_numbers_pdf(pdf_file)
        print(pages)
    except subprocess.CalledProcessError as e:
        returncode = e.returncode
        print(f"f{pdf_file} is erroneous; pdfinfo return {returncode}")
        sys.exit(returncode)
    except RuntimeError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
