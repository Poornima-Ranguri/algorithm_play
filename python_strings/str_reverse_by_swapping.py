 def swap(s):  
    """Reverse string s by swapping elements from both ends."""
     a = list(s)
     for i in range(len(s)):
         print(i, -1-i, a[i], a[-1-i])
         if i + 1 > len(s) // 2:
             break
         a[i], a[-1-i] = a[-1-i], a[i]
     return ''.join(a)

