I really liked this problem because I felt like I was able to progress in making my code more efficient.

First we note that for a given x, if the set {x,2x,3x,4x,5x,6x} are all to have the same digits, then we must realize that
multiplying by 6 creates an upper bound that cannot go into the next order of magnitude.

For instance:  if we are testing numbers in the range of 100 to 999, then we really only need test the numbers 100 to 166. 
This is because 6*167 > 1000 and so it cannot be that all the numbers in the set have the same digits. This is reflected in 
the second FOR loop for the code.

Secondly, because we have the value 5x, we know that the number must contain the digit 5 somewhere. If it doesn't, we can
ignore it.

Finally, all the digits in the number cannot be odd due to the fact we have the value 2x. I am not sure yet how to properly 
implement this into the code, so for now it is left out. But it would make the code more efficient if we could skip those 
numbers too.
