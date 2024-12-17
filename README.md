# HCR probe generator

This code is based on https://github.com/rwnull/insitu_probe_generator

Use batch_probe_generator.ipynb to generate HCR probes for all genes, listed in an input.csv file.

1. place your targets.csv files into the targets folder
    * required headers: 'short','gene_name','amplifier','reference','sequence'
    * short: abbreveation for species name: e.g. dr for Danio rerio

2. download and paste the required BLAST reference files in the references folder:
    * extract the file; should end with .fa

3. Find your HCR probes in the generated_probes folder
    * contains also the .xlsx file to upload to IDT
 