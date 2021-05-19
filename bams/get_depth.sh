for FOL in groupA groupB groupC groupD CAMC-CBA018 CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF
do
  cd $FOL

  while read LINE
  do
    NAME=`echo $LINE | cut -d"/" -f2`

    BAMFILE=`find ../bams -name "*${NAME}*bam"`
    echo $BAMFILE

    ~/programs/samtools-1.12/bin/samtools depth $BAMFILE | awk '{ total += $3 } END { print total/NR }' > ${NAME}.depth

  done<queries
  cd ..
done
