mydata <- read.csv("a0-weightsdf-2021-04-23.csv",
                   header = T)

mydata <- subset(mydata, subset = !is.na(mydata$coverage_weight))

sample.1000 <- sample(mydata$central_sample_id, size = 1000, prob = mydata$coverage_weight)
sample.2000 <- sample(mydata$central_sample_id, size = 2000, prob = mydata$coverage_weight)
sample.5000 <- sample(mydata$central_sample_id, size = 5000, prob = mydata$coverage_weight)

for(s in ls(pattern = "^sample")){
  write.table(get(s),
              file = paste0(s, ".txt"),
              col.names = F,
              row.names = F,
              quote = F)
}
