def calc_average():  
    # Calculates the average of 8 scores entered by the user
    total = sum(float(input(f"Please enter score #{i}:")) for i in range(1, 9))  
    # Prompts user to enter each score, converts it to float, sums them, and stores in total
    return int(total / 8)  
    # Divides the total by 8 to get the average, converts to integer, and returns it

def determine_grade(score):  
    # Determines the letter grade based on the average score
    if score >= 90:
        return "A"  # Returns 'A' for scores 90 and above
    elif score >= 80:
        return "B"  # Returns 'B' for scores 80-89
    elif score >= 70:
        return "C"  # Returns 'C' for scores 70-79
    elif score >= 60:
        return "D"  # Returns 'D' for scores 60-69
    return "F"  # Returns 'F' for scores below 60

def main():  
    # Main function to execute the program
    avg = calc_average()  # Calls calc_average to get the average score
    print("Your average grade is:", determine_grade(avg))  
    # Calls determine_grade with the average score and prints the grade

if __name__ == "__main__":  
    main()  # Runs the main function if the script is executed directly
