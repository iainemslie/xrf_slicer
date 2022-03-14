"""
Created on Fri Mar 11 2022

@author: Iain Emslie
Technical Assistant (Plant Imaging)
Canadian Light Source
"""

import pandas as pd
import numpy as np
import os
import argparse
import tifffile


def run_slicer(infile_path, outdir_path):
    welcome_message()

    filename, file_extension = os.path.splitext(infile_path)
    if file_extension == '.xlsx':
        df = pd.read_excel(infile_path, header=None, engine='openpyxl')
    elif file_extension == '.xls':
        df = pd.read_excel(infile_path, header=None)
    elif file_extension == '.ods':
        df = pd.read_excel(infile_path, header=None, engine='odf')
    else:
        print("{} is an invalid file type".format(file_extension))

    num_rows = len(df)
    num_cols = len(df.columns)

    # We assume that input files always contain x,y,z coordinates but we ignore the z column
    number_xyz_cols = 3

    # We find the number of columns not including the x,y,z coordinates
    num_slices = num_cols - number_xyz_cols

    print("Input file path: '{}'".format(infile_path))
    print("Output directory path: '{}'\n".format(outdir_path))
    print(" - Number of rows in spreadsheet: {}".format(num_rows))
    print(" - Number of columns in spreadsheet: {}".format(num_cols))
    print(" - Number of slices: {}".format(num_slices))

    # We find max value then add 1 to account for '0th' index
    image_width = int(df.iloc[:, 0].max()) + 1
    image_height = int(df.iloc[:, 1].max()) + 1

    print(" - Image width: {}".format(image_width))
    print(" - Image height: {}".format(image_height))

    # Create a 3D numpy array to store images - row-column-slice
    image = np.empty((image_height, image_width, num_slices))

    # We iterate through excel rows and get x-y coordinates
    for row_index in range(num_rows):
        row_values = df.iloc[row_index]
        x_coord = int(row_values[0])
        y_coord = int(row_values[1])
        # Save to 3D numpy array the corresponding values
        for z_index in range(num_slices):
            image[y_coord, x_coord, z_index] = row_values[z_index + number_xyz_cols]

    if not os.path.isdir(os.path.join(outdir_path, 'sli')):
        os.makedirs(os.path.join(outdir_path, 'sli'), mode=0o777)

    # Write each z-slice as separate image
    for z_index in range(num_slices):
        tifffile.imwrite(os.path.join(outdir_path, 'sli', 'slice_{:03d}.tif'.format(z_index)),
                         image[:, :, z_index].astype('float32'), dtype='float32')

    finish_message()


def welcome_message():
    print("****************************************************")
    print("****************** - XRF-Slicer - ******************")
    print("****************************************************\n")


def finish_message():
    print("\n***************************************************")
    print("****************** - Completed - ******************")
    print("***************************************************\n")


if __name__ == '__main__':
    description_string = 'Turns excel x-ray fluorescence data into .tiff images. Output is saved to /sli directory\n'
    parser = argparse.ArgumentParser(description=description_string)
    parser.add_argument('--input', help='Input path to .xlsx, .xls or .ods file')
    parser.add_argument('--output', help='Output path to store /sli directory containing .tiff images')

    args = parser.parse_args()

    if args.input is None or args.output is None:
        print("Please supply --input argument with an input file")
        print("Please supply --output argument with an output directory")
    else:
        run_slicer(args.input, args.output)
