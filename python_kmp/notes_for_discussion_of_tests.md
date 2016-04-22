 1. Use of random strings

        import random
        import string
        import re                                                                       
        
        def random_string(length=100, chars=4):
            inventory = random.sample(string.ascii_letters, chars)
            return ''.join(random.choice(inventory) for _ in range(length))

 2. Use of Keith Schwarz's different implementation of COMPUTE-PREFIX-FUNCTION to test `fill_skip_ahead_array`.

 3. Problem testing for all matches, because `re.finditer` ignores overlapping matches. Example:

        In [1]: seq = '1010101010101010101010101010101010'
        
        In [2]: subseq = '0101010'
        
        In [3]: list(KMP.match(seq, subseq))
        Out[3]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
        
        In [4]: [i.start() for i in re.finditer(subseq, seq)]
        Out[4]: [1, 9, 17, 25]

   Solution: Use look-ahead to force return of even overlapping matches:

        In [5]: [i.start() for i in re.finditer('(?='+subseq+')', seq)]
        Out[5]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]

[end]