#
import petinfo
#
#
#
# --- Main program --- #
def main():
    #
    # user input
    name = input("Enter the name of your pet: ")
    print(f"You entered {name} as the name of your pet")

    age = float(input("Enter the age (numbers only) of your pet: "))
    print(f"You entered {age} as the age of your pet")

    pet_type = input("Enter the type of your pet (dog, bird, snake, cat, etc.): ")
    print(f"You entered {pet_type} as the type of your pet")
    
    # create pet object
    pet = petinfo.Pet(name, pet_type, age)
    
    # Display pet information
    print(pet)
    #
#
#
#

# call main function
if __name__ == "__main__":
    main()