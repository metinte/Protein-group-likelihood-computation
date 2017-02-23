#Metin Toksoz-Exley GEPHI

#Grab a random pathway 
import csv 
import random  

def random_row(file): 
    line = next(file) 
    for num, row in enumerate(file): 
      if random.randrange(num + 2): continue 
      line = row 
    return line 

with open('SelectedPathways.csv', 'rt', 'wt') as file: 
    contents = csv.reader(file) 
    [x for x in contents] 
    random_row(file)
random_row(file)
    #assuming I don't need to limit it to the 633 actual rows because it has imported all data so 
    #random should stay within that constraint


#Grab a random set of n proteins from pathway

#Loop over all pathways 

#Report the ratio 

#Loop back to 1 to build up a sample

#Loop back to 1 with the next n to build stem and leaf plot for each n 
