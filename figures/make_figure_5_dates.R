setwd(dirname(rstudioapi::getSourceEditorContext()$path))

data <- read.csv("../groupA_transmission/groupA_transmission.csv")
# data$sample_date <- as.Date(data$sample_date)

temp <- table(data$epi_week)
df <- data.frame("epi_week" = seq(57,66), "count" = rep(0, 10))
df$epi_week <- as.character(df$epi_week )
for(i in 1:10){
  if(df$epi_week[i] %in% names(temp)){
    df$count[i] <- temp[df$epi_week[i]]
  }
}

cols <- c(rep("red", 5), rep("#1a505f", 8))

svg("groupA_epiweek_counts.svg",
    width = 14, height = 8)
# pdf("groupA_epiweek_counts.pdf",
#     width = 14, height = 8)
par(cex = 2, cex.axis = 1.4, cex.lab = 1.4)
barplot(count ~ epi_week, data = df,
        xlab = "epiweek",
        ylab = "number of genomes",
        ylim = c(0, 20),
        col = cols, border = NA,
        axes = F)
axis(side = 2,
     lwd = 2)
legend("topleft",
       legend = c("Group A",
                  "transmission"),
       col = c("red", "#1a505f"),
       bty = "n",
       pch = 15,
       pt.cex = 2)
dev.off()



