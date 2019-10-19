import argparse
import os
import sys
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("sourcePath", help="Path to the source folder")
parser.add_argument("sourceExt", help="Extention of the source files")
parser.add_argument("destinationPath", help="Path to the destination folder")
parser.add_argument("destinationExt", help="Extention of the destination files")

args = parser.parse_args()

sourceFiles = []
for root, dirs, files in os.walk(args.sourcePath):
    for name in files:
        if f'.{args.sourceExt}' in name:
            sourceFiles.append(name)
    break

sourceFiles.sort()

print(f'Found {len(sourceFiles)} source files')
print('\n'.join(sourceFiles))

destFiles = []
for root, dirs, files in os.walk(args.destinationPath):
    for name in files:
        if f'.{args.destinationExt}' in name:
            destFiles.append(name)
    break

destFiles.sort()
print(f'Found {len(destFiles)} destination files')
print('\n'.join(destFiles))



if (not sourceFiles) or (not destFiles):
    print("No files are found")
    sys.exit()

if len(sourceFiles) != len(destFiles):
    print("The number of files in both folders does not match. Exiting!")
    sys.exit()

newNames = []
for df in destFiles:
    file_name, file_ext = os.path.splitext(df)
    newNames.append(f'{file_name}.{args.sourceExt}')

newNames.sort()

print(f'{len(newNames)} new names: {newNames}')

for index,value in enumerate(sourceFiles):
    src = os.path.join(args.sourcePath, value)
    dst = os.path.join(args.destinationPath, newNames[index])

    print(f'Copying file from {src} to {dst}')
    shutil.copyfile(src, dst)
