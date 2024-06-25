# pdf-line-ruler
A python tool that is useful for calculating the sum of lengths of all lines in a PDF file. Particularly useful for estimating the length of laser cutting jobs.

Usage: python3 main.py <Path to PDF file> <Optional: Path to known length PDF file> <Optional: time takes to cut known length PDF file in any time units>

Estimated time = <time to cut known length PDF file> / <length of known length PDF file (estimated from file2)> * <length of target PDF file>
