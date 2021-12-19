----------------------------------------------------------------------
Sun Dec 19, works for test.data, using two dictionary logic 

day_14>python  b.py  | grep diff
              1749 - 161 = diff: 1588
                           diff: 1588 <-- the correct number
              2192039569602 - 3849876073 = diff: 2188189693529
                                           diff: 2188189693529  <-- correct for test.data

however, when I use the full input data, I get the wrong answers !!!

day_14>python  b.py  | grep diff
              3166 - 635 = diff: 2531
                           diff: 2712  <-- the correct number
              7508787104320 - 352917345929 = diff: 7155869758391
   big=8768088887348   small=431465827781    diff: 8336623059567  <-- correct for input.data


----------------------------------------------------------------------

 I was reading through,  what this person had done, was create a python dictionary of pairs with the count of that pair 
  my_dict = {  "CH":5 ,  "CN":5,  "CB":5 .... }

       and the light bulb went off !!!    

I am still not sure quite how this will work ... 
because you have that third char hanging out there (possibly a non-issue)

but I could see that if you polymerized all the  "CH"  strings (lets say they are 5 in number)
connect them to "CB"    and "BH" 

so in your new  dictionary          CH: 0      CB: 5    BH:5 
  
so the total count effectively doubles (which is the progression I was seeing  n*(n-1) 

so I stopped going through the other code, and with this insight,  try to code it on my own 
---------------------------------------------------------------------------------------------
thinking about the problem this way,  you have a small set of letter combinations in the polymer

   in part A it was only NBC 
   in part B you have ten letters,  B, C, F, H, K, N, O, P, S, V
   then you have all two letter permutations:   BC CB  BF FB BH HB .... and so on  
   as I m sure u know,  this would be  worst case:  10! / 2!  or  1,814,400     lets say 2 million,
   which is a very manageable number, it turns out the number of permutations is way less than 2 million

you  just have to keep track of  "how many" of each two-letter permutations you have ... 
AND you have to keep track of how many letters you have in your original template 
adding in every time you add one more letter

when you polymerize ... you  change  BC->S    
   (you have to bump the S count by the number of BC pairs you have, call that mm)

you create two new  pairs ( or add to an already existing pair)    BS  +mm     CS +mm

I polymerize template_A  dictionary into template_B  dictionary, then over-wrote  A with B 

The easiest way to see that your results are correct, 
is that the total number of polymer instances should multiply by a factor of 2 every day
originally 3, 6 the next day, 12 on the second  and 24 on the third day
---------------------------------------------------------------------------------------------


--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine.
The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine,
and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula;
specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input).
You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. 
A rule like AB -> C means that when elements A and B are immediately adjacent, 
element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first  pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third  pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.

Note that these pairs overlap: the second element of one pair is the first element of the next pair. 
Also, because all pairs are considered simultaneously, 
inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. 
After step 5, it has length 97; 
After step 10, it has length 3073. 
After step 10, B occurs 1749 times, 
C occurs 298 times, 
H occurs 161 times, and N occurs 865 times; 
taking the quantity of the most common element (B, 1749) 
and subtracting the quantity of the least common element (H, 161) 
produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find 
the most and least common elements in the result. 
What do you get if you take the quantity of the most common element
and subtract the quantity of the least common element?

    Your puzzle answer was 2712.

A day_14>python  zatoichi49.py  test.data
1588
2188189693529

A day_14>time  python  zatoichi49.py    input.data
2712
8336623059567
     real    0m0.172s
