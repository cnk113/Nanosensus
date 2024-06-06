# Nanosensus

This is WIP repository on implementing DeepConsensus with Nanopore sequencing reads that have UMIs.

Steps before using Nanosensus

1. Basecall with dorado with `--emit-moves` and align to reference
```
dorado basecaller sup path_to_fast5/ --reference fasta_ref_index --emit-moves --sort-bam > dorado.bam
```
3. Align with Uncalled4 to map signal to individual reads
```
uncalled4 align fasta_ref_index path_to_fast5 --bam-in dorado.bam -o out.bam
```
3. Group UMIs with longread_umi; will replace with Flexiplex in the future

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
