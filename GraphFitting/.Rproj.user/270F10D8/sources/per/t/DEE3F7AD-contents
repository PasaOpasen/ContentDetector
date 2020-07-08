
library(tidyverse)

data = read_delim('vacs_train.csv', delim = ';')

data2 = data[,c(19,22)]

write_delim(data2, 'vacs.csv', delim = ';')


data3 = data[,c(18,22)]

write_delim(data3, 'vacs_experience.csv', delim = ';')




levels(factor(data3$experience.name))
