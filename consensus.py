import pyabpoa as pa
import pysam
import sys
from collections import defaultdict

bam = pysam.AlignmentFile(sys.argv[1], "rb")

seq = defaultdict(list)
seq_id = defaultdict(list)

for idx, read in enumerate(bam):
    try:
        umi = read.get_tag("UR")
        seq[umi].append(read.sequence)
        seq_id[umi].append(idx)
    except KeyError:
        continue

consensus = {}
a = pa.msa_aligner()
for umi,reads in seq.items():
    consensus[umi] = a.msa(reads, out_cons=True, out_msa=True)

res.cons_seq[0]


