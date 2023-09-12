'''
Divide & conquer
    Merge sort [ T(n) is n * log_2(n) ]
    log_2(n) -> that's how many time you can divide the array into halves
           n -> all merges must traverse the array

        divide  -> divide the array into halves
        conquer -> sort the halves (we'll use merge sort)
                   - returns a bunch of len-1 arrays?
        combine -> merge the halves
    (good idea to know one 'good' sorting algorithm)

    Quick Sort [AC:  T(n) is n * log_2(n), WC:  T(n) is n^2 ]
    log_2(n) -> that's how many time you can divide the array into halves
           n -> finding the pivot(s)

        divide -> select a pivot (!?)
                  pivot => an element of the array
                        => we place it so that elements to its left are smaller,
                                               elements to its right are larger,
                        => pivot is in the correct place

        conquer -> sort the two parts of the array (left of pivot, right of pivot)
        combine -> not a lot to do here ?

find_max (divide into halves)
extra-space complexity:

T(1) = 1
T(n) = 2*T(n/2) + n = 2 * [ 2*T(n/4) + n/2] + n = 4*T(n/4) + n + n
2^k = n  ( <=> k = log_2(n) ) => 2^k*T(1) + kn = n + n * log_2(n)


binary search
T(1) = 1
T(n) = T(n/2) + 1 ( => log_2(n) )

(x ** k//2) * (x ** k//2)
return aux ** 2

Backtracking
0 1 2


8-queen problem
data representation
    ->

-----






'''