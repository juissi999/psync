import argparse

from utils import find_files_in_folderstructure

parser = argparse.ArgumentParser("simple_example")

parser.add_argument("inputdir", help="Input directory.", type=str)
parser.add_argument("outputdir", help="Output directory.", type=str)


args = parser.parse_args()

print("Input directory: " + args.inputdir)
print("Output directory: " + args.outputdir)


files_in_inputdirectory = find_files_in_folderstructure(args.inputdir)
files_in_outputdirectory = find_files_in_folderstructure(args.outputdir)

filenames_in_inputdir = [x[1] for x in files_in_inputdirectory]
filenames_in_outputdir = [x[1] for x in files_in_outputdirectory]

print("FILES IN INPUT-DIR:")
print(filenames_in_inputdir)
print("FILES IN OUTPUT-DIR:")
print(filenames_in_outputdir)

hashes_in_inputdir = [x[2] for x in files_in_inputdirectory]
hashes_in_outputdir = {x[2] for x in files_in_outputdirectory}

intersecting_hashes = []
for index, hashvalue in enumerate(hashes_in_inputdir):
    if (hashvalue in hashes_in_outputdir):
        intersecting_hashes.append(index)

if len(intersecting_hashes) > 0:
    print("Some files in the input directory seem to exist in the output directory already.")
    print("Files:")
    print([filenames_in_inputdir[index] for index in intersecting_hashes])
