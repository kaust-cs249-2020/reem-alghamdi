"""
@BY: Reem Alghamdi
@DATE: 06-12-2020
"""
from ch9.code.ch9_05 import longest_shared_substring


"""
3. Give an example of a string P = P 1 ...P n over alphabet Σ = {A, B} whose
uncompressed suffix tree has size Θ(n^2 ).


suffix tree guarantee O(|text|) space complexity. so only strings with length = 1 will have size O(n^2).
So either "A" or "B"
"""

"""
4. A palindrome is a string that is identical when reversed. Given a string
S, design an algorithm that can find the longest palindromic substring of
S.

I would use the same approach as longest shared substring, I would use text1 = string and text2 = inverse of string
"""


def longest_palindromic_substring(text):
    return longest_shared_substring(text, text[::-1])

"""
5. There is a casino that sometimes uses a fair die and sometimes uses a
loaded die. You get to see the outcomes of the rolls, but not which die is
used. For each die, you are given the probability of the faces, which are
numbered 1 to 6. You are also given the probabilities of switching dice
and the probability of starting with each die type – in short, an HMM.
Suppose you know that an Occasionally Dishonest Casino never uses the
loaded die more than 2 times in a row. If you do nothing about this, the
state sequence returned by the Viterbi algorithm may be an impossible
one with 3 or more consecutive uses of the loaded die. This may happen
if, by chance, some fair rolls that look more likely under the loaded model
are adjacent to loaded rolls that also look more likely under the loaded
model.
(a) Can you use the Verterbi algorithm to obtain the most likely state
sequence given an observation? If so, how?
(b) What is the structure of the correct HMM for this casino, in terms of
the number of states, their interpretations, and the allowable transitions
among them?

b)
first, let's look at the simple example: 
the sates are two: {fair, loaded} dies
the emission and transmission are given by their probabilities
the alphabet is the numbers 1 to 6

now, we have more constraints.. we can not use loaded more than two times in a row. 
Since HMM are basically finite state machines, here is the diagram + description:
STATES: {Fair, Loaded1, Loaded2}
alphabet: {1, 2, 3, 4, 5, 6}
emission: as given
transmission: a function of states x states, p is possible with probability as given and 0 is not possible:

    F   L1  L2
F   p   p   0
L1  p   0   p
L2  p   0   0

simply put, the dealer can use fair dice as many times as he wants. Once he uses a loaded dice,however, he have two choices: 
1. use a fair dice
2. use a loaded dice again

once he uses the loaded dice again, he has only ONE option: go back to using fair dice

the diagram is in this same folder: graphviz.svg

a) since we were able to define HMM properly, we can use the Verterbi algorithm
"""


if __name__ == "__main__":
    print(longest_palindromic_substring("reem"))  # should be ee
    print(longest_palindromic_substring("sjdfhfaeaefeaeaoiuijl"))  # should be aeaefeaea
    print(longest_palindromic_substring("ABACCDDDCC"))  # should be CCDDDCC
