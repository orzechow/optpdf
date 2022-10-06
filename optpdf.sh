#!/bin/bash
#
# optpdf file.pdf
#   This script will attempt to optimize the given pdf
#
# See also https://tbrink.science/blog/2018/05/13/lossy-compression-for-pdfs

for i in "$@"
do

  file="$i"
  filebase=$(basename "$file" .pdf)
  optfile=/tmp/$$-${filebase}_opt.pdf
#  pdfsetting="printer"
  pdfsetting="ebook"
  echo "optimizing $i for $pdfsetting"
  if gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/${pdfsetting} -dNOPAUSE -dQUIET -dBATCH -sOutputFile="${optfile}" "${file}"; then
    optsize=$(stat -c "%s" "${optfile}")
    orgsize=$(stat -c "%s" "${file}")
    if [ "${optsize}" -eq 0 ]; then
      echo "No output!  Keeping original"
      rm -f "${optfile}"
      exit;
    fi
    if [ "${optsize}" -ge "${orgsize}" ]; then
      echo "Didn't make it smaller! Keeping original"
      rm -f "${optfile}"
      exit;
    fi
    bytesSaved=$((orgsize - optsize))
    percent=$((optsize * 100 / orgsize))
    echo Saving "$bytesSaved" bytes \(now "${percent}"% of old\)
    rm "${file}"
    mv "${optfile}" "${file}"
  fi

done
