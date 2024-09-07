#!/usr/bin/env python3

# optpdf file.pdf
#   This script will attempt to optimize the given pdf
#
# See also https://tbrink.science/blog/2018/05/13/lossy-compression-for-pdfs
#
# Rewritten to Python by GitHub Copilot

import os
import subprocess
import sys

def optimize_pdf(file):
  filebase = os.path.splitext(os.path.basename(file))[0]
  optfile = f"/tmp/{os.getpid()}-{filebase}_opt.pdf"
  pdfsetting = "ebook"
  # pdfsetting="printer"
  print(f"Optimizing {file} for {pdfsetting}")
  try:
    subprocess.run(["gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", f"-dPDFSETTINGS=/{pdfsetting}", "-dNOPAUSE", "-dQUIET", "-dBATCH", f"-sOutputFile={optfile}", file], check=True)
    optsize = os.path.getsize(optfile)
    orgsize = os.path.getsize(file)
    if optsize == 0:
      print("No output! Keeping original")
      os.remove(optfile)
      return
    if optsize >= orgsize:
      print("Didn't make it smaller! Keeping original")
      os.remove(optfile)
      return
    bytesSaved = orgsize - optsize
    percent = (optsize * 100) // orgsize
    print(f"Saving {bytesSaved} bytes (now {percent}% of old)")
    os.remove(file)
    os.rename(optfile, file)
  except subprocess.CalledProcessError as e:
    print(f"Error optimizing {file}: {e}")

if __name__ == "__main__":
  for file in sys.argv[1:]:
    optimize_pdf(file)
