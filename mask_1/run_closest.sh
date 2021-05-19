~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupA/background.L.fasta --query groupA/groupA.L.fasta > groupA/L.closest.csv
~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupA/background.R.fasta --query groupA/groupA.R.fasta > groupA/R.closest.csv
rm groupA/background*fasta

~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupB/background.L.fasta --query groupB/groupB.L.fasta > groupB/L.closest.csv
~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupB/background.R.fasta --query groupB/groupB.R.fasta > groupB/R.closest.csv
rm groupB/background*fasta

~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupC/background.L.fasta --query groupC/groupC.L.fasta > groupC/L.closest.csv
~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupC/background.R.fasta --query groupC/groupC.R.fasta > groupC/R.closest.csv
rm groupC/background*fasta

~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupD/background.L.fasta --query groupD/groupD.L.fasta > groupD/L.closest.csv
~/programs/gofasta/gofasta closest -t2 --number 1000 --target groupD/background.R.fasta --query groupD/groupD.R.fasta > groupD/R.closest.csv
rm groupD/background*fasta

~/programs/gofasta/gofasta closest -t2 --number 1000 --target CAMC-CB7AB3/background.L.fasta --query CAMC-CB7AB3/CAMC-CB7AB3.L.fasta > CAMC-CB7AB3/L.closest.csv
~/programs/gofasta/gofasta closest -t2 --number 1000 --target CAMC-CB7AB3/background.R.fasta --query CAMC-CB7AB3/CAMC-CB7AB3.R.fasta > CAMC-CB7AB3/R.closest.csv
rm CAMC-CB7AB3/background*fasta

~/programs/gofasta/gofasta closest -t2 --number 1000 --target MILK-103C712/background.L.fasta --query MILK-103C712/MILK-103C712.L.fasta > MILK-103C712/L.closest.csv
~/programs/gofasta/gofasta closest -t2 --number 1000 --target MILK-103C712/background.R.fasta --query MILK-103C712/MILK-103C712.R.fasta > MILK-103C712/R.closest.csv
rm MILK-103C712/background*fasta

~/programs/gofasta/gofasta closest -t2 --number 1000 --target QEUH-1067DEF/background.L.fasta --query QEUH-1067DEF/QEUH-1067DEF.L.fasta > QEUH-1067DEF/L.closest.csv
~/programs/gofasta/gofasta closest -t2 --number 1000 --target QEUH-1067DEF/background.R.fasta --query QEUH-1067DEF/QEUH-1067DEF.R.fasta > QEUH-1067DEF/R.closest.csv
rm QEUH-1067DEF/background*fasta
