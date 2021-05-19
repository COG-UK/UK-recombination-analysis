for FILE in groupA.fasta groupB.fasta groupC.fasta groupD.fasta CAMC-CB7AB3.fasta MILK-103C712.fasta QEUH-1067DEF.fasta
do
  cat $FILE >> all.fasta
done
