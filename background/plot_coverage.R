setwd(dirname(rstudioapi::getSourceEditorContext()$path))

data <- read.table("coverage.tsv", header = T)
data <- read.table("coverage2.tsv", header = T)

hist(data$coverage, xlim = c(0.98, 0.99), breaks = 200)

max(data$coverage)
sum(data$coverage == 0.9835)

