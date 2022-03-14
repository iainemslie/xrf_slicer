## XRF-Slicer
XRF-Slicer converts x-ray fluorescence excel data specified in the same format as **onion-control.xlsx** into **.tiff** image slices.
The first two columns in the excel data represent the x and y image coordinates.
The third column represents the physical size of the images in the z-plane.
The remaining columns each represent a single image in the z-plane and record pixel intensity for
each x-y-coordinate pair of the output image.

The program has both command-line and GUI functionality.

The command line can be run from **slicer.py** and takes two arguments:  

    --input: Input path to .xlsx, .xls or .ods file
    --output: Output path to store /sli directory containing .tiff images

The GUI can be run from **slicer_gui.py**. Simply select or enter the paths to input file and output directory and click *'Run Slicer'*.

Created for Jarvis Stobbs (Plant Imaging Lead) - jarvis.stobbs@lightsource.ca

## Installation

1. Make sure you have Python3 installed
2. Install virtualenv using either of:

        pip install virtualenv

        python -m pip install virtualenv
3. Create a new virtual environment somewhere in the filesystem:

        virtualenv my_venv
4. Activate the environment:
   1. Windows:

           my_venv/Scripts/activate
   2. Linux:

           source my_venv/bin/activate

5. Install the required modules:

        pip install -r requirements.txt
6. Run the program:
   1. Command Line:

           python slicer.py --input path/to/infile.xls --output path/to/outdir
   2. Graphical interface

           python slicer_gui.py
   
These links may be useful if you run into trouble:

https://aaronstannard.com/how-to-setup-a-proper-python-environment-on-windows/

https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/