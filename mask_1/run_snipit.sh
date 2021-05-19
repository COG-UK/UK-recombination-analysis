for FOL in `ls -d */`
do
  cd $FOL
  tail -n+2 L.closest.csv | cut -d, -f1 > queries
  tail -n+2 L.closest.csv | cut -d, -f2 | cut -d";" -f1 | sort | uniq > L.neighbours
  tail -n+2 R.closest.csv | cut -d, -f2 | cut -d";" -f1 | sort | uniq > R.neighbours

  grep -A1 -f L.neighbours ../../background/date_filtered.cov_filtered.fasta | grep -v "^--$" > neighbours.fasta
  grep -A1 -f queries ../../recombinant_genomes/all.fasta | grep -v "^--$" >> neighbours.fasta
  grep -A1 -f R.neighbours ../../background/date_filtered.cov_filtered.fasta | grep -v "^--$" >> neighbours.fasta
  cat ../../background/MN908947.fa >> neighbours.fasta

  PREF=`echo $FOL | cut -d"/" -f1`
  snipit neighbours.fasta -r MN908947.3 -o $PREF

  cd ..
done
