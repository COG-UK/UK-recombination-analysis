mkdir -p pileup

for BAMFILE in bams/*bam
do
  NAME=`echo $BAMFILE | cut -d"/" -f2 | cut -d"." -f1`

  python3 ../scripts/get_mpileup_positions.py $BAMFILE b117.pos pileup/${NAME}.poslist

  ~/programs/samtools-1.9/samtools mpileup -l pileup/${NAME}.poslist $BAMFILE > pileup/${NAME}.pileup

  python3 ../scripts/parse_pileup.py pileup/${NAME}.pileup > pileup/${NAME}.allelecounts
done
