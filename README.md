# Grade-calc
> **Programming Principles Assignment**  
> *Kennesaw State University - MS Cybersecurity Program*

This was one of several assignments needed to pass the **Programming Principles** module. 

---

### 🎓 Assignment Description: Grading Program

The program should calculate the average of 8 test scores and display the corresponding letter grade.

#### Functions to Implement

1. **`calc_average`**  
   Prompts for 8 test scores and returns the average.

2. **`determine_grade`**  
   Accepts the average score and returns the corresponding letter grade based on this scale:

   | Score Range | Grade |
   |-------------|-------|
   | 90-100      | A     |
   | 80-89       | B     |
   | 70-79       | C     |
   | 60-69       | D     |
   | Below 60    | F     |

---

### Code Breakdown
calc_average() Function
Prompts the user to enter eight scores, calculates the sum of these scores, and returns the integer average. This function gathers all scores in a single line using a loop within a summation.

determine_grade(score) Function
Accepts the average score as input and returns a letter grade. The function uses a series of conditional checks to assign letter grades:

A for scores 90 and above
B for scores 80-89
C for scores 70-79
D for scores 60-69
F for scores below 60
main() Function
Calls calc_average() to get the average score, passes that average to determine_grade(), and prints the final letter grade to the user.

__name__ Check
Ensures that the program runs only if executed directly, not when imported as a module.


   
