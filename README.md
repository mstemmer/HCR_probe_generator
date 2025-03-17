# HCR probe generator

This code is an add-on to https://github.com/rwnull/insitu_probe_generator

Use batch_probe_generator.ipynb to generate HCR probes for all genes, listed in a csv file.

1. Create a google or excel sheet of your targets:
    * required headers: 'short','gene_name','amplifier','reference','sequence'
    * short: abbreveation for species name: e.g. dr for Danio rerio
    * optionally add more columns, if suited for your documentation

1. Export sheet as .csv file and place into the targets folder

4. Open the jupyter notebook "batch_probe_generator.ipynb", set the project name and adjust the folder paths to this repository 
    * project name: same as the name of the targets.csv file, but without the ".csv".
    * paths are specific to your computer, depends where you placed this repository

3. Download and paste the required BLAST reference files in the references folder:
    * extract the file; should end with .fa
4. Run all the cells in the notebook "batch_probe_generator.ipynb"
    * make sure you have created and selected the correct python environment
    * see beginning of notebook for creating the conda environment
4. Find your HCR probes in the generated_probes folder
    * contains also the .xlsx file to upload to IDT
 