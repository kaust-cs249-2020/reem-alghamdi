# CHAPTER 1: Where in the Genome Does Replication Begin?
## Section 02
### PatternCount
    Code Challenge: Implement PatternCount (reproduced below).
    Input: Strings Text and Pattern.
    Output: Count(Text, Pattern).


### Frequent Words 
    Frequent Words Problem: Find the most frequent k-mers in a string.

    Input: A string Text and an integer k.
    Output: All most frequent k-mers in Text.


## Section 03
###  Reverse Complement
    Reverse Complement Problem: Find the reverse complement of a DNA string.

    Input: A DNA string Pattern.
    Output: Patternrc , the reverse complement of Pattern.

### Pattern Matching
    Pattern Matching Problem: Find all occurrences of a pattern in a string.

    Input: Strings Pattern and Genome.
    Output: All starting positions in Genome where Pattern appears as a substring.

## Section 04
### Clump Finding
    Clump Finding Problem: Find patterns forming clumps in a string.

    Input: A string Genome, and integers k, L, and t.
    Output: All distinct k-mers forming (L, t)-clumps in Genome.

## Section 07
### Minimum Skew
    Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

    Input: A DNA string Genome.
    Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

## Section 08
### Hamming Distance
    Hamming Distance Problem: Compute the Hamming distance between two strings.

    Input: Two strings of equal length.
    Output: The Hamming distance between these strings.

### Approximate Pattern Matching
    Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

    Input: Strings Pattern and Text along with an integer d.
    Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

### ApproximatePatternCount
    Code Challenge: Implement ApproximatePatternCount.

    Input: Strings Pattern and Text as well as an integer d.
    Output: Countd(Text, Pattern).

### Frequent Words with Mismatches
    Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.

    Input: A string Text as well as integers k and d.
    Output: All most frequent k-mers with up to d mismatches in Text.

### Frequent Words with Mismatches and Reverse Complements
    Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a string.

    Input: A DNA string Text as well as integers k and d.
    Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Patternrc) over all possible k-mers.


## Section 11
### Neighbors
    Code Challenge: Implement Neighbors to find the d-neighborhood of a string.

    Input: A string Pattern and an integer d.
    Output: The collection of strings Neighbors(Pattern, d).

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

