# Java: Pass-By-Value? Pass-By-Reference
*Reference this [article](https://www.javadude.com/articles/passbyvalue.htm).

## 1 - Definition
Both two terms describe _variables_.
### Pass-By-Value
Def v1: 
The actual parameter (or argument expression) is fully evaluated and the resulting value is **copied** into a location being
used to hold the formal parameter’s value during method/function execution. That location is typically a chunk of memory 
on the runtime stack for the application (which is how Java handles it), but other languages could choose parameter storage differently.

[Def v2](https://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value/430958#430958): 
When a parameter is passed by value, the caller and callee have two independent variables with the same value. If the callee 
modifies the parameter variable, the effect is not visible to the caller.

### Pass-By-Reference
Def v1: The formal parameter merely acts as an **alias** for the actual parameter. Anytime the method/function uses the formal 
parameter (for reading or writing), it is actually using the actual parameter.

Def v2: When a parameter is passed by reference, the caller and the callee use the same variable for the parameter. If the callee
modifies the parameter variable, the effect is visible to the caller's variable.

## 2 - Java: Always Pass-By-Value
Java is strictly pass-by-value, exactly as in C. Read the [Java Language Specification (JLS)](https://docs.oracle.com/javase/specs/jls/se11/html/jls-8.html#jls-8.4.1):

    When the method or constructor is invoked (§15.12), the **values** of the actual argument expressions initialize newly created 
    parameter variables, each of the declared type, before execution of the body of the method or constructor. The Identifier 
    that appears in the FormalParameter may be used as a simple name in the body of the method or constructor to refer to the formal parameter.

## 2* - C: Always Pass-By-Value


## 3 - The Litmus Test

There’s a simple “litmus test” for whether a language supports pass-by-reference semantics:
- Can you write a traditional swap(a,b) method/function in the language?
  A traditional swap method or function takes two arguments and swaps them such that variables passed into the function 
are changed outside the function. Its basic structure looks like:
    ```
    void swap(Type arg1, Type arg2) {
        Type temp = arg1;
        arg1 = arg2;
        arg2 = temp;
    }
    ```
    If we can actually swap the values of `var1` & `var2`, the language supports pass-by-reference semantics.
- But you CANNOT do this in Java!
- In java, swap method should be:
    ```
    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    ```
