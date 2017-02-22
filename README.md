# Protein-group-likelihood-computation
- Given that we see n proteins in a given pathway what is the probability that they are found in another pathway?
  . This seems biased because there could be lots of irrelevant pathways!
  . But the next distribution (below) tries to normalize against this bias by only considering relevant pathways 
 - Given that we see n proteins together in one pathway, what is the probability that one protein from that group being present in a pathway implies that the others are also present?
  . This should give us a basis for hypothesis testing to find large groups of closely related proteins
  . Really, this is the baseline for all our performance estimation (both for community detection and the like)

Protein group likelihood computation
+ Protein group likelihood computation!
 1. Grab a random pathway
 2. Grab a random set of n proteins from the pathway
 3. Loop over all pathways
  a. Is at least one protein in our group in that pathway?  If so, count it
  b. Are all proteins in our group in that pathway? If so, count it
 4. Report the ratio (# pathways with all proteins)/(# pathways with at least one protein)
 5. Loop back to 1 to build up a sample!
 6. Loop back to 1 with the next n to build stem-and=leaf plot for each n
