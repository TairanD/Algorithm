# Radix Sort

#### Introduction

All algorithms introduced before are based on the comparison operation. Yet, not bucket sort, which is based on radix.
Based on the radix of the target set of data (let's take decimal numbers stored in an array as the example), the
algorithm requires 10
container (a.k.a. bucket) storing data. By putting elements in and out buckets (when out, elements in the lower bucket
out firstly) from the lowest digit to the highest digit from the beginning
of the array, we can sort them in order.

#### How does this work?

1. Starting from the lowest digit to the highest digit
    - Guaranteeing the priorities of following sort operations against earlier sort.
2. Arranging elements from the beginning of the array (**from left to right**) combined with **FIFO principle** of each
   bucket
    - Ensuring the order sorted from previous procedures (like units' digit & tens digit compared to hundreds digit)
      will be preserved



