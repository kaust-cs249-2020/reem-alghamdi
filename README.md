# CHAPTER 1: Where in the Genome Does Replication Begin?

**This chapter is about finding the most frequent K-mer in a DNA string**


Genome replication is one of the most important tasks carried out in the cell. Before a cell can divide, it must first replicate its genome so that each of the two daughter cells inherits its own copy. 

![replication](https://static.wixstatic.com/media/988d7f_7ef43621eed44d0abf39a39c8287d322~mv2.png)

Replication begins in a genomic region called the replication origin (denoted ori) and is carried out by molecular copy machines called DNA polymerases.


Research has shown that the region of the bacterial genome encoding ori is typically a few hundred nucleotides long.


## Section 02
### PatternCount

We will use the term k-mer to refer to a string of length k and define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text. Following the above example, Count(ACA**ACTAT**GCAT**ACTAT**CGGGA**ACTAT**CCT, ACTAT) = 3. We note that Count(CG**ATATA**TCC**ATA**G, ATA) is equal to 3 (not 2) since we should account for overlapping occurrences of Pattern in Text.

    Code Challenge: Implement PatternCount (reproduced below).
    
    Input: Strings Text and Pattern.
    Output: Count(Text, Pattern).

Example: 

    Sample Input:
    
        GCGCG
        GCG
        
    Sample Output:
    
        2
    
    
### Frequent Words 

We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. You can see that ACTAT is a most frequent 5-mer of ACA**ACTAT**GCAT**ACTAT**CGGGA**ACTAT**CCT, and ATA is a most frequent 3-mer of CG**ATATA**TCC**ATA**G.
    
    Frequent Words Problem: Find the most frequent k-mers in a string.

    Input: A string Text and an integer k.
    Output: All most frequent k-mers in Text.
Example: 
    
    Sample Input:
    
        ACGTTGCATGTCGCATGATGCATGAGAGCT
        4
    
    Sample Output:
    
        CATG GCAT

## Section 03
###  Reverse Complement
Given a nucleotide p, we denote its complementary nucleotide as p*. The reverse complement of a string Pattern = p1 … pn is the string Pattern_rc = pn* … p1* formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string. 

    Reverse Complement Problem: Find the reverse complement of a DNA string.

    Input: A DNA string Pattern.
    Output: Pattern_rc , the reverse complement of Pattern.

Example:

    Sample Input:
    
        AAAACCCGGT
    
    Sample Output:
    
        ACCGGGTTTT
 
### Pattern Matching
    Pattern Matching Problem: Find all occurrences of a pattern in a string.

    Input: Strings Pattern and Genome.
    Output: All starting positions in Genome where Pattern appears as a substring.

Example:

    Sample Input:
    
        ATAT
        GATATATGCATATACTT
        
    Sample Output:
    
        1 3 9
        
        
## Section 04
### Clump Finding

instead of finding clumps of a specific k-mer, let’s try to find every k-mer that forms a clump in the genome. Hopefully, the locations of these clumps will shed light on the location of ori. Our plan is to slide a window of fixed length L along the genome, looking for a region where a k-mer appears several times in short succession. The parameter value L = 500 reflects the typical length of ori in bacterial genomes. We defined a k-mer as a "clump" if it appears many times within a short interval of the genome. More formally, given integers L and t, a k-mer Pattern forms an (L, t)-clump inside a (longer) string Genome if there is an interval of Genome of length L in which this k-mer appears at least t times. (This definition assumes that the k-mer completely fits within the interval. This also does not take reverse complements into account yet.) 
For example, TGCA forms a (25,3)-clump in the following Genome:
gatcagcataagggtccC**TGCA**A**TGCA**TGACAAGCC**TGCA**GTtgttttac

    Clump Finding Problem: Find patterns forming clumps in a string.

    Input: A string Genome, and integers k, L, and t.
    Output: All distinct k-mers forming (L, t)-clumps in Genome.

Example:

    Sample Input:
    
        CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
        5 50 4
    
    Sample Output:
    
        CGACA GAAGA
        
## Section 07
We are now ready to discuss the replication process in more detail. As illustrated in the figure below, the two complementary DNA strands running in opposite directions around a circular chromosome unravel, starting at ori. As the strands unwind, they create two replication forks, which expand in both directions around the chromosome until the strands completely separate at the replication terminus (denoted ter). The replication terminus is located roughly opposite to ori in the chromosome.


![replication1](http://bioinformaticsalgorithms.com/images/Replication/naive_replication.png)

When all four DNA polymerases have reached ter, the chromosome's DNA will have been completely replicated, resulting in two pairs of complementary strands shown in the lower figure, and the cell is ready to divide.

![replication2](http://bioinformaticsalgorithms.com/images/Replication/naive_replication_complete.png)

The problem with our current description is that it assumes that DNA polymerases can copy DNA in either direction along a strand of DNA (i.e., both 5’ → 3’ and 3’ → 5’). However, nature has not yet equipped DNA polymerases with this ability, as they are unidirectional, meaning that they can only traverse a template strand of DNA in the 3' → 5' direction, which is opposite from the 5’ → 3’ direction of DNA.

The unidirectionality of DNA polymerase requires a major revision to our naive model of replication. Imagine that you decided to walk along DNA from ori to ter. There are four different half-strands of parent DNA connecting ori to ter, as highlighted in the figure below. Two of these half-strands are traversed from ori to ter in the 5’ → 3’ direction and are thus called forward half-strands (represented by thin blue and green lines in the figure below). The other two half-strands are traversed from ori to ter in the 3’ → 5’ direction and are thus called reverse half-strands (represented by thick blue and green lines in the figure below).

![replication3](http://bioinformaticsalgorithms.com/images/Replication/half_strands.png)

Biologists call a reverse half-strand (thick lines) a leading half-strand since a single DNA polymerase traverses this half-strand non-stop, and they call a forward half-strand (thin lines) a lagging half-strand since it is used as a template by many DNA polymerases stopping and starting replication.

our idea is to traverse the genome, keeping a running total of the difference between the counts of G and C. If this difference starts increasing, then we guess that we are on the forward half-strand; on the other hand, if this difference starts decreasing, then the we guess that we are on the reverse half-strand

![replication4](http://bioinformaticsalgorithms.com/images/Replication/increasing_decreasing_skew.png)


Since we don't know the location of ori in a circular genome, let's linearize it (i.e., select an arbitrary position and pretend that the genome begins here), resulting in a linear string Genome. We define Skew_i(Genome) as the difference between the total number of occurrences of G and the total number of occurrences of C in the first i nucleotides of Genome. The skew diagram is defined by plotting Skew_i (Genome) (as i ranges from 0 to |Genome|), where Skew0 (Genome) is set equal to zero. The figure below shows a skew diagram for the DNA string CATGGGCATCGGCCATACGCC.

Note that we can compute Skew_i+1(Genome) from Skew_i(Genome) according to the nucleotide in position i of Genome. If this nucleotide is G, then Skew_i+1(Genome) = Skew_i(Genome) + 1; if this nucleotide is C, then Skew_i+1(Genome)= Skew_i(Genome) – 1; otherwise, Skew_i+1(Genome) = Skew_i(Genome).


**Exercise Break**: Give all values of Skew_i (GAGCCACCGCGATA) for i ranging from 0 to 14.

![skew](http://bioinformaticsalgorithms.com/images/Replication/skew_diagram_basic.png)

**Sample Input:**

     CATGGGCATCGGCCATACGCC

**Sample Output:**

     0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2



### Minimum Skew
Let's follow the 5' → 3' direction of DNA and walk along the chromosome from ter to ori (along a reverse half-strand), then continue on from ori to ter (along a forward half-strand). In our previous discussion, we saw that the skew is decreasing along the reverse half-strand and increasing along the forward half-strand. Thus, the skew should achieve a minimum at the position where the reverse half-strand ends and the forward half-strand begins, which is exactly the location of ori!

    Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

    Input: A DNA string Genome.
    Output: All integer(s) i minimizing Skew_i (Genome) among all values of i (from 0 to |Genome|).

Example:
    
    Sample Input:
    
        TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
    
    Sample Output:
    
        11 24
        
## Section 08
### Hamming Distance
We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches. The number of mismatches between strings p and q is called the Hamming distance between these strings and is denoted HammingDistance(p, q).

    Hamming Distance Problem: Compute the Hamming distance between two strings.

    Input: Two strings of equal length.
    Output: The Hamming distance between these strings.

Example:

    Sample Input:
    
        GGGCCGTTGGT
        GGACCGTTGAC
    
    Sample Output:
    
        3
        
### Approximate Pattern Matching
We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.

    Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

    Input: Strings Pattern and Text along with an integer d.
    Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

Example:

    Sample Input:
    
        ATTCTGGA
        CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
        3
    
    Sample Output:
    
        6 7 26 27

### ApproximatePatternCount

Given strings Text and Pattern as well as an integer d, we define Count_d(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches. For example, Count_1(**AACAA**GCTG**ATAAACA**TTT**AAAGA**G, AAAAA) = 4 because AAAAA appears four times in this string with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

    Code Challenge: Implement ApproximatePatternCount.

    Input: Strings Pattern and Text as well as an integer d.
    Output: Count_d(Text, Pattern).

Example:

    Sample Input:
    
        GAGG
        TTTAGAGCCTTCAGAGG
        2
    
    Sample Output:
    
        4
        
### Frequent Words with Mismatches
A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Count_d(Text, Pattern) among all k-mers. Note that Pattern does not need to actually appear as a substring of Text; for example, as we already saw, AAAAA is the most frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though it does not appear exactly in this string.

    Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.

    Input: A string Text as well as integers k and d.
    Output: All most frequent k-mers with up to d mismatches in Text.

Example:

    Sample Input:
    
        ACGTTGCATGTCGCATGATGCATGAGAGCT
        4 1
    
    Sample Output:
    
        ATGC ATGT GATG
  
### Frequent Words with Mismatches and Reverse Complements
We now redefine the Frequent Words Problem to account for both mismatches and reverse complements. Recall that Pattern_rc refers to the reverse complement of Pattern.

    Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a string.

    Input: A DNA string Text as well as integers k and d.
    Output: All k-mers Pattern maximizing the sum Count_d(Text, Pattern)+ Count_d(Text, Pattern_rc) over all possible k-mers.

Example:

    Sample Input:
    
        ACGTTGCATGTCGCATGATGCATGAGAGCT
        4 1
    
    Sample Output:
    
        ATGT ACAT


## Section 11
### Neighbors
Our goal is to generate the d-neighborhood Neighbors(Pattern, d), the set of all k-mers whose Hamming distance from Pattern does not exceed d.

    Code Challenge: Implement Neighbors to find the d-neighborhood of a string.

    Input: A string Pattern and an integer d.
    Output: The collection of strings Neighbors(Pattern, d).

Example:

    Sample Input:
    
        ACG
        1
    
    Sample Output:
    
        CCG TCG GCG AAG ATG AGG ACA ACC ACT ACG
        

# CHAPTER 2: Which DNA Patterns Play the Role of Molecular Clocks?
**given a matrix of DNA strings, find the most frequent k-mer in all of them**


Genes encode proteins, and proteins dictate cell function. To respond to changes in their environment, cells must therefore control their protein levels. The flow of information from DNA to RNA to protein means that the cell can adjust the amount of proteins that it produces during both transcription (DNA to RNA) and translation (RNA to protein).

It turns out that every plant cell keeps track of day and night independently of other cells, and that just three plant genes, called LHY, CCA1, and TOC1, are the clock’s master timekeepers. Such regulatory genes, and the regulatory proteins that they encode, are often controlled by external factors (e.g., nutrient availability or sunlight) in order to allow organisms to adjust their gene expression.

For example, regulatory proteins controlling the circadian clock in plants coordinate circadian activity as follows. TOC1 promotes the expression of LHY and CCA1, whereas LHY and CCA1 repress the expression of TOC1, resulting in a negative feedback loop. In the morning, sunlight activates the transcription of LHY and CCA1, triggering the repression of TOC1 transcription. As light diminishes, so does the production of LHY and CCA1, which in turn do not repress TOC1 any more. Transcription of TOC1 peaks at night and starts promoting the transcription of LHY and CCA1, which in turn repress the transcription of TOC1, and the cycle begins again.

LHY, CCA1, and TOC1 are able to control the transcription of other genes because the regulatory proteins that they encode are transcription factors, or master regulatory proteins that turn other genes on and off. A transcription factor regulates a gene by binding to a specific short DNA interval called a regulatory motif, or transcription factor binding site, in the gene's upstream region, a 600-1000 nucleotide-long region preceding the start of the gene

The figure below shows ten NF-κB binding sites from the Drosophila melanogaster genome; the most popular nucleotides in every column are shown by upper case colored letters.

    1  T C G G G G g T T T t t
    2  c C G G t G A c T T a C
    3  a C G G G G A T T T t C
    4  T t G G G G A c T T t t
    5  a a G G G G A c T T C C
    6  T t G G G G A c T T C C
    7  T C G G G G A T T c a t
    8  T C G G G G A T T c C t
    9  T a G G G G A a c T a C
    10  T C G G G t A T a a C C

Our aim is to turn the biological challenge of finding regulatory motifs into a computational problem. Below, we have implanted a 15-mer hidden message at a randomly selected position in each of ten randomly generated DNA strings. This example mimics a transcription factor binding site hiding in the upstream regions of ten genes.

    1 "atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccg"
    2 "acccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataaaaaaaaaggggggga"
    3 "tgagtatccctgggatgacttaaaaaaaagggggggtgctctcccgatttttgaatatgtaggatcattcgccagggtccga"
    4 "gctgagaattggatgaaaaaaaagggggggtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggaga"
    5 "tcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaataaaaaaaagggggggcttatag"
    6 "gtcaatcatgttcttgtgaatggatttaaaaaaaaggggggggaccgcttggcgcacccaaattcagtgtgggcgagcgcaa"
    7 "cggttttggcccttgttagaggcccccgtaaaaaaaagggggggcaattatgagagagctaatctatcgcgtgcgtgttcat"
    8 "aacttgagttaaaaaaaagggggggctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgta"
    9 "ttggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcataaaaaaaagggggggaccgaaagggaag"
    10 "ctggtgagcaacgacagattcttacgtgcattagctcgcttccggggatctaatagcacgaagcttaaaaaaaaggggggga" 



This is a simple problem – applying an algorithm for the Frequent Words Problem to the concatenation of these strings will immediately reveal the most frequent 15-mer shown below as the implanted pattern. Since these short strings were randomly generated, it is unlikely that they contain other frequent 15-mers.

    1 "atgaccgggatactgatAAAAAAAAGGGGGGGggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccg"
    2 "acccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataAAAAAAAAGGGGGGGa"
    3 "tgagtatccctgggatgacttAAAAAAAAGGGGGGGtgctctcccgatttttgaatatgtaggatcattcgccagggtccga"
    4 "gctgagaattggatgAAAAAAAAGGGGGGGtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggaga"
    5 "tcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaatAAAAAAAAGGGGGGGcttatag"
    6 "gtcaatcatgttcttgtgaatggatttAAAAAAAAGGGGGGGgaccgcttggcgcacccaaattcagtgtgggcgagcgcaa"
    7 "cggttttggcccttgttagaggcccccgtAAAAAAAAGGGGGGGcaattatgagagagctaatctatcgcgtgcgtgttcat"
    8 "aacttgagttAAAAAAAAGGGGGGGctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgta"
    9 "ttggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcatAAAAAAAAGGGGGGGaccgaaagggaag"
    10 "ctggtgagcaacgacagattcttacgtgcattagctcgcttccggggatctaatagcacgaagcttAAAAAAAAGGGGGGGa"




Now imagine that instead of implanting exactly the same pattern into all sequences, we mutate the pattern before inserting it into each sequence by randomly changing the nucleotides at four randomly selected positions within each implanted 15-mer, as shown below.

    1 "atgaccgggatactgatAgAAgAAAGGttGGGggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccg"
    2 "acccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaatacAAtAAAAcGGcGGGa"
    3 "tgagtatccctgggatgacttAAAAtAAtGGaGtGGtgctctcccgatttttgaatatgtaggatcattcgccagggtccga"
    4 "gctgagaattggatgcAAAAAAAGGGattGtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggaga"
    5 "tcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaatAtAAtAAAGGaaGGGcttatag"
    6 "gtcaatcatgttcttgtgaatggatttAAcAAtAAGGGctGGgaccgcttggcgcacccaaattcagtgtgggcgagcgcaa"
    7 "cggttttggcccttgttagaggcccccgtAtAAAcAAGGaGGGccaattatgagagagctaatctatcgcgtgcgtgttcat"
    8 "aacttgagttAAAAAAtAGGGaGccctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgta"
    9 "ttggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcatActAAAAAGGaGcGGaccgaaagggaag"
    10 "ctggtgagcaacgacagattcttacgtgcattagctcgcttccggggatctaatagcacgaagcttActAAAAAGGaGcGGa"

Applying our solution to the Frequent Words Problem is no longer going to help us, since AAAAAAAAGGGGGGG does not even appear in the sequences above. Perhaps, then, we could apply our solution to the Frequent Words with Mismatches Problem. However, in Chapter 1, we implemented an algorithm for the Frequent Words with Mismatches Problem aimed at finding hidden messages with a small number of mismatches and a small k-mer size (e.g., one or two mismatches for DnaA boxes of length 9). This algorithm is likely to become too slow when searching for the implanted motif above, which is longer and has more mutations.

***Furthermore, the Frequent Words Problem is inadequate because it does not correctly model the biological problem of motif finding. A DnaA box is a pattern that clumps, or appears frequently, within a relatively short interval of the genome. In contrast, a regulatory motif is a pattern that appears at least once (perhaps with variation) in each of many different regions that are scattered throughout the genome.***

Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches. For example, the implanted 15-mer in the strings above represents a (15,4)-motif.

## Section 02
### MotifEnumeration
    Implanted Motif Problem: Find all (k, d)-motifs in a collection of strings.

    Input: A collection of strings Dna, and integers k and d.
    Output: All (k, d)-motifs in Dna.

Example:

    Sample Input:
    
        3 1
        ATTTGGC
        TGCCTTA
        CGGTATC
        GAAAATT
    
    Sample Output:
    
        ATA ATT GTT TTT


MotifEnumeration is unfortunately rather slow for large values of k and d, and so we will try a different approach instead. Maybe we can detect an implanted pattern simply by identifying the two most similar k-mers between each pair of strings in Dna? However, consider the implanted 15-mers AgAAgAAAGGttGGG and cAAtAAAAcGGGGcG, each of which differs from AAAAAAAAGGGGGGG by four mismatches. Although these 15-mers look similar to the correct motif AAAAAAAAGGGGGGG, they are not so similar when compared to each other, having eight mismatches:

    AgAAgAAAGGttGGG
    || ||   | || | 
    cAAtAAAAcGGGGcG 

Since these two implanted patterns are so different, we should be concerned whether we will be able to find them by searching for the two similar k-mers among pairs of strings in Dna.

## Section 03
A more appropriate problem formulation would score individual instances of motifs depending on how similar they are to an “ideal” motif (i.e., a transcription factor binding site that binds the best to the transcription factor). However, since the ideal motif is unknown, we attempt to select a k-mer from each string and score these k-mers depending on how similar they are to each other.

To define scoring, consider a list of t DNA strings Dna, where each string has length n, and select a k-mer from each string to form a collection Motifs, which we represent as a t x k motif matrix. In the figure below, which shows the motif matrix for the NF-κB binding sites from the figure below, we indicate the most frequent nucleotide in each column of the motif matrix by upper case letters. If there are multiple most frequent nucleotides in a column, then we arbitrarily select one of them to break the tie. Note that positions 2 and 3 are the most conserved (nucleotide G is completely conserved in these positions), whereas position 10 is the least conserved.

### Motif 

Our goal is to select k-mers resulting in the most “conserved” motif matrix, meaning the matrix with the most upper case letters (and thus the fewest number of lower case letters). Leaving aside the question of how we select such k-mers, we will first focus on how to score the resulting motif matrices, defining **Score(Motifs) as the number of unpopular (lower case) letters in the motif matrix Motifs** . Our goal is to find a collection of k-mers that minimizes this score.

We can construct the 4 × k count matrix **Count(Motifs) counting the number of occurrences of each nucleotide in each column of the motif matrix;** the (i, j)-th element of Count(Motifs) stores the number of times that nucleotide i appears in column j of Motifs. We will further divide all of the elements in the count matrix by t, the number of rows in Motifs. This results in a profile matrix P = **Profile(Motifs) for which Pi,j is the frequency of the i-th nucleotide in the j-th column of the motif matrix.** *Note that the elements of any column of the profile matrix sum to 1*. The figure below shows the motif, count, and profile matrices for the NF-κB binding sites.

Finally, we form a consensus string, denoted **Consensus(Motifs), from the most popular letters in each column of the motif matrix.** If we select Motifs correctly from the collection of upstream regions, then Consensus(Motifs) provides an ideal candidate regulatory motif for these regions. For example, the consensus string for the NF-κB binding sites in the figure below is TCGGGGATTTCC.


![motif](http://bioinformaticsalgorithms.com/images/Motifs/motifs_score_count_profile_consensus.png)

Every column of Profile(Motifs) corresponds to a probability distribution, or a collection of nonnegative numbers that sum to 1. For example, the 2nd column in the profile matrix for the NF-κB binding sites corresponds to the probabilities 0.2, 0.6, 0.0, and 0.2 for A, C, G, and T, respectively.

**Entropy is a measure of the uncertainty of a probability distribution (p1, …, pN), and is defined as follows:
H(p1,…,pN)=− ∑(i=1, N) (pi⋅log2pi)**

For example, the entropy of the probability distribution (0.2, 0.6, 0.0, 0.2) corresponding to the 2nd column of the NF-κB profile matrix is 1.371. whereas the entropy of the more conserved final column (0.0, 0.6, 0.0, 0.4) is 0.971. and the entropy of the very conserved 5th column (0.0, 0.0, 0.9, 0.1) is 0.467

The entropy of the completely conserved third column is 0, which is the minimum possible entropy. On the other hand, a column with equally-likely nucleotides (all probabilities equal to 1/4) has maximum possible entropy −4 · 1/4 · log2(1/4) = 2. In general, the more conserved the column, the smaller its entropy. Thus, entropy offers an improved method of scoring motif matrices: the entropy of a motif matrix is defined as the sum of the entropies of its columns. In this book, we will continue to use Score(Motifs) for simplicity, but the entropy score is used more often in practice.

    This function takes a matrix of motifs, and compute information
    Note: give an array of strings, each string is the COLUMN of the matrix NOT row!(fix later)
    
    Input: A collection of strings Dna
    Output: consensus, score, count, profile, entropy, entropies 
 
## Section 04
Given a collection of k-mers Motifs = {Motif1, … , Motif_t} and a k-mer Pattern, we now define d(Pattern, Motifs) as the sum of Hamming distances between Pattern and each Motif_i:
d(Pattern,Motifs)=∑(i=1,t) HammingDistance(Pattern,Motif_i). 

Because Score(Motifs) corresponds to counting the lower case elements of Motifs column-by-column and d(Consensus(Motifs), Motifs) corresponds to counting these elements row-by-row, we obtain that **Score(Motifs) = d(Consensus(Motifs), Motifs).**

This equation gives us an idea. Instead of searching for a collection of k-mers Motifs minimizing **Score(Motifs)** let's instead search for a potential consensus string Pattern minimizing **d(Pattern, Motifs)** among all possible k-mers Pattern and all possible choices of k-mers Motifs in Dna. This problem is equivalent to the Motif Finding Problem.


nstead of having to search for all Motifs, we now have to search all Motifs as well as all k-mers Pattern. The key observation for solving the Equivalent Motif Finding Problem is that, given Pattern, we don’t need to explore all possible collections Motifs in order to minimize d(Pattern, Motifs).

To explain how this can be done, we define Motifs(Pattern, Dna) as a collection of k-mers that minimizes d(Pattern, Motifs) for a given Pattern and all possible sets of k-mers Motifs in Dna. For example, for the strings Dna shown below, the five colored 3-mers represent Motifs(AAA, Dna).

![median_String1](http://bioinformaticsalgorithms.com/images/Motifs/median_string_1.png)



The reason why we don’t need to consider all possible collections Motifs in Dna = Dna1, ..., Dnat is that we can generate the k-mers in Motifs(Pattern, Dna) one at a time; that is, we can select a k-mer in Dnai independently of selecting k-mers in all other strings in Dna. Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to denote the minimum Hamming distance between Pattern and any k-mer in Text,
d(Pattern,Text)=min of all k-mers Pattern’ in Text (HammingDistance(Pattern,Pattern′). For example, d(GATTCTCA, GCAAAGACGCTGACCAA) = 3.

A k-mer in Text that achieves the minimum Hamming distance with Pattern is denoted Motif(Pattern, Text). For the above example, Motif(GATTCTCA, GCAAAGACGCTGACCAA) = GACGCTGA.

Given a k-mer Pattern and a set of strings Dna = {Dna1, … , Dna_t}, we define d(Pattern, Dna) as the sum of distances between Pattern and all strings in Dna,
d(Pattern,Dna)=∑(i=1, t)d(Pattern,Dnai). For example, for the strings Dna shown below, d(AAA, Dna) = 1 + 1 + 2 + 0 + 1 = 5.


![median_String2](http://bioinformaticsalgorithms.com/images/Motifs/median_string_2.png)

### Median String

Our goal is to find a k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern, the same task that the Equivalent Motif Finding Problem is trying to achieve. We call such a k-mer a median string for Dna.

    Median String Problem: Find a median string.

    Input: A collection of strings Dna and an integer k.
    Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers.

Example:

    Sample Input:
    
        3
        AAATTGACGCAT
        GACGACCACGTT
        CGTCAGCGCCTG
        GCTGAGCACCGG
        AGTTCGGGACAG
    
    Sample Output:
    
        GAC
    
## Section 05
In this section, we will explore a greedy approach to motif finding. Again, let Motifs be a collection of k-mers taken from t strings Dna. Recall from our discussion of entropy that we can view each column of Profile(Motifs) as a four-sided biased die. Thus, a profile matrix with k columns can be viewed as a collection of k dice, which we will roll to randomly generate a k-mer. For example, if the first column of the profile matrix is (0.2, 0.1, 0.0, 0.7), then we generate A as the first nucleotide with probability 0.2, C with probability 0.1, G with probability 0.0, and T with probability 0.7.

Below, we reproduce the profile matrix for the NF-κB binding sites, where the lone colored entry in the i-th column corresponds to the i-th nucleotide in ACGGGGATTACC. The probability Pr(ACGGGGATTACC | Profile) that Profile generates ACGGGGATTACC is computed by simply multiplying the highlighted entries in the profile matrix.

![profile_most](http://bioinformaticsalgorithms.com/images/Motifs/probability_random_string.png)

### Profile-most Probable k-mer
    Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.

    Input: A string Text, an integer k, and a 4 × k matrix Profile.
    Output: A Profile-most probable k-mer in Text.

Example:

    Sample Input:
    
        ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
        5
        0.2 0.2 0.3 0.2 0.3
        0.4 0.3 0.1 0.5 0.1
        0.3 0.3 0.5 0.2 0.4
        0.1 0.2 0.1 0.1 0.2
    
    Sample Output:
    
        CCGAG
        
### GreedyMotifSearch

    Code Challenge: Implement GreedyMotifSearch.

    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

Example:

    Sample Input:
    
        3 5
        GGCGTTCAGGCA
        AAGAATCAGTCA
        CAAGGAGTTCGC
        CACGTCAATCAC
        CAATAATATTCG
    
    Sample Output:
    
        CAG
        CAG
        CAA
        CAA
        CAA
## Section 06
consider the following Profile.

![pseudocounts](http://bioinformaticsalgorithms.com/images/Motifs/greedy_profile_1.png)

The fourth symbol of TCGTGGATTTCC causes Pr(TCGTGGATTTCC, Profile) to be equal to zero. As a result, the entire string is assigned a zero probability, even though TCGTGGATTTCC differs from the consensus string at only one position. For that matter, TCGTGGATTTCC has the same low probability as AAATCTTGGAA, which is very different from the consensus string.

In order to improve this unfair scoring, bioinformaticians often substitute zeroes with small numbers called pseudocounts. The simplest approach to introducing pseudocounts, called Laplace’s Rule of Succession. In the case of motifs, pseudocounts often amount to adding 1 (or some other small number) to each element of Count(Motifs). For example, say we have the following motif, count, and profile matrices:

![pseudocounts2](http://bioinformaticsalgorithms.com/images/Motifs/greedy_profile_2.png)

Laplace’s Rule of Succession adds 1 to each element of Count(﻿Motifs), updating the two matrices to the following:

![pseudocounts2](http://bioinformaticsalgorithms.com/images/Motifs/greedy_profile_3.png)


### Greedy Motif Search with pseudocounts
    Code Challenge: Implement GreedyMotifSearch with pseudocounts.

    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t) with pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

Example:

    Sample Input:
    
        3 5
        GGCGTTCAGGCA
        AAGAATCAGTCA
        CAAGGAGTTCGC
        CACGTCAATCAC
        CAATAATATTCG
    
    Sample Output:
    
        TTC
        ATC
        TTC
        ATC
        TTC
## Section 07
### RandomizedMotifSearch
    Code Challenge: Implement RandomizedMotifSearch.

    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times. Remember to use pseudocounts!

Example:

    Sample Input:
        
        8 5
        CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
        GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
        TAGTACCGAGACCGAAAGAAGTATACAGGCGT
        TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
        AATCCACCAGCTCCACGTGCAATGTTGGCCTA
    
    Sample Output:
    
        TCTCGGGG
        CCAAGGTG
        TACAGGCG
        TTCAGGTG
        TCCACGTG

## Section 09
### GibbsSampler

Note that RandomizedMotifSearch may change all t strings Motifs in a single iteration. This strategy may prove reckless, since some correct motifs (captured in Motifs) may potentially be discarded at the next iteration. GibbsSampler is a more cautious iterative algorithm that discards a single k-mer from the current set of motifs at each iteration and decides to either keep it or replace it with a new one. This algorithm thus moves with more caution in the space of all motifs, as illustrated below.


![random_gibbs](http://bioinformaticsalgorithms.com/images/Motifs/randomized_vs_gibbs.png)


    Code Challenge: Implement GibbsSampler.

    Input: Integers k, t, and N, followed by a collection of strings Dna.
    Output: The strings BestMotifs resulting from running GibbsSampler(Dna, k, t, N) with 20 random starts. Remember to use pseudocounts!

Example:

    Sample Input:
    
        8 5 100
        CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA
        GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
        TAGTACCGAGACCGAAAGAAGTATACAGGCGT
        TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
        AATCCACCAGCTCCACGTGCAATGTTGGCCTA
    
    Sample Output:
    
        TCTCGGGG
        CCAAGGTG
        TACAGGCG
        TTCAGGTG
        TCCACGTG
        
## Section 12
### DistanceBetweenPatternAndStrings
    Code Challenge: Implement DistanceBetweenPatternAndStrings.

    Input: A string Pattern followed by a collection of strings Dna.
    Output: d(Pattern, Dna).

Example:

    Sample Input:
    
        AAA
        TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT
    
    Sample Output:
    
        5
        
# CHAPTER 3: How Do We Assemble Genomes?
**This chapter is about assembling DNA**

First, DNA is double-stranded, and we have no way of knowing a priori which strand a given read derives from, meaning that we will not know whether to use a read or its reverse complement when assembling a particular strand of a genome. Second, modern sequencing machines are not perfect, and the reads that they generate often contain errors. Sequencing errors complicate genome assembly because they prevent us from identifying all overlapping reads. Third, some regions of the genome may not be covered by any reads, making it impossible to reconstruct the entire genome.

Since the reads generated by modern sequencers often have the same length, we may safely assume that reads are all k-mers for some value of k. The first part of this chapter will assume an ideal — and unrealistic — situation in which all reads come from the same strand, have no errors, and exhibit perfect coverage, so that every k-mer substring of the genome is generated as a read. Later, we will show how to relax these assumptions for more realistic datasets.

## Section 02: 
### String Composition 
Given a string Text, its k-mer composition Composition_k(Text) is the collection of all k-mer substrings of Text (including repeated k-mers). For example, Composition_3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}.
*Note that we have listed k-mers in lexicographic order (i.e., how they would appear in a dictionary) rather than in the order of their appearance in TATGGGGTGC. We have done this because the correct ordering of the reads is unknown when they are generated.*
    
    String Composition Problem: Generate the k-mer composition of a string.

    Input: An integer k and a string Text.
    Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.
    
Example:
    
    Sample Input:
    
        5
        CAATCCAAC
    
    Sample Output:
    
        CAATC
        AATCC
        ATCCA
        TCCAA
        CCAAC
        
let’s consider an additional 3-mer composition:

    AAT  ATG  ATG  ATG  CAT  CCA  GAT  GCC  GGA  GGG  GTT  TAA  TGC  TGG  TGT
The difficulty in assembling this simulated genome arises because ATG is repeated three times in the 3-mer composition, which causes us to have the three choices TGG, TGC, and TGT by which to extend ATG. Repeated substrings in the genome are not a serious problem when we have just 15 reads, but with millions of reads, repeats make it much more difficult to "look ahead" and construct the correct assembly.

If you followed our discussion of finding the origin of replication in bacterial genomes, you know how unlikely it is to witness a long repeat in a randomly generated sequence of nucleotides. You also know that real genomes are anything but random. Indeed, approximately 50% of the human genome is made up of repeats, e.g., the approximately 300 nucleotide-long Alu sequence is repeated over a million times, with only a few nucleotides inserted/deleted/substituted each time

## Section 03
In the figure below, consecutive 3-mers in TAATGCCATGGGATGTT are linked together to form this string's genome path.


![genome_path](http://bioinformaticsalgorithms.com/images/Assembly/path_graph.png)


### String Spelled by a Genome Path
    String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.

    Input: A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
    Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).

Example:

    Sample Input:
    
        ACCGA
        CCGAA
        CGAAG
        GAAGC
        AAGCT
    
    Sample Output:
    
        ACCGAAGCT
        
###  Overlap Graph
In this chapter, we will use the terms prefix and suffix to refer to the first k − 1 nucleotides and last k − 1 nucleotides of a k-mer, respectively. For example, Prefix(TAA) = TA and Suffix(TAA) = AA. We note that the suffix of a 3-mer in the genome path is equal to the prefix of the following 3-mer in the path. For example, Suffix(TAA) = Prefix(AAT) = AA in the genome path for TAATGCCATGGGATGTT.

If we strictly follow the rule of connecting two 3-mers with an arrow every time the suffix of one is equal to the prefix of the other, then we will connect all consecutive 3-mers in TAATGCCATGGGATGTT. However, because we don’t know this genome in advance, we wind up having to connect many other pairs of 3-mers as well. For example, each of the three occurrences of ATG should be connected to TGC, TGG, and TGT.

    Overlap Graph Problem: Construct the overlap graph of a collection of k-mers.

    Input: A collection Patterns of k-mers.
    Output: The overlap graph Overlap(Patterns).

Example:

    Sample Input:
    
        ATGCG
        GCATG
        CATGC
        AGGCA
        GGCAT
        GGCAC
    
    Sample Output:
    
        CATGC -> ATGCG
        GCATG -> CATGC
        GGCAT -> GCATG
        AGGCA -> GGCAC,GGCAT

### k-Universal linear String 
A binary string is a string composed only of 0’s and 1’s; a binary string is k-universal if it contains every binary k-mer exactly once. For example, 0001110100 is a 3-universal string, as it contains each of the eight binary 3-mers (000, 001, 011, 111, 110, 101, 010, and 100) exactly once.

    Code Challenge: Solve the k-Universal Circular String Problem.

    Input: An integer k.
    Output: A k-universal linear string.

Example:

    Sample Input:
    
        4
    
    Sample Output:
    
        0000100110101111000

## Section 04
In general, given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text. The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).
### De Bruijn Graph from a String
    De Bruijn Graph from a String Problem: Construct the de Bruijn graph of a string.

    Input: An integer k and a string Text.
    Output: DeBruijnk(Text).

Example:

    Sample Input:
    
        4
        AAGATTCTCTAAGA
    
    Sample Output:
    
        AAG -> AGA,AGA
        AGA -> GAT
        ATT -> TTC
        CTA -> TAA
        CTC -> TCT
        GAT -> ATT
        TAA -> AAG
        TCT -> CTA,CTC
        TTC -> TCT
## Section 05
### DeBruijn Graph from k-mers 
    DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.

    Input: A collection of k-mers Patterns.
    Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
    
Example:

    Sample Input:
    
        GAGG
        CAGG
        GGGG
        GGGA
        CAGG
        AGGG
        GGAG
    
    Sample Output:
    
        AGG -> GGG
        CAG -> AGG,AGG
        GAG -> AGG
        GGA -> GAG
        GGG -> GGA,GGG
        
        
**We now have two ways of solving the String Reconstruction Problem. We can either find a Hamiltonian path in the overlap graph  or find an Eulerian path in the de Bruijn graph. Hamiltorian is NP but Euler is P so we go with Euler's solution**

## Section 08
### Eulerian Cycle Problem
    Eulerian Cycle Problem: Find an Eulerian cycle in a graph.

    Input: A graph.
    Output: An Eulerian cycle in this graph, if one exists.
    
Example:

    Sample Input:
    
        0 -> 3
        1 -> 0
        2 -> 1,6
        3 -> 2
        4 -> 2
        5 -> 4
        6 -> 5,8
        7 -> 9
        8 -> 7
        9 -> 6
    
    Sample Output:
    
        6->8->7->9->6->5->4->2->1->0->3->2->6
        
### Eulerian Path Problem
    Code Challenge: Solve the Eulerian Path Problem.

    Input: The adjacency list of a directed graph that has an Eulerian path.
    Output: An Eulerian path in this graph.

Example:

    Sample Input:
    
        0 -> 2
        1 -> 3
        2 -> 1
        3 -> 0,4
        6 -> 3,7
        7 -> 8
        8 -> 9
        9 -> 6
    
    Sample Output:
    
        6->7->8->9->6->3->0->2->1->3->4
        
### StringReconstruction
    Code Challenge: Solve the String Reconstruction Problem.

    Input: An integer k followed by a list of k-mers Patterns.
    Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

Example:

    Sample Input:
        
        4
        CTTA
        ACCA
        TACC
        GGCT
        GCTT
        TTAC
    
    Sample Output:
    
        GGCTTACCA

### k-Universal Circular String 

    Code Challenge: Solve the k-Universal Circular String Problem.

    Input: An integer k.
    Output: A k-universal circular string.

Example:

    Sample Input:
    
        4
    
    Sample Output:
    
        0000110010111101
        
## Section 09
Previously, we described an idealized form of genome assembly in order to build up your intuition about de Bruijn graphs. In the rest of the chapter, we will discuss a number of practically motivated topics that will help you appreciate the advanced methods used by modern assemblers.

We have already mentioned that assembling reads sampled from a randomly generated text is trivial, since random strings are not expected to have long repeats. Moreover, de Bruijn graphs become less and less tangled when read length increases (see the figure below). As soon as read length exceeds the length of all repeats in a genome (provided the reads have no errors), the de Bruijn graph turns into a path. However, despite many attempts, biologists have not yet figured out how to generate long and accurate reads. The most accurate sequencing technologies available today generate reads that are only about 300 nucleotides long, which is too short to span most repeats, even in short bacterial genomes.

We saw earlier that the string TAATGCCATGGGATGTT cannot be uniquely reconstructed from its 3-mer composition since another string (TAATGGGATGCCATGTT) has the same 3-mer composition.

Increasing read length would help identify the correct assembly, but since increasing read length presents a difficult experimental problem, biologists have devised an ingenious experimental approach to increase read length by generating read-pairs, which are pairs of reads separated by a fixed distance d in the genome (see figure below). You can think about a read-pair as a long “gapped" read of length k + d + k whose first and last k-mers are known but whose middle segment of length d is unknown. Nevertheless, read-pairs contain more information than k-mers alone, and so we should be able to use them to improve our assemblies. If only you could infer the nucleotides in the middle segment of a read-pair, you would immediately increase the read length from k to 2 · k + d.

Given a string Text, a (k,d)-mer is a pair of k-mers in Text separated by distance d. We use the notation (Pattern1|Pattern2) to refer to a (k,d)-mer whose k-mers are Pattern1 and Pattern2. For example, (AAT|TGG) is a (3,4)-mer in TAATGCCATGGGATGTT. The (k,d)-mer composition of Text, denoted PairedComposition_k,d(Text), is the collection of all (k,d)- mers in Text (including repeated (k,d)-mers). 

### String Reconstruction from Read-Pairs
Note that while there are repeated 3-mers in the 3-mer composition of this string, there are no repeated (3,1)-mers in its paired composition. Furthermore, although TAATGCCATGGGATGTT and TAATGGGATGCCATGTT have the same 3-mer composition, they have different (3,1)-mer compositions. Thus, if we can generate the (3,1)-mer composition of these strings, then we will be able to distinguish between them

    String Reconstruction from Read-Pairs Problem: Reconstruct a string from its paired composition.

    Input: A collection of paired k-mers PairedReads and an integer d.
    Output: A string Text with (k,d)-mer composition equal to PairedReads (if such a string exists).

Example:

    Sample Input:
    
        4 2
        GAGA|TTGA
        TCGT|GATG
        CGTG|ATGT
        TGGT|TGAG
        GTGA|TGTT
        GTGG|GTGA
        TGAG|GTTG
        GGTC|GAGA
        GTCG|AGAT
    
    Sample Output:
    
        GTGGTCGTGAGATGTTGA
        
## Section 10

First, given a k-mer substring of a genome, we define its coverage as the number of reads to which this k-mer belongs.

There is also a sense of coverage in terms of how well a collection of sequencing reads "cover" the genome.  We have previously taken for granted that a sequencing machine can generate all k-mers present in the genome, but this assumption of "perfect coverage" does not hold in practice. For example, the popular Illumina sequencing technology generates reads that are approximately 300 nucleotides long, but this technology still misses many 300-mers present in the genome (even if the average coverage is very high), and nearly all the reads that it does generate have sequencing errors.  How, then, can we use these reads effectively?

The left part of the figure below shows four 10-mer reads that capture some but not all of the 10-mers from an example genome. However, if we take the counterintuitive step of breaking these reads into shorter 5-mers (figure below, right), then these 5-mers exhibit perfect coverage. This read breaking approach, in which we break reads into shorter k-mers, is used by many modern assemblers.


![read_break](http://bioinformaticsalgorithms.com/images/Assembly/read_breaking.png)

Read breaking must deal with a practical trade-off. On the one hand, the smaller the value of k, the larger the chance that the k-mer coverage is perfect. On the other hand, smaller values of k result in a more tangled de Bruijn graph, making it difficult to infer the genome from this graph.

Even after read breaking, most assemblies still have gaps in k-mer coverage, causing the de Bruijn graph to have missing edges, and so the search for an Eulerian path fails. In this case, biologists often settle on assembling contigs (long, contiguous segments of the genome) rather than entire chromosomes. For example, a typical bacterial sequencing project may result in about a hundred contigs, ranging in length from a few thousand to a few hundred thousand nucleotides. For most genomes, the order of these contigs along the genome remains unknown. 

Fortunately, we can derive contigs from the de Bruijn graph. A path in a graph is called non-branching if in(v) = out(v) = 1 for each intermediate node v of this path, i.e., for each node except possibly the starting and ending node of a path. A maximal non-branching path is a non-branching path that cannot be extended into a longer non-branching path.

We are interested in these paths because the strings of nucleotides that they spell out must be present in any assembly with a given k-mer composition. 

Error-prone reads represent yet another barrier to real sequencing projects. Adding the single erroneous read CGTACGGACA (with a single error that misreads T as C) to the set of "broken" 5-mer reads from earlier in the lesson results in erroneous 5-mers CGTAC, GTACG, TACGG, ACGGA, and CGGAC after read breaking. These 5-mers result in an erroneous path from node CGTA to node GGAC in the de Bruijn graph below, meaning that if the correct read CGTATGGACA is generated as well, then we will have two paths connecting CGTA to GGAC in the de Bruijn graph. This structure is called a bubble, which we define as two short disjoint paths (e.g., shorter than some threshold length) connecting the same pair of nodes in the de Bruijn graph.

Existing assemblers remove bubbles from de Bruijn graphs. The practical challenge is that, since nearly all reads have errors, de Bruijn graphs have millions of bubbles (see below).

Bubble removal occasionally removes the correct path, thus introducing errors rather than fixing them. To make matters worse, in a genome having inexact repeats, where the repeated regions differ by a single nucleotide or some other small variation, reads from the two repeat copies will also generate bubbles in the de Bruijn graph because one of the copies may appear to be an erroneous version of the other. Applying bubble removal to these regions introduces assembly errors by making repeats appear more similar than they are. Thus, modern genome assemblers attempt to distinguish bubbles caused by sequencing errors (which should be removed) from bubbles caused by variations (which should be retained).

Next, while the de Bruijn graph framework requires that we know the multiplicity of each k-mer in the genome (i.e., the number of times the k-mer appears), this information is not readily available from reads. However, the multiplicity of a k-mer in a genome can often be estimated using its coverage. Indeed, k-mers that appear t times in a genome are expected to have approximately t times higher coverage than k-mers that appear just once. Needless to say, coverage varies across the genome, and this condition is often violated. As a result, existing assemblers often assemble repetitive regions in genomes without knowing the exact number of times each k-mer from this region occurs in the genome.
### Contig Generation 
    Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).

    Input: A collection of k-mers Patterns.
    Output: All contigs in DeBruijn(Patterns).

Example:

    Sample Input:
    
        ATG
        ATG
        TGT
        TGG
        CAT
        GGA
        GAT
        AGA
    
    Sample Output:
    
        AGA ATG ATG CAT GAT TGGA TGT

## Section 13
### String Spelled by a Gapped Genome Path 
    String Spelled by a Gapped Genome Path Problem: Reconstruct a sequence of (k, d)-mers corresponding to a path in a paired de Bruijn graph.

    Input: A sequence of (k, d)-mers (a1|b1), ..., (an|bn) such that Suffix((ai|bi)) = Prefix((ai+1|bi+1)) for 1 ≤ i ≤ n - 1.
    Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer of Text is equal to (ai|bi) for 1 ≤ i ≤ n (if such a string exists).

Example:

    Sample Input:
    
        4 2
        GACC|GCGC
        ACCG|CGCC
        CCGA|GCCG
        CGAG|CCGG
        GAGC|CGGA
    
    Sample Output:
    
        GACCGAGCGCCGGA
        
## Section 14
### MaximalNonBranchingPaths
    Code Challenge: Implement MaximalNonBranchingPaths.

    Input: The adjacency list of a graph whose nodes are integers.
    Output: The collection of all maximal nonbranching paths in this graph.

Example:

    Sample Input:
    
        1 -> 2
        2 -> 3
        3 -> 4,5
        6 -> 7
        7 -> 6
    
    Sample Output:
    
        1 -> 2 -> 3
        3 -> 4
        3 -> 5
        7 -> 6 -> 7
        
# CHAPTER 4: How Do We Sequence Antibiotics?
**this chapter is about sequencing peptides**

Let’s begin by considering Tyrocidine B1, one of many antibiotics produced by Bacillus brevis. Tyrocidine B1 is defined by the 10 amino acid-long sequence shown below (using both the one-letter and three-letter notations for amino acids). Our goal in this section is to figure out how Bacillus brevis could have made this antibiotic.
    
    Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr
    V   K   L   F   P   W   F   N   Q   Y
    
The Central Dogma of Molecular Biology states that “DNA makes RNA makes protein.” According to the Central Dogma, a gene from a genome is first transcribed into a strand of RNA composed of four ribonucleotides: adenine, guanine, cytosine, and uracil. A strand of RNA can be represented as an RNA string, formed over the four-letter alphabet {A, C, G, U}. Then, the RNA transcript is translated into an amino acid sequence of a protein.

Transcription simply transforms a DNA string into an RNA string by replacing all occurrences of T with U. The resulting strand of RNA is translated into an amino acid sequence as follows. During translation, the RNA strand is partitioned into non-overlapping 3-mers called codons. Then, each codon is converted into one of 20 amino acids via the genetic code; the resulting sequence can be represented as an amino acid string formed over a 20-letter alphabet.     
## Section 02

### Protein Translation
    Protein Translation Problem: Translate an RNA string into an amino acid string.

    Input: An RNA string Pattern and the array GeneticCode.
    Output: The translation of Pattern into an amino acid string Peptide.

Example:

    Sample Input:
    
        AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
    
    Sample Output:
    
        MAMAPRTEINSTRING
        
### Peptide Encoding 
Thousands of different DNA 30-mers could code for Tyrocidine B1, and we would like to know which one appears in the Bacillus brevis genome. There are three different ways to divide a DNA string into codons for translation, one starting at each of the first three starting positions of the string. These different ways of dividing a DNA string into codons are called reading frames. Since DNA is double-stranded, a genome has six reading frames (three on each strand), as shown in the figure below.

![reading_frames](http://bioinformaticsalgorithms.com/images/Antibiotics/reading_frames.png)

We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide. For example, the DNA string GAAACT is transcribed into GAAACU and translated into ET. The reverse complement of this DNA string, AGTTTC, is transcribed into AGUUUC and translated into SF. Thus, GAAACT encodes both ET and SF.

    Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.

    Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    Output: All substrings of Text encoding Peptide (if any such substrings exist).
    
Example:

    Sample Input:
    
        ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
        MA
        
    Sample Output:
        
        ATGGCC
        GGCCAT
        ATGGCC    
        
## Section 04
The workhorse of peptide sequencing is the mass spectrometer, an expensive molecular scale that shatters molecules into pieces and then weighs the resulting fragments. The mass spectrometer measures the mass of a molecule in daltons (Da); 1 Da is approximately equal to the mass of a single nuclear particle (i.e., a proton or neutron).

We will approximate the mass of a molecule by simply adding the number of protons and neutrons found in the molecule’s constituent atoms, which yields the molecule’s integer mass. 

 the resulting experimental spectrum contains the masses of all possible linear fragments of the peptide, which are called subpeptides. For example, the cyclic peptide NQEL has 12 subpeptides: N, Q, E, L, NQ, QE, EL, LN, NQE, QEL, ELN, and LNQ. We will also assume that subpeptides may occur more than once if an amino acid occurs multiple times in the peptide (e.g., ELEL also has 12 subpeptides: E, L, E, L, EL, LE, EL, LE, ELE, LEL, ELE, and LEL.
 
### Count Cyclic Peptides
    Exercise Break: How many subpeptides does a cyclic peptide of length n have?
    
Example:
    
    Sample Input:
    
        31315
    
    Sample Output:
    
        980597910


### Theoretical Spectrum
The theoretical spectrum of a cyclic peptide Peptide, denoted Cyclospectrum(Peptide), is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the mass of the entire peptide, with masses ordered from smallest to largest. We will assume that the theoretical spectrum can contain duplicate elements, as is the case for NQEL (shown below), where NQ and EL have the same mass.

![Cyclospectrum](http://bioinformaticsalgorithms.com/images/Antibiotics/duplicate_elements.png)

    Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.

    Input: An amino acid string Peptide.
    Output: Cyclospectrum(Peptide).

Example:

    Sample Input:
    
        LEQN
    
    Sample Output:
    
        0 113 114 128 129 227 242 242 257 355 356 370 371 484
        
## Section 05
### Counting Peptides with Given Mass
    Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass.

    Input: An integer m.
    Output: The number of linear peptides having integer mass m.

Example:

    Sample Input:
    
        1024
    
    Sample Output:
    
        14712706211
        

## Section 06

More generally, brute force algorithms that enumerate all candidate solutions but discard large subsets of hopeless candidates by using various consistency conditions are known as branch-and-bound algorithms. Each such algorithm consists of a branching step to increase the number of candidate solutions, followed by a bounding step to remove hopeless candidates. In our branch-and-bound algorithm for the Cyclopeptide Sequencing Problem, the branching step will extend each candidate peptide of length k into 18 peptides of length k + 1, and the bounding step will remove inconsistent peptides from consideration.

### Count Linear Peptides
    Exercise Break: How many subpeptides does a linear peptide of given length n have? (Include the empty peptide and the entire peptide.)

Example:

    Sample Input:
    
        4
    
    Sample Output:
    
        11

### Cyclopeptide Sequencing
Given an experimental spectrum Spectrum of a cyclic peptide, a linear peptide is consistent with Spectrum if every mass in its theoretical spectrum is contained in Spectrum. If a mass appears more than once in the theoretical spectrum of the linear peptide, then it must appear at least that many times in Spectrum in order for the linear peptide to be consistent with Spectrum. For example, a linear peptide can still be consistent with the theoretical spectrum of NQEL if the peptide’s spectrum contains 242 twice. But it cannot be consistent with the theoretical spectrum of NQEL if its spectrum contains 113 twice.

    Cyclopeptide Sequencing Problem: Given an ideal spectrum, find a cyclic peptide whose theoretical spectrum matches the experimental spectrum.

    Input: A collection of (possibly repeated) integers Spectrum corresponding to an ideal spectrum.
    Output: An amino acid string Peptide such that Cyclospectrum(Peptide) = Spectrum (if such a string exists).

Example:

    Sample Input:
    
        0 113 128 186 241 299 314 427
    
    Sample Output:
    
        186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186

## Section 07
Although CyclopeptideSequencing successfully reconstructed Tyrocidine B1, this algorithm only works in the case of an ideal spectrum, i.e., when the experimental spectrum of a peptide coincides exactly with its theoretical spectrum. This inflexibility of CyclopeptideSequencing presents a practical barrier, since mass spectrometers generate "noisy" spectra that are far from ideal — they are characterized by having both false masses and missing masses. A false mass is present in the experimental spectrum but absent from the theoretical spectrum; a missing mass is present in the theoretical spectrum but absent from the experimental spectrum.

### Cyclopeptide Scoring
To generalize the Cyclopeptide Sequencing Problem to handle noisy spectra, we need to relax the requirement that a candidate peptide’s theoretical spectrum must match the experimental spectrum exactly, and instead incorporate a scoring function that will select the peptide whose theoretical spectrum matches the given experimental spectrum the most closely. Given a cyclic peptide Peptide and a spectrum Spectrum, we define Score(Peptide, Spectrum) as the number of masses shared between Cyclospectrum(Peptide) and Spectrum. The scoring function should take into account the multiplicities of shared masses, i.e., how many times they occur in each spectrum. For example, suppose that Spectrum is the theoretical spectrum of NQEL; for this spectrum, mass 242 has multiplicity 2. If 242 has multiplicity 1 in the experimental spectrum of Peptide, then 242 contributes 1 to Score(Peptide, Spectrum). If 242 has multiplicity 2 or more in the experimental spectrum of Peptide, then 242 contributes 2 to Score(Peptide, Spectrum)
    
    Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.

    Input: An amino acid string Peptide and a collection of integers Spectrum.
    Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).

Example:

    Sample Input:
    
        NQEL
        0 99 113 114 128 227 257 299 355 356 370 371 484
    
    Sample Output:
    
        11
        
###  Leaderboard Cyclopeptide Sequencing
    Cyclopeptide Sequencing Problem (for spectra with errors): Find a cyclic peptide having maximum score against an experimental spectrum.

    Input: A collection of integers Spectrum.
    Output: A cyclic peptide Peptide maximizing Score(Peptide, Spectrum) over all peptides Peptide with mass equal to ParentMass(Spectrum).

Example:
    
    Sample Input:
    
        10
        0 71 113 129 147 200 218 260 313 331 347 389 460
    
    Sample Output:
    
        113-147-71-129

## Section 09
When we apply LeaderboardCyclopeptideSequencing for the extended alphabet to Spectrum10, one of the highest-scoring peptides is VKLFPWFNQXZ, where X has mass 98 and Z has mass 65. Apparently, non-standard amino acids successfully competed with standard amino acids for the limited number of positions on the leaderboard, resulting in VKLFPWFNQXZ winning over the correct peptide VKLFPWFNQY. Since LeaderboardCyclopeptideSequencing fails to identify the correct peptide even with only 10% false and missing masses, our stated aim from the previous section is now even more important. We must determine the amino acid composition of a peptide from its spectrum so that we may run LeaderboardCyclopeptideSequencing on this smaller alphabet of amino acids.

We define the convolution of a spectrum by taking all positive differences of masses in the spectrum.

### Spectral Convolution 
    Spectral Convolution Problem: Compute the convolution of a spectrum.

    Input: A collection of integers Spectrum.
    Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times; you may return the elements in any order.

Example:

    Sample Input:
    
        0 137 186 323
    
    Sample Output:
    
        137 137 186 186 323 49

### ConvolutionCyclopeptideSequencing
    Code Challenge: Implement ConvolutionCyclopeptideSequencing.

    Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).

Example:
    
    Sample Input:
    
        20
        60
        57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493
    
    Sample Output:
    
        99-71-137-57-72-57
        
## Section 11
We can compute an array PrefixMass storing the masses of each prefix of Peptide in increasing order, e.g., for Peptide = NQEL, PrefixMass = (0, 114, 242, 371, 484). Then, the mass of the subpeptide of Peptide beginning at position i + 1 and ending at position j can be computed as PrefixMass(j) − PrefixMass(i). For example, when Peptide = NQEL,

Mass(QE) = PrefixMass(3) − PrefixMass(1) = 371 − 114 = 257.

### Linear Spectrum
    Code Challenge: Implement LinearSpectrum.

    Input: An amino acid string Peptide.
    Output: The linear spectrum of Peptide.
    
Example:

    Sample Input:
    
        NQEL
    
    Sample Output:
    
        0 113 114 128 129 242 242 257 370 371 484
        
        
## Section 13
### Linear Scoring
    Code Challenge: Compute the score of a linear peptide with respect to a spectrum.

    Input: An amino acid string Peptide and a collection of integers Spectrum.
    Output: The linear score of Peptide with respect to Spectrum, LinearScore(Peptide, Spectrum).
    
Example:

    Sample Input:
    
        NQEL
        0 99 113 114 128 227 257 299 355 356 370 371 484
    
    Sample Output:
    
        8
        
### Trim
    Code Challenge: Implement Trim (reproduced below).

    Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
    Output: The N highest-scoring linear peptides on Leaderboard with respect to Spectrum.

Example:

    Sample Input:
    
        LAST ALST TLLT TQAS
        0 71 87 101 113 158 184 188 259 271 372
        2
        
    Sample Output:
    
        LAST ALST
        
## Section 14
### Turnpike 
If A = (a1 = 0, a2, …, an) is a set of n points on a line segment in increasing order (a1 < a2 < · · · < an), then ∆A denotes the collection of all pairwise differences between points in A. For example, if A = (0, 2, 4, 7,), then
ΔA=(−7, −5, −4, −3, −2, −2, 0, 0, 0, 0, 2, 2, 3, 4, 5, 7). The turnpike problem asks us to reconstruct A from ∆A.

    Turnpike Problem: Given all pairwise distances between points on a line segment, reconstruct the positions of those points.

    Input: A collection of integers L.
    Output: A set of integers A such that ∆A = L.

Example:

    Sample Input:
    
        -10 -8 -7 -6 -5 -4 -3 -3 -2 -2 0 0 0 0 0 2 2 3 3 4 5 6 7 8 10
    
    Sample Output:
    
        0 2 4 7 10
# CHAPTER 5: How Do We Compare Biological Sequences?
**Given two(or more) sequences, how can we compare them?**

 We now define an alignment of sequences v and w as a two-row matrix such that the first row contains the symbols of v (in order), the second row contains the symbols of w (in order), and space symbols (called gap symbols and shown as dashes below) may be interspersed throughout both strings, as long as two space symbols are not aligned against each other. Here is the alignment of ATGTTATA and ATCGTCC from the figure on the previous step.

    A T - G T T A T A
    A T C G T - C - C

An alignment presents one possible scenario by which v could have evolved into w. Columns containing the same letter in both rows are called matches and represent conserved nucleotides, whereas columns containing different letters are called mismatches and represent single-nucleotide substitutions. Columns containing a space symbol are called indels: a column containing a space symbol in the top row of the alignment is called an insertion, as it implies the insertion of a symbol when transforming v into w; a column containing a space symbol in the bottom row of the alignment is called a deletion, as it indicates the deletion of a symbol when transforming v into w. The alignment above has four matches, two mismatches, one insertion, and two deletions.
The matches in an alignment of two strings define a common subsequence of the two strings, or a sequence of symbols appearing in the same order (although not necessarily consecutively) in both strings. For example, the alignment above indicates that ATGT is a common subsequence of ATGTTATA and ATCGTCC. An alignment of two strings maximizing the number of matches therefore corresponds to a longest common subsequence (LCS) of these strings. Note that two strings may have more than one longest common subsequence.
## Section 05
## DPChange
    Change Problem: Find the minimum number of coins needed to make change.

    Input: An integer money and an array Coins of d positive integers.
    Output: The minimum number of coins with denominations Coins that changes money.

Example:

    Sample Input:
    
        40
        50,25,20,10,5,1
    
    Sample Output:
    
        2
        
## Section 06
### Find the length of a longest path in the Manhattan Tourist Problem.
    Manhattan Tourist Problem: Find a longest path in a rectangular city.

    Input: A weighted n × m rectangular grid with n + 1 rows and m + 1 columns.
    Output: A longest path from source (0,0) to sink (n, m) in the grid.
    
Example:

    Sample Input:
        
        4 4
        1 0 2 4 3
        4 6 5 2 1
        4 4 5 2 1
        5 6 8 5 3
        -
        3 2 4 0
        3 2 4 2
        0 7 3 3
        3 3 0 2
        1 3 2 2
    
    Sample Output:
    
        34
        
## Section 08
### Longest Common Subsequence Problem
    Longest Common Subsequence Problem: Find a longest common subsequence of two strings.

    Input: Two strings.
    Output: A longest common subsequence of these strings.

Example:

    Sample Input:
    
        AACCTTGG
        ACACTGTGA
    
    Sample Output:
    
        AACTGG


### Longest Path in a DAG 
    Longest Path in a Directed Graph Problem: Find a longest path between two nodes in an edge-weighted directed graph.

    Input: An edge-weighted directed graph with source and sink nodes.
    Output: A longest path from source to sink in the directed graph.
   
Example:

    Sample Input:
    
        0
        4
        0->1:7
        0->2:4
        2->3:2
        1->4:1
        3->4:3
    
    Sample Output:
    
        9
        0->2->3->4
        
## Section 10
### Global Alignment
**mach ALL v to ALL w**

The graph:

![global](http://bioinformaticsalgorithms.com/images/Alignment/colored_alignment_graph.png)


    Global Alignment Problem: Find a highest-scoring alignment of two strings as defined by a scoring matrix.

    Input: Two strings and a scoring matrix Score.
    Output: An alignment of the strings whose alignment score (as defined by Score) is maximized over all alignments of the strings.

Example:

    Sample Input:
    
        PLEASANTLY
        MEANLY
    
    Sample Output:
    
        8
        PLEASANTLY
        -MEA--N-LY
    

###  Local Alignment 
**mach SUBSET of v to SUBSET of w**
The graph:

![local](http://bioinformaticsalgorithms.com/images/Alignment/zero_weight_edges.png)


    Local Alignment Problem: Find the highest-scoring local alignment between two strings.

    Input: Strings v and w as well as a matrix score.
    Output: Substrings of v and w whose global alignment score (as defined by score) is maximized among all substrings of v and w.

Example:

    Sample Input:
    
        MEANLY
        PENALTY
    
    Sample Output:
    
        15
        EANL-Y
        ENALTY

## Section 11
### Edit Distance
The edit distance between two strings as the minimum number of edit operations needed to transform one string into another.


    Edit Distance Problem: Find the edit distance between two strings.

    Input: Two strings.
    Output: The edit distance between these strings.

Example:

    Sample Input:
    
        PLEASANTLY
        MEANLY
    
    Sample Output:
    
        5
        
### Fitting Alignment
Global alignment will not work because it tries to align all of v to all of w; local alignment will not work because it tries to align substrings of both v and w. Thus, we have a distinct alignment application called the Fitting Alignment Problem.

“Fitting” w to v requires finding a substring v′ of v that maximizes the global alignment score between v′ and w among all substrings of v.

**match SUBSET of v to ALL OF of w**

![comp_alignment](http://bioinformaticsalgorithms.com/images/Alignment/global_local_fitting.png)


    Fitting Alignment Problem: Construct a highest-scoring fitting alignment between two strings.

    Input: Strings v and w as well as a matrix Score.
    Output: A highest-scoring fitting alignment of v and w as defined by the scoring matrix Score.

Example:

    Sample Input:
    
        GTAGGCTTAAGGTTA
        TAGATA
    
    Sample Output:
    
        2
        TAGGCTTA
        TAGA--TA
        
### Overlap Alignment
An overlap alignment of strings v = v1 ... vn and w = w1 ... wm is a global alignment of a suffix of v with a prefix of w. An optimal overlap alignment of strings v and w maximizes the global alignment score between an i-suffix of v and a j-prefix of w (i.e., between vi ... vn and w1 ... wj) among all i and j.


    Overlap Alignment Problem: Construct a highest-scoring overlap alignment between two strings.

    Input: Two strings and a matrix score.
    Output: A highest-scoring overlap alignment between the two strings as defined by the scoring matrix score.

Example:

    Sample Input:
    
        PAWHEAE
        HEAGAWGHEE
    
    Sample Output:
    
        1
        HEAE
        HEAG
        
## Section 12
### Alignment with Affine Gap Penalties 
**global alignment, but favour bigger continuous gaps over a lot of mini gaps between matches**


    Alignment with Affine Gap Penalties Problem: Construct a highest-scoring global alignment between two strings (with affine gap penalties).

    Input: Two strings, a matrix score, and numbers σ and ε.
    Output: A highest scoring global alignment between these strings, as defined by the scoring matrix score and by the gap opening and extension penalties σ and ε.

Example:

    Sample Input:
    
        PRTEINS
        PRTWPSEIN
    
    Sample Output:
    
        8
        PRT---EINS
        PRTWPSEIN-
        
## Section 13
### Middle Edge in Linear Space

    Middle Edge in Linear Space Problem: Find a middle edge in the alignment graph in linear space.

    Input: Two strings and a matrix score.
    Output: A middle edge in the alignment graph of these strings (where the edge lengths are defined by score).

Example:

    Sample Input:
    
        PLEASANTLY
        MEASNLY
    
    Sample Output:
    
        (4, 3) (5, 4)

### LinearSpaceAlignment
**global alignment, but do it in linear space**

    Code Challenge: Implement LinearSpaceAlignment to solve the Global Alignment Problem for a large dataset.

    Input: Two long (10000 amino acid) protein strings written in the single-letter amino acid alphabet.
    Output: The maximum alignment score of these strings, followed by an alignment achieving this maximum score. Use the BLOSUM62 scoring matrix and indel penalty σ = 5.
    
Example:

    Sample Input:
    
        PLEASANTLY
        MEANLY
    
    Sample Output:
        
        8
        PLEASANTLY
        -MEA--N-LY    

## Section 14
### Multiple Longest Common Subsequence
**global alignment, but for three subsequences**

    Multiple Alignment Problem: Find the highest-scoring alignment between multiple strings under a given scoring matrix.

    Input: A collection of t strings and a t-dimensional matrix Score.
    Output: A multiple alignment of these strings whose score (as defined by the matrix Score) is maximized among all possible alignments of these strings.

Example:

    Sample Input:
    
        ATATCCG
        TCCGA
        ATGTACTG
    
    Sample Output:
    
        3
        ATATCC-G-
        ---TCC-GA
        ATGTACTG-

## Section 17
### TopologicalOrdering

     Code Challenge: Implement TopologicalOrdering.
     
     Input: The adjacency list of a graph (with nodes represented by integers).
     Output: A topological ordering of this graph.
Example:

    Sample Input:
    
        0 -> 1
        1 -> 2
        3 -> 1
        4 -> 2
    
    Sample Output:
    
        0, 3, 4, 1, 2
