"""
Assignment 1

Question: Consider the number 5757. How many characters do you need to represent it in a unary numeral
system, such as the Roman numerals, and in a positional numeral system, such as the binary
numeral system? If n is the number of digits in a given number, sketch roughly what is the
character (or space) requirement to represent this number in a unary numeral system and in a
positional system.

Answer: 
Unary system
In a unary numeral system, the number is represented by repeating a single symbol the number of times equal to the number itself.

For example, the number 3 would be represented as "111" in unary. Therefore, the number of characters needed to represent the number in unary is exactly the number itself.

For 5757 in unary, you would need 5757 repetitions of the unary symbol 1. space required 5757

Binary system:

"""
def decimal_to_binary(num):
    binary_string = ""  # Step 1: Initialize an empty string to store the binary representation.

    while num > 0:  # Continue the process as long as the number is greater than 0.
        remainder = num % 2  # Step 2: Find the remainder when the number is divided by 2. This will be either 0 or 1.
        binary_string += str(remainder)  # Add the remainder to our string.

        num //= 2  # Step 3: Update the number by setting it to its quotient when divided by 2.

    return binary_string[::-1]  # Step 5: Reverse the string of remainders to get the final binary representation.

# Testing the function
numbers = [5757, 3, 19, 57]
for num in numbers:
    print(f"{num} in Binary is: {decimal_to_binary(num)}")


def decimal_to_hexadecimal(num):
    # A list to map the remainders to their respective hexadecimal character
    hex_map = "0123456789ABCDEF"
    
    hex_string = ""  # Step 1: Initialize an empty string to store the hexadecimal representation.

    while num > 0:  # Continue the process as long as the number is greater than 0.
        remainder = num % 16  # Step 2: Find the remainder when the number is divided by 16.
        hex_char = hex_map[remainder]  # Step 3: Convert the remainder to its hexadecimal character.
        hex_string += hex_char  # Add the hex character to our string.

        num //= 16  # Step 4: Update the number by setting it to its quotient when divided by 16.

    return hex_string[::-1]  # Step 6: Reverse the string of characters to get the final hexadecimal representation.

# Testing the function
numbers = [5757, 3, 19, 57]
for num in numbers:
    print(f"{num} in hexadecimal is: {decimal_to_hexadecimal(num)}")


"""
Assignment 2:
To shift all 1s on its tape one cell to the right, a Turing machine will need to recognize the position of each 1, make space by moving everything to the right of the 1 one position further, and then place the 1 in the newly created empty space.

Here's a high-level breakdown of the Turing machine's operation:

Start in the initial state. Search for the first 1.
When a 1 is found, change it to a blank (or some other character, say X, denoting that this position has been processed) and move right until you find a blank.
When you find a blank, replace it with 1 and move left.
Keep moving left until you find X, then change it to blank and move right to search for the next 1.
Now, let's specify the transitions for this Turing machine:

Answer
Here's a high-level breakdown of the Turing machine's operation:

Start in the initial state. Search for the first 1.
When a 1 is found, change it to a blank (or some other character, say X, denoting that this position has been processed) and move right until you find a blank.
When you find a blank, replace it with 1 and move left.
Keep moving left until you find X, then change it to blank and move right to search for the next 1.
Now, let's specify the transitions for this Turing machine:

States:

start: Initial state where the machine searches for a 1.
found_1: State where the machine has found a 1 and is searching for a blank to shift the 1.
found_blank: State where the machine has found a blank and is moving left to find the X.
found_X: State where the machine has found the X and is going back to the start state.
Transitions:

�
1
T 1 ​: (start, 0) -> (start, 0, right): If in start state and you read a 0, keep moving right.
�
2
T2 : (start, 1) -> (found_1, X, right): If in start state and you read a 1, change it to X and move right.
�
3
T3 : (found_1, 0) -> (found_1, 0, right): If you've found a 1 and you read a 0, keep moving right.
�
4
T4 : (found_1, 1) -> (found_1, 1, right): If you've found a 1 and you read another 1, keep moving right.
�
5
T5 : (found_1, blank) -> (found_blank, 1, left): If you've found a 1 and you read a blank, place a 1 and move left.
�
6
T6 : (found_blank, 0) -> (found_blank, 0, left): If in found_blank state and you read a 0, keep moving left.
�
7
T7 : (found_blank, 1) -> (found_blank, 1, left): If in found_blank state and you read a 1, keep moving left.
�
8
T8 : (found_blank, X) -> (start, blank, right): If in found_blank state and you read X, replace it with blank and go to start state.

Simulation transitions for tape 0110:

T1, T2, T4, T3, T5, T6, T8 results 00101
"""


"""
Assignment 3: Integer factorization

Step 1: Start with the smallest prime number, which is 2.
Is 57 ÷ 2
57÷2 an integer (i.e., is the remainder 0)? No, so 2 is not a factor.

Step 2: Move to the next prime number, which is 3.
Is 57 ÷ 3
57÷3 an integer? Yes, 
57÷3=19
57÷3=19. So, 3 is a prime factor of 57.

Now, continue the trial division for the quotient, which is 19.

Step 3: Check if 19 is divisible by 3 (since we've already tried 2).
No, 19÷3
19÷3 is not an integer.

Step 4: Move to the next prime number, which is 5.
Is 19÷5
19÷5 an integer? No, so 5 is not a factor.

Step 5: Move to the next prime number, which is 7.
However, note that 7 squared (49) is less than 57 but the next square of a prime number, 11 squared (121), is greater than 57. Hence, if 57 had any prime factors larger than 7 but smaller than itself, it would have to have a complementary factor smaller than 7 to multiply to 57. But we've already checked all primes less than 7, so we only need to check up to the square root of 57.

Therefore, 7 is the last number we need to check. Is 
19÷7
19÷7 an integer? No.

Since 19 is not divisible by any prime number less than its square root and is greater than 1, 19  itself is prime.


"""
def prime_factors(n):
    factors = []
    divisor = 2  # Start with the smallest prime number
    while n > 1:
        while n % divisor == 0:  # While n is divisible by divisor
            factors.append(divisor)
            n //= divisor
        divisor += 1  # Increment to the next integer
    return factors

number = 57
factors = prime_factors(number)
print(f"Prime factors of {number} are: {factors}")

# Question 2: 342=2×33×19

"""
Assignment 4: Parallelization and Kernel

1. The resulting matrice would be a 2 by four matrice

The resulting matrix  C will be a two by four matrix.


For the given matrices, there will be: 2 rows in matrix A multiplied by 4 columns in matrix 

B = 2×4=8 independent computations.

So, at most 8 parallel threads can run for this task.

Million by Million Matrix with another Million by Million Matrix:
If you have a matrix A of size 10^6×10^6 and another matrix B of the same size, the resulting matrix C will also be 
10^6×10^6.

So, you'll have up to
10^6×10^6 = 10^12
  independent computations.

Thus, in theory, you could have 
10^12*10^12
  parallel threads for this task.

However, practically speaking, running 
10^12*10^12
threads simultaneously is infeasible due to hardware constraints. 
In real-world scenarios, matrix multiplication at this scale often uses specialized algorithms 
(like the Strassen algorithm or the Coppersmith–Winograd algorithm) and hardware accelerators (like GPUs) that can handle large-scale parallelism 
efficiently, and techniques like data partitioning, tiling, and memory hierarchy optimizations to manage the data effectively.

2. a) P is a matrix because it represents the transition probabilities between each pair of states. With 5 states in our Markov Chain, there are 
5×5=25 possible transitions, hence 25 entries in the matrix.

Not any matrix can be a transition probability matrix. The conditions are:
    Each entry P(Si→Sj) must be in the range [0,1], because they represent probabilities.
    The sum of the probabilities in each row must be 1, meaning that from any state Si, the 
    probabilities of transitioning to all other states (including possibly staying in Si) must total 100%.

  b) The multiplication of the transition probability matrix P with a vector x gives the state distribution after one discrete time interval because it aggregates the transition probabilities for the initial state represented by x.
For a healthy person, the vector would be: 
x=[1,0,0,0,0] (100% probability of being healthy and 0% for all other states).

For a recovered person, the vector would be: 
x=[0,0,0,0,1] (100% probability of being recovered and 0% for all other states).  

"""

"""
Assignment 6:
1. The use case involving optimizing renewable energy storage and distribution is the most exciting.
2. Given Deloitte's reputation, I consider the claims to be credible, but would rely more on direct references provided.
3. Quantum computing in energy optimization is in early stages, with promising outcomes expected in the next decade.
4. Quantum computing could revolutionize drug discovery by simulating complex molecular interactions at unprecedented speeds.
"""