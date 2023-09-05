import argparse

from utils import validate_parameters, find_files_in_folderstructure, copy_files


def find_intersecting_hashes(files_in_inputdirectory, files_in_outputdirectory, verbose, filenames_in_inputdir):

  hashes_in_inputdir = [x[2] for x in files_in_inputdirectory]
  hashes_in_outputdir = {x[2] for x in files_in_outputdirectory}

  intersecting_hashes = []
  non_intersecting_hashes = []
  for index, hashvalue in enumerate(hashes_in_inputdir):
      if (hashvalue in hashes_in_outputdir):
          intersecting_hashes.append(index)
      else:
          non_intersecting_hashes.append(index)

  if len(intersecting_hashes) > 0:
      print("Some files in the input directory seem to exist in the output directory already.")

      if verbose:
        print("Files:")
        print([filenames_in_inputdir[index] for index in intersecting_hashes])

  return intersecting_hashes, non_intersecting_hashes 

def main():

  parser = argparse.ArgumentParser("simple_example")

  parser.add_argument("inputdir", help="Input directory.", type=str)
  parser.add_argument("outputdir", help="Output directory.", type=str)
  parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
  parser.add_argument('-s', '--sync', action='store_true')  # on/off flag

  # omit duplicate hashes
  # omit duplicate filenames
  # rename duplicate filenames
  # flatten source file structure

  args = parser.parse_args()

  parameters_valid = validate_parameters(args.inputdir, args.outputdir)

  if (not parameters_valid):
    print("Check your parameters.")
    return()

  files_in_inputdirectory = find_files_in_folderstructure([args.inputdir])
  files_in_outputdirectory = find_files_in_folderstructure([args.outputdir])

  filenames_in_inputdir = [x[1] for x in files_in_inputdirectory]
  filenames_in_outputdir = [x[1] for x in files_in_outputdirectory]

  print("Input directory: " + args.inputdir + " (" + str(len(filenames_in_inputdir)) + " files)")
  print("Output directory: " + args.outputdir + " (" + str(len(filenames_in_outputdir)) + " files)")

  if args.verbose:
    print("FILES IN INPUT-DIR:")
    print(filenames_in_inputdir)
    print("FILES IN OUTPUT-DIR:")
    print(filenames_in_outputdir)

  intersecting_hashes, non_intersecting_hashes = find_intersecting_hashes(files_in_inputdirectory, files_in_outputdirectory, args.verbose, filenames_in_inputdir)

  files_to_copy = [(files_in_inputdirectory[index]) for index in non_intersecting_hashes]

  if (args.sync):
    print("Copying " + str(len(files_to_copy)) + " files...")
    copy_files(files_to_copy, args.inputdir, args.outputdir)
    print("Done.")
  else:
    print("About to copy " + str(len(files_to_copy)) + " files to destination dir. Please add -s flag to copy.")


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    main()
