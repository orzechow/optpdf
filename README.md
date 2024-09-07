# optpdf

`optpdf.py` is a tool for optimizing PDF files.

It uses ghostscript to reduce the given PDFs in file size and improve PDF compatibility.

Based on https://tbrink.science/blog/2018/05/13/lossy-compression-for-pdfs  
Rewritten to Python and modified by @orzechow and GitHub Copilot (kinda lazy 🤙)


## Usage

```bash
usage: optpdf [-h] [-q {screen,ebook,printer}] files [files ...]

This script will attempt to optimize the given pdf

positional arguments:
  files                 PDF files to optimize

options:
  -h, --help            show this help message and exit
  -q {screen,ebook,printer}, --quality {screen,ebook,printer}
                        PDF optimization setting (default: ebook)
```