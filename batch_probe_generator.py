# create environment
# conda create -n hcr_probe_generator -c bioconda biopython numpy=1.23.5 pandas=1.3.5 blast

from maker37cb import maker
import os
import pandas as pd
from contextlib import redirect_stdout

pause = 12
polyAT = 5
polyCG = 5
choose = "n"
BlastProbes = "y"
dropout = "y"
show = "y"
report = "y"
maxprobe = "y"
numbr = 0

db = "/home/mstemmer/repos/insitu_probe_generator/Danio_rerio.GRCz11.cdna.all.fa"
outpath = "/home/mstemmer/repos/insitu_probe_generator/"


input_df = pd.read_csv("input.csv")

for index, row in input_df.iterrows():
    print(f'Working on {row["name"]} ...')
    outfile = os.path.join(f"{outpath}{row['name']}_probes.csv")
    
    with open(os.path.join(f"{outpath}{row['name']}_out.txt"), 'w') as f:
        with redirect_stdout(f):
            maker(row['name'],row['sequence'],row['amplifier'],pause,choose,polyAT,polyCG,BlastProbes,db,dropout,show,report,maxprobe,numbr,outfile)