import nltk
from nltk.tokenize import sent_tokenize
import argparse

nltk.download('punkt')

def checker(file_path):
    """
    Checks if file_path ends with '.txt'
    :param file_path: str
    :return: str
    """
    if not file_path.endswith('.txt'):
        raise argparse.ArgumentTypeError('File must have extension .txt')
    return file_path

# Use argparse to help construct a clean CLI
parser = argparse.ArgumentParser(description='Sort all sentences of an input text file in alphabetical order.')
parser.add_argument('File',
                    metavar='file_name',
                    type=checker,
                    help='the text file to order')
args = parser.parse_args()

# Iterates through lines in input file, tokenizing each into sentences, then outputs each sentence as a line in a new
# file, in alphabetical order
with open(args.File + "_ordered.txt", 'w') as outfile, open(args.File, 'r') as infile:
    all_sentences = []
    for line in infile:
        line = line.replace('"', '“')
        all_sentences.extend(sent_tokenize(line))
    for sentence in sorted(all_sentences,key=lambda s: s.strip('“')):
        outfile.write(sentence)
        outfile.write('\n')
