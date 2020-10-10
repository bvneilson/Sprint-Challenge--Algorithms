#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) I believe this snippet runs at quadratic time (O(n^2)) because the time to run this program increases exponentially as the input increases. i.e. an input size of 4 may seem fairly harmless, but if we increase input to any sort of large number in the 100s or 1,000s even, we would see this program run for much, much more time.

b) I believe this snippet runs at linear time (O(n)) because the time to run this program would increase steadily as input size grows. i.e. the inside while loop runs more times the larger the input.

c) I believe this snippet runs at linear time (O(n)) because the time to run this program would increase steadily as input size grows. i.e. the greater the number of 'bunnies', the greater the amount of times bunnyEars() is recursively called.

## Exercise II

1. Drop egg off top floor

If egg breaks:
2a. Make note of this tested floor, then divide number of floors by half and drop next egg from there (rounding to nearest floor when necessary)

    If egg breaks:
    3a. Repeat step 2a

    Else if: cur_floor == last_floor - 1, you have found floor f

    Else:
    3b. Repeat step 2a but with the floors above current floor (cur_floor through last_floor - 1)

      If egg breaks:
      4a. Repeat step 2a

      Else:
      4b. Repeat step 3b

Else:
2b. If egg does not break, you have found floor f

Analysis: b) I believe this algorithm would run at linear time (O(n)) because the time to run this program would increase steadily as input size grows. i.e. the potential (worst case) number of iterations would depend on how large the input is.
