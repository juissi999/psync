import argparse

from utils import find_files_in_folderstructure

parser = argparse.ArgumentParser("simple_example")

parser.add_argument("inputdir", help="Input directory.", type=str)
parser.add_argument("outputdir", help="Output directory.", type=str)


args = parser.parse_args()

print("Input directory: " + args.inputdir)
print("Output directory: " + args.outputdir)

files_in_outputdirectory = {}

find_files_in_folderstructure(args.inputdir, files_in_outputdirectory)

print(files_in_outputdirectory)
