import pyfastx
import sys
import pysam

fq = pyfastx.Fastx(sys.argv[1])

seq_umi = {}

for name,seq,qual in fq:
    umi = name
    seq_umi[name] = umi

bam = pysam.AlignmentFile(sys.argv[2], "rb")

for read in bam:
   umi = seq_umi.get(read.name)
   if umi is not None:
       read.set_tag("UR", umi)
   

