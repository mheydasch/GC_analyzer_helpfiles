
Goal of this package is to provide additional helper functions to facilitate the work flow for the GrowthConeAnalyzer MATLAB software:
"Bagonis, Maria M., et al. "Automated profiling of growth cone heterogeneity defines relations between morphology and motility." J Cell Biol 218.1 (2019): 350-379."

Functions have been created based on personal needs and most of them are rather unpolished and might not be transferable to someone elses data architecture.

Contents of this package:

restructure_visualisations.py:

Goal of this script is to restructure the output of the growth cone analyzer.
To allow faster inspection of the segmentation performance and to facilitate exclusion
of un-, or badly segmented cells.

takes all segmentation representations burried deep in the folder of the GC output
and copies all of them to a single folder
moves all directories for which no segmentation could be found to a 'Not_segmented'
directory
with the -e option it accepts a text file as second input and moves all folders 
annotated in that file to a segmentation error directory.

Accepts as inputs:
-h to show the help documentation
-d, the directory where your analyzed images are stored
-e, the text file that contains your annotated filenames
If only –d is parsed it will search for the png files of the segmentation and copy them 
all together into a folder Collection, keeping a unique name for each of them. 
In addition it will take all folders where no segmentation files could be found and moves them to a folder Not_segmented
You can then observe the images and create a .txt file with those that have segmentation errors. 
Simply put the name of the image without frame number and extension into the text file.
Put one name per line only!
Works independent of the amount of subfolders.

gc_batch_run.py:
Goal of this function is to allow batch processing of all the movies of an experiment together after cropping.

Accepts as inputs:
-h to show the help documentation
-d, the directory where your cropped images are stored
-m, the modality you want to image with (this determines the segmentation parameter file that will get loaded. This is hardcoded
	for 4 default ones. Alternatively one can give the full path to a different file.
	the path to the default ones obviously needs to be adjusted for every user. This is easy to do by changing the respective line in the code.)
-s, the directory where your shade correction files are stored. This is only applicable for the biosensors modality

A call can look something like this:
python3 gc_batch_run.py -d /home/myimaging/Experiment1 -m 60x

This is not starting any computation but creates files that slurm will use to start the batch processing in:
./job_files
To start the batch process you then have to type:
slurm job_files/batch.sl 

restructure_actin.py: Takes the first image of channel1 of each cropped movie
			 and copies it into a collection folder, so one can look at all the movies again.

restructure_graphs.py: Takes all .png files in the current folder (preferential output of the graph folder) and copies them into a collection folder, so one can easier view all the graphs together.

restructure_fret.py: Takes all .png files in the FRET output folder and copies them into a collection folder. 

rename_Si_blinded.py: can be used to blind the cropping process to the experimenter.
Renames the files from the microscope into pattern: Well, Date, FoV, channel.
It replaces the well name by a random string of length 8 and creates a csv
file memorizing which string belongs to which well.
To be used before growth cone analyzer crops images to exclude personal bias
in picking the growth cones for each conditions.
Patterns might need to be adjusted depending on the original file names.

GetOriginalName.py:
To be used after Growth Cone analyzer has cropped the blinded videos
to get back the original well names by using the .csv file created by rename_Si_blinded.py





