# Bioinformatics: subsequences
Finding occurrences of a pattern **P** in a target string **D** using Dynamic Programming

Given a query string **P** and a target string **D**, the goal is find how many times **P** appears as a sub-sequence of **D**. Note that the term sub-sequence is not the same as the term sub-string and a sub-sequence may have other characters of **D** occuring in between the characters of **P**. For example, **AT** is a sub-sequence of **ACGT**. **CT** is also a sub-sequence of **ACGT**. However, **TA** is not a subsequence of **ACGT**. 

Formally, the problem can be stated as follows:

Given two strings **P** and **D**, how many different sequences of increasing indices, *ind*, you can find, so that **D**[*ind1*] + **D**[*ind2*] + **D**[*ind3*] +….+ **D**[*ind|P|*] = **P**. Here, *ind* is an array of increasing integers, + is the character concatenation operation, **D**[*i*] is the *ith* character of string **D**, and |**P**| is the length of the string **P**.

For example, if **P** is **AT** and **D** is **AGTATCCTGTA**, **P** occurs as a subsequence of **D** seven times, where the indices are [1,3], [1,5], [1,8], [1,10], [4,5], [4,8], and [4,10].

A dynamic programming solution for this problem has the following reccurrence equation, where F(*i,j*) shows the number of occurrences of the first *i* characters of **P** as a sub-sequence of the first *j* characters of **D**:

F(i,0) = 0 0 ≤ *i* ≤ |**P**|
F(0,j) = 1 0 ≤ *j* ≤ |**D**|

F(i,j-1) + F(i-1,j-1) if D[j] is equal to P[i]

F(i,j) = F(i,j-1) if D[j] is not equal to P[i]

Since F can grow very quickly to very large numbers for certain **P** and **D**, only 5 digits of the computed are used. In other words, we are only be interested in F(|**P**|,|**D**|) % 100000.
