# https://leetcode.com/problems/tenth-line/

# Read from the file file.txt and output the tenth line to stdout.
LINE=0

while read entry ; do
  LINE=$(($LINE + 1))
  if [ $LINE -eq 10 ] ; then
    echo $entry
    exit 0
  fi
done < file.txt
