def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"


def main():
    while True:
        user_input = input("Enter student's score (0-100): ")

        try:
            score = float(user_input)  # handling decimal scores too

            # Rejecting values outside 0-100
            if score < 0 or score > 100:
                print("Error: Score must be between 0 and 100. Try again.")
                continue

            # Displaying the corresponding grade
            grade = get_grade(score)
            print(f"Score: {score} → Grade: {grade}")
            break  # exit loop after valid input

        except ValueError:
            # Handle invalid input like letters, symbols
            print("Error: Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()