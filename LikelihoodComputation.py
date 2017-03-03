#Metin Toksoz-Exley GEPHI

#Grab a random pathway 
import csv 
import random  


with open('SelectedPathways.csv', 'rt') as file: 
    contents = csv.reader(file) 
    listpathways = [x for x in contents] 
print listpathways
print contents
#random_row=random.randrange(len(listpathways))
#listpathways[random_row]


#REWRITE THIS SO THAT IT WORKS WITH LIST PATHWAYS THINGY 

    
    #assuming I don't need to limit it to the 633 actual rows because it has imported all data so 
    #random should stay within that constraint


#Grab a random set of n proteins from pathway

#Loop over all pathways 

#Report the ratio 

#Loop back to 1 to build up a sample

#Loop back to 1 with the next n to build stem and leaf plot for each n 
