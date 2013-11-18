## Gayle Laakmann, _Cracking the Coding Interview_, Ideas, Chapter 01

  * 1.1: Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?

    1. Easy solution is quadratic: traverse list once; for each traversal, traverse the remainder and look for a duplicate.
    2. Sort copy of list; traverse, comparing adjacent items for duplication. `O(n log n)`, requires additional space.
    3. To avoid using additional space in above, can sort in place. However, that destroys original list.

  * 1.2: Write code to reverse a C-Style String (C-String means that “abcd” is represented as five characters, including the null character.)

    1. Traverse list, doing the following steps: hold address of `next_node`; change `next_node` attribute to the previous nodes's `next_node`, which you have been holding; insert `null` at root and delete from tail; set rootpointer to address of former last node.
    1. Use XOR doubly linked list?

  * 1.3: Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer NOTE: One or two additional variables are fine An extra copy of the array is not.

  FOLLOW UP: Write the test cases for this method.

    1. Use the quadratic solution to 1.1, above. Remove each duplicate as found.

  * 1.4: Write a method to decide if two strings are anagrams or not.

    1. In Python, sort each string and assert that they are equal.

  * 1.5: Write a method to replace all spaces in a string with ‘%20’. O(n log n)`.

  * 1.6: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees Can you do this in place?

    1. The key to in-place solution is how the array is read as a matrix. Given


            matrix        array
            ------        -----
            20 21 22
            10 11 12  =>  00 01 02 10 11 12 20 21 22
            00 01 02      

    Row `r` of matrix is N indices of the array, beginning at index rN.

    Now we want to convert the array into a _rotated_ matrix. We will rotate 90° counterclockwise.

            array                           matrix
            -----                           ------
                                            
            00 01 02 10 11 12 20 21 22  => 

    Now we 

                          12 02
            10 11 12  =>  11 01
            00 01 02      10 00

    Row 0 of rotated mat

  * 1.7: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

  * 1.8: Assume you have a method isSubstring which checks if one word is a substring of another Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i e , “waterbottle” is a rotation of “erbottlewat”).

[end]