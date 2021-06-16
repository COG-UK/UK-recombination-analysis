This respository documents the scripts used to analyse data for the paper:

Jackson B, et al. **Generation and transmission of inter-lineage recombinants in the SARS-CoV-2 pandemic**. *Submitted*

--

It is organised into the following subdirectories (in alphabetical order), which represent the file structure used in the original analyses, but note that the sequences and their associated metadata are not included in this repository:
<br>
<br>

`3seq_weighted_background`

- the command used to run 3SEQ

`background`

- scripts to handle the comprehensive background sequence dataset (of non-recombinant sequences)

`bams`

- scripts to investigate the raw read data for the recombinants

`bams_ambig`

- scripts to investigate the raw read data for the mixtures

`figures`

- scripts to generate figures for the manuscript

`geography`

- scripts to investigate the presence of other lineages in the geographic locations of the putative recombinants

`groupA_neighbours_tree`

- scripts and metadata to generate the phylogenetic tree for the Group A transmission chain + parental context

`mask_1`

- scripts to carry out the first mask and search for candidate parental sequences by genetic similarity for the different regions of the recombinant genomes

`mask_2`

- scripts to carry out the final mask and search for candidate parental sequences by genetic similarity for the different regions of the recombinant genomes

`recombinant_genomes`

- scripts to handle the recombinant genomes

`scripts`

- miscellaneous python scripts which were called elsewhere in the repository

`weighted background`

- scripts to generate and analyse the weighted random sample of background (non-recombinant) sequences from the UK

`weighted_background_phylo_incong`

- scripts for running the phylogenetic incongruence analysis, and the resulting phylogenetic trees
