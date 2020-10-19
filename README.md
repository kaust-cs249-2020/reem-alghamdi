# CHAPTER 1: Where in the Genome Does Replication Begin?
Genome replication is one of the most important tasks carried out in the cell. Before a cell can divide, it must first replicate its genome so that each of the two daughter cells inherits its own copy. 
![replication](https://static.wixstatic.com/media/988d7f_7ef43621eed44d0abf39a39c8287d322~mv2.png)

Replication begins in a genomic region called the replication origin (denoted ori) and is carried out by molecular copy machines called DNA polymerases.

**GOAL**: how to find ori?

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

Since we don't know the location of ori in a circular genome, let's linearize it (i.e., select an arbitrary position and pretend that the genome begins here), resulting in a linear string Genome. We define Skewi(Genome) as the difference between the total number of occurrences of G and the total number of occurrences of C in the first i nucleotides of Genome. The skew diagram is defined by plotting Skewi (Genome) (as i ranges from 0 to |Genome|), where Skew0 (Genome) is set equal to zero. The figure below shows a skew diagram for the DNA string CATGGGCATCGGCCATACGCC.
Note that we can compute Skewi+1(Genome) from Skewi(Genome) according to the nucleotide in position i of Genome. If this nucleotide is G, then Skewi+1(Genome) = Skewi(Genome) + 1; if this nucleotide is C, then Skewi+1(Genome)= Skewi(Genome) – 1; otherwise, Skewi+1(Genome) = Skewi(Genome).


**Exercise Break**: Give all values of Skewi (GAGCCACCGCGATA) for i ranging from 0 to 14.
![skew](http://bioinformaticsalgorithms.com/images/Replication/skew_diagram_basic.png)

**Sample Input:**

     CATGGGCATCGGCCATACGCC

**Sample Output:**

     0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2



### Minimum Skew
Let's follow the 5' → 3' direction of DNA and walk along the chromosome from ter to ori (along a reverse half-strand), then continue on from ori to ter (along a forward half-strand). In our previous discussion, we saw that the skew is decreasing along the reverse half-strand and increasing along the forward half-strand. Thus, the skew should achieve a minimum at the position where the reverse half-strand ends and the forward half-strand begins, which is exactly the location of ori!

    Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

    Input: A DNA string Genome.
    Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

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
## Section 02
### MotifEnumeration
    Implanted Motif Problem: Find all (k, d)-motifs in a collection of strings.

    Input: A collection of strings Dna, and integers k and d.
    Output: All (k, d)-motifs in Dna.

## Section 03
### Motif 
    This function takes a matrix of motifs, and compute information
    Input: A collection of strings Dna
    Output: consensus, score, count, profile, entropy, entropies 
 
## Section 04
### Median String
    Median String Problem: Find a median string.

    Input: A collection of strings Dna and an integer k.
    Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers.

## Section 05
### Profile-most Probable k-mer
    Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.

    Input: A string Text, an integer k, and a 4 × k matrix Profile.
    Output: A Profile-most probable k-mer in Text.

### GreedyMotifSearch
    Code Challenge: Implement GreedyMotifSearch.

    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.

## Section 06

### Greedy Motif Search with pseudocounts
    Code Challenge: Implement GreedyMotifSearch with pseudocounts.

    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna, k, t) with pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.


## Section 07
### RandomizedMotifSearch
    Code Challenge: Implement RandomizedMotifSearch.

    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times. Remember to use pseudocounts!


## Section 09
### GibbsSampler
    Code Challenge: Implement GibbsSampler.

    Input: Integers k, t, and N, followed by a collection of strings Dna.
    Output: The strings BestMotifs resulting from running GibbsSampler(Dna, k, t, N) with 20 random starts. Remember to use pseudocounts!

## Section 12
### DistanceBetweenPatternAndStrings
    Code Challenge: Implement DistanceBetweenPatternAndStrings.

    Input: A string Pattern followed by a collection of strings Dna.
    Output: d(Pattern, Dna).

# CHAPTER 3: How Do We Assemble Genomes?
## Section 02: 
### String Composition 
    String Composition Problem: Generate the k-mer composition of a string.

    Input: An integer k and a string Text.
    Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.

## Section 03
### String Spelled by a Genome Path
    String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.

    Input: A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
    Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).

###  Overlap Graph
    Overlap Graph Problem: Construct the overlap graph of a collection of k-mers.

    Input: A collection Patterns of k-mers.
    Output: The overlap graph Overlap(Patterns).

## Section 04
### De Bruijn Graph from a String
    De Bruijn Graph from a String Problem: Construct the de Bruijn graph of a string.

    Input: An integer k and a string Text.
    Output: DeBruijnk(Text).

## Section 05
### Eulerian Path
    Eulerian Path Problem: Construct an Eulerian path in a graph.

    Input: A directed graph.
    Output: A path visiting every edge in the graph exactly once (if it exists).

## Section 08
### Eulerian Cycle Problem
    Eulerian Cycle Problem: Find an Eulerian cycle in a graph.

    Input: A graph.
    Output: An Eulerian cycle in this graph, if one exists.
### Eulerian Path Problem
    Code Challenge: Solve the Eulerian Path Problem.

    Input: The adjacency list of a directed graph that has an Eulerian path.
    Output: An Eulerian path in this graph.
### StringReconstruction
    Code Challenge: Solve the String Reconstruction Problem.

    Input: An integer k followed by a list of k-mers Patterns.
    Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)
### k-Universal Circular String 
    Code Challenge: Solve the k-Universal Circular String Problem.

    Input: An integer k.
    Output: A k-universal circular string.

## Section 09
### String Reconstruction from Read-Pairs
    String Reconstruction from Read-Pairs Problem: Reconstruct a string from its paired composition.

    Input: A collection of paired k-mers PairedReads and an integer d.
    Output: A string Text with (k,d)-mer composition equal to PairedReads (if such a string exists).

## Section 10
### Contig Generation 
    Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).

    Input: A collection of k-mers Patterns.
    Output: All contigs in DeBruijn(Patterns).


## Section 13
### String Spelled by a Gapped Genome Path 
    String Spelled by a Gapped Genome Path Problem: Reconstruct a sequence of (k, d)-mers corresponding to a path in a paired de Bruijn graph.

    Input: A sequence of (k, d)-mers (a1|b1), ..., (an|bn) such that Suffix((ai|bi)) = Prefix((ai+1|bi+1)) for 1 ≤ i ≤ n - 1.
    Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer of Text is equal to (ai|bi) for 1 ≤ i ≤ n (if such a string exists).

## Section 14
### MaximalNonBranchingPaths
    Code Challenge: Implement MaximalNonBranchingPaths.

    Input: The adjacency list of a graph whose nodes are integers.
    Output: The collection of all maximal nonbranching paths in this graph.

# CHAPTER 4: How Do We Sequence Antibiotics?
## Section 02
### Protein Translation
    Protein Translation Problem: Translate an RNA string into an amino acid string.

    Input: An RNA string Pattern and the array GeneticCode.
    Output: The translation of Pattern into an amino acid string Peptide.

### Peptide Encoding 
    Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.

    Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    Output: All substrings of Text encoding Peptide (if any such substrings exist).
    
## Section 04
### Count Cyclic Peptides
    Exercise Break: How many subpeptides does a cyclic peptide of length n have?
### Theoretical Spectrum
    Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.

    Input: An amino acid string Peptide.
    Output: Cyclospectrum(Peptide).

## Section 05
### Counting Peptides with Given Mass
    Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass.

    Input: An integer m.
    Output: The number of linear peptides having integer mass m.

## Section 06
### Count Linear Peptides
    Exercise Break: How many subpeptides does a linear peptide of given length n have? (Include the empty peptide and the entire peptide.)
### Cyclopeptide Sequencing
    Cyclopeptide Sequencing Problem: Given an ideal spectrum, find a cyclic peptide whose theoretical spectrum matches the experimental spectrum.

    Input: A collection of (possibly repeated) integers Spectrum corresponding to an ideal spectrum.
    Output: An amino acid string Peptide such that Cyclospectrum(Peptide) = Spectrum (if such a string exists).


## Section 07
### Cyclopeptide Scoring
    Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.

    Input: An amino acid string Peptide and a collection of integers Spectrum.
    Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).

###  Leaderboard Cyclopeptide Sequencing
    Cyclopeptide Sequencing Problem (for spectra with errors): Find a cyclic peptide having maximum score against an experimental spectrum.

    Input: A collection of integers Spectrum.
    Output: A cyclic peptide Peptide maximizing Score(Peptide, Spectrum) over all peptides Peptide with mass equal to ParentMass(Spectrum).


## Section 09
### Spectral Convolution 
    Spectral Convolution Problem: Compute the convolution of a spectrum.

    Input: A collection of integers Spectrum.
    Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times; you may return the elements in any order.
### ConvolutionCyclopeptideSequencing
    Code Challenge: Implement ConvolutionCyclopeptideSequencing.

    Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).

## Section 11
### Linear Spectrum
    Code Challenge: Implement LinearSpectrum.

    Input: An amino acid string Peptide.
    Output: The linear spectrum of Peptide.
    
## Section 13
### Linear Scoring
    Code Challenge: Compute the score of a linear peptide with respect to a spectrum.

    Input: An amino acid string Peptide and a collection of integers Spectrum.
    Output: The linear score of Peptide with respect to Spectrum, LinearScore(Peptide, Spectrum).
### Trim
    Code Challenge: Implement Trim (reproduced below).

    Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
    Output: The N highest-scoring linear peptides on Leaderboard with respect to Spectrum.

## Section 14
### Turnpike 

    Turnpike Problem: Given all pairwise distances between points on a line segment, reconstruct the positions of those points.

    Input: A collection of integers L.
    Output: A set of integers A such that ∆A = L.
    
# CHAPTER 5: How Do We Compare Biological Sequences?

 
## Section 05
## DPChange
    Change Problem: Find the minimum number of coins needed to make change.

    Input: An integer money and an array Coins of d positive integers.
    Output: The minimum number of coins with denominations Coins that changes money.

passed all tests
## Section 06
### Find the length of a longest path in the Manhattan Tourist Problem.
    Manhattan Tourist Problem: Find a longest path in a rectangular city.

    Input: A weighted n × m rectangular grid with n + 1 rows and m + 1 columns.
    Output: A longest path from source (0,0) to sink (n, m) in the grid.
    
passed all tests

## Section 08
### Longest Common Subsequence Problem
    Longest Common Subsequence Problem: Find a longest common subsequence of two strings.

    Input: Two strings.
    Output: A longest common subsequence of these strings.
passed all tests

### Longest Path in a DAG 
    Longest Path in a Directed Graph Problem: Find a longest path between two nodes in an edge-weighted directed graph.

    Input: An edge-weighted directed graph with source and sink nodes.
    Output: A longest path from source to sink in the directed graph.
   
passed all tests 

## Section 10
### Global Alignment
    Global Alignment Problem: Find a highest-scoring alignment of two strings as defined by a scoring matrix.

    Input: Two strings and a scoring matrix Score.
    Output: An alignment of the strings whose alignment score (as defined by Score) is maximized over all alignments of the strings.
passed all tests  

###  Local Alignment 
    Local Alignment Problem: Find the highest-scoring local alignment between two strings.

    Input: Strings v and w as well as a matrix score.
    Output: Substrings of v and w whose global alignment score (as defined by score) is maximized among all substrings of v and w.
passed all tests  

## Section 11
### Edit Distance
    Edit Distance Problem: Find the edit distance between two strings.

    Input: Two strings.
    Output: The edit distance between these strings.
passed all tests  

### Fitting Alignment
    Fitting Alignment Problem: Construct a highest-scoring fitting alignment between two strings.

    Input: Strings v and w as well as a matrix Score.
    Output: A highest-scoring fitting alignment of v and w as defined by the scoring matrix Score.
passed all tests  

### Overlap Alignment
    Overlap Alignment Problem: Construct a highest-scoring overlap alignment between two strings.

    Input: Two strings and a matrix score.
    Output: A highest-scoring overlap alignment between the two strings as defined by the scoring matrix score.
passed all tests  

## Section 12
### Alignment with Affine Gap Penalties 
    Alignment with Affine Gap Penalties Problem: Construct a highest-scoring global alignment between two strings (with affine gap penalties).

    Input: Two strings, a matrix score, and numbers σ and ε.
    Output: A highest scoring global alignment between these strings, as defined by the scoring matrix score and by the gap opening and extension penalties σ and ε.
passed all tests

## Section 13
### Middle Edge in Linear Space

    Middle Edge in Linear Space Problem: Find a middle edge in the alignment graph in linear space.

    Input: Two strings and a matrix score.
    Output: A middle edge in the alignment graph of these strings (where the edge lengths are defined by score).
needs more work
## Section 14
### Multiple Longest Common Subsequence
    Multiple Alignment Problem: Find the highest-scoring alignment between multiple strings under a given scoring matrix.

    Input: A collection of t strings and a t-dimensional matrix Score.
    Output: A multiple alignment of these strings whose score (as defined by the matrix Score) is maximized among all possible alignments of these strings.
passed all tests

