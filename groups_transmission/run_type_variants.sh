do
  echo $FILE
  PREF=`echo $FILE | cut -d"." -f1`
  echo $PREF
  python3 type_variants.py --fasta-in aligned.fasta \
    --variants-config $FILE \
    --reference MN908947.fa \
    --variants-out ${PREF}.type_variants.csv \
    --append-genotypes
done
