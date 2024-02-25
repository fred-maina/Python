def main():
    #main function of the program
    name=input("Input Your Name: ")#asks user for their name
    age=int(input("Input Your Age:"))# Takes users input for age and converts it to an integer
    Location=input("Input your Location: ")#takes user input for location and saves it in location
    print(f"Hello, {name}. You are {age} years old, and you come from {Location}.")#uses string formatting to output the details collected from the user
main()