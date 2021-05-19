mkdir -p groupA groupB groupC groupD CAMC-CBA018 CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF

for FOL in groupA groupB groupC groupD CAMC-CBA018 CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF
do
  cd $FOL
  cp ../../mask_2/${FOL}/queries queries

  while read LINE
  do
    NAME=`echo $LINE | cut -d"/" -f2`
    grep -A1 $LINE ../../recombinant_genomes/all.fasta > snps.temp.fasta
    grep $LINE ../../mask_2/${FOL}/L.closest.csv | cut -d"," -f2 | cut -d";" -f1 > ${NAME}.set
    grep $LINE ../../mask_2/${FOL}/R.closest.csv | cut -d"," -f2 | cut -d";" -f1 >> ${NAME}.set
    python3 ../../scripts/get_fasta_from_IDs.py ../../background/date_filtered.cov_filtered.fasta ${NAME}.set >> snps.temp.fasta

    BAMFILE=`find ../bams_trimmed -name "*${NAME}*bam"`
    echo $BAMFILE

    ~/programs/gofasta/gofasta snps --reference ../../background/MN908947.fa --query snps.temp.fasta | tail -n+2 | cut -d, -f2 | tr "|" "\n" | sort | uniq > ${NAME}.snps
    python3 ../../scripts/get_mpileup_positions.py $BAMFILE ${NAME}.snps ${NAME}.poslist

    ~/programs/samtools-1.9/samtools mpileup -l ${NAME}.poslist $BAMFILE > ${NAME}.pileup

    python3 ../../scripts/parse_pileup.py ${NAME}.pileup > ${NAME}.allelecounts

  rm ${NAME}.set snps.temp.fasta
  done<queries
  cd ..
done
