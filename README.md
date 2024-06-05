# Nanosensus

This is WIP repository on implementing DeepConsensus with Nanopore sequencing reads that have UMIs.

Steps before using Nanosensus

1. Basecall with dorado with `--emit-moves` and align to reference
2. Align with Uncalled4 to map signal to individual reads
3. Group UMIs with longread_umi; will replace with Flexiplex in the future

Steps from Nanosensus

4. Map the UMIs from fastq to the Uncalled4 BAM file with `map_umi.py`
5. Generate consensus with `consensus.py` on UMI mapped BAM file
6. Preprocess the BAM for training with `preprocess.py`

The current approach is to replace the PacBio features used in DeepConsensus

PacBio -> Nanopore

PW -> Mean current signal

IP -> Dwell time

Strand -> Strand

CCS -> abPOA consensus

SN -> Signal length
