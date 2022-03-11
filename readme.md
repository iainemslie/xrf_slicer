## XRF-Slicer
XRF-Slicer converts X-ray fluorescent excel data specified in the same format as **onion-control.xlsx** into *.tiff* image slices.
The first two columns in the excel data represent the x and y image coordinates.
The third column represents the physical size of the images in the z-plane.
The remaining columns each represent a single image in the z-plane and record pixel intensity for
each x-y-coordinate pair of the output image.

The program has both command-line and GUI functionality.

The command line can be run from **slicer.py** and takes two arguments:  

    --input: Input path to .xlsx, .xls or .ods file
    --output: Output path to store /sli directory containing .tiff images

The GUI can be run from **slicer_qt.py**. Simply select or enter the paths to input file and output directory and click *"Run Slicer"*.
