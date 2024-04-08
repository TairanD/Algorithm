# Bitwise Operations

## 1 - Definition
In computers, all calculations are conducted in binary representation (a.k.a. 0s and 1s), bitwise operations involve 
manipulating individual bits (each bit has single binary value of 0 or 1) of binary representations of numbers to perform operations efficiently. 

## 2 - Faster
Bitwise operations are often faster than arithmetic operations (+, -, *, /) due to several key reasons:
1. Hardware Support: Many CPUs have specialized hardware circuits called Arithmetic Logic Units (ALUs) designed to 
perform bitwise operations directly on binary numbers. These circuits can execute bitwise operations with fewer clock 
cycles compared to arithmetic operations, which often require more complex sequences of micro-operations.
2. Simplicity of Operations: Bitwise operations involve simpler and more straightforward operations at the binary level, 
such as AND, OR, XOR, and shifting. These operations can be implemented more efficiently in hardware and executed with 
fewer clock cycles compared to arithmetic operations like addition, subtraction, multiplication, and division, which involve more complex algorithms.
3. Efficient Memory Usage: Bitwise operations often work with smaller units of data, manipulating individual bits rather
than entire numbers. This can lead to more efficient use of memory and cache, reducing the time spent on memory accesses
and improving overall performance, especially in situations where memory bandwidth is a bottleneck.

Therefore, using bitwise operations properly can increase the efficiency.