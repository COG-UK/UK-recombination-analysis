setwd(dirname(rstudioapi::getSourceEditorContext()$path))

get_MAF <- function(rw){
  mx <- which.max(rw[2:5])
  minor_al_count <- 0
  for(i in 1:4){
    if(i == mx){
      next
    }
    minor_al_count <- minor_al_count + rw[i + 1]
  }
  MAF <- as.numeric(minor_al_count / sum(rw[2:5]))
  return(MAF)
}

get_mean_freq <- function(tbl) {
  MAFs <- apply(tbl, 1, get_MAF)
  return(mean(MAFs))
}

ambig_files <- list.files(path = "../bams_ambig/pileup", pattern = "allelecounts$", full.names = T)
ambig_acs <- lapply(ambig_files, read.table, header = T, sep = "\t")
ambig_MAF <- sapply(ambig_acs, get_mean_freq)

recom_files <- list.files(path = "../bams", pattern = "allelecounts$", full.names = T, recursive = T)
recom_acs <- lapply(recom_files, read.table, header = T, sep = "\t")
recom_MAF <- sapply(recom_acs, get_mean_freq)

mean(recom_MAF)
mean(ambig_MAF)

recom_files[which.max(recom_MAF)]

wilcox.test(ambig_MAF, recom_MAF)

png("MAFs.png", 7, 7, units = "i", res = 300)
hist(ambig_MAF, breaks = 10, 
     xlim = c(0,0.6),
     ylim = c(0, 8),
     xlab = "mean minor allele frequency",
     main = "raw read minor allele frequencies")
hist(recom_MAF, breaks = 10, xlim = c(0,0.6), add = T, col = "red")
legend("topright",
       col = c("red", "grey"),
       legend = c("recombinants", "mixtures"),
       pch = 15,
       bty = "n")
dev.off()
