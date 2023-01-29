# Read from the file file.txt and output the tenth line to stdout.
awk 'NR == 10' file.txt

# NR: the current row number (start from 1).
# Because the default action of awk is {print $0}, we can ignore the action.
