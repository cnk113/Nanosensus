# Nanosensus

This is WIP repository on implementing DeepConsensus with Nanopore sequencing reads that have UMIs.

Steps before using Nanosensus

1. Basecall with dorado with `--emit-moves` and align to reference
```
dorado basecaller sup path_to_fast5/ --reference fasta_ref_index --emit-moves > dorado.bam
```
2. Align with Uncalled4 to map signal to individual reads
```
uncalled4 align fasta_ref_index path_to_fast5 --bam-in dorado.bam -o out.bam
```
1/2. Or basecall with dorado directly into Uncalled4 with stdin; make sure to download dorado model beforehand
```
dorado basecaller model path_to_fast5/ --reference fasta_ref_index --emit-moves | uncalled4 align fasta_ref_index path_to_fast5 -o out.bam --bam-in
```
3. Group UMIs with longread_umi or with Flexiplex
```
samtools bam2fq uncalled4.bam | flexiplex -d 10x3v3 -f 0 > reads.fastq
# From flexiplex
scripts/flexiplex_filter/main.py --whitelist 3M-february-2018.txt --no-inflection --outfile my_filtered_barcode_list.txt my_barcode_list.txt
flexiplex -d 10x3v3 -k my_filtered_barcode_list.txt reads.fastq > new_reads.fastq
```

Steps from Nanosensus

4. Map the UMIs from fastq to the Uncalled4 BAM file with `map_umi.py`
5. Generate consensus with `consensus.py` on UMI mapped BAM file
6. Preprocess the BAM for training with `preprocess.py`

`preprocess.py` is directly replacing `model_train_custom_loop.py` while maintaining object structure of PacBio reads

The current approach is to replace the PacBio features used in DeepConsensus

PacBio features -> Nanopore features

PW -> Mean current signal

IP -> Dwell time

Strand -> Strand

CCS -> abPOA consensus

SN -> Signal length
