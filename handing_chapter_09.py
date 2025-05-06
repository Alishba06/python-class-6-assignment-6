#  Example (with explanation)

# try:
#     result = 10 / 0         # Yahan error aayegi (ZeroDivisionError)

# except:

#     print("Error a gayi! kuch to galat hai.")



# Example (Specific Error Catch)

# try:

#     num = 10 / 0

# except ZeroDivisionError:
#     print("Zero se divide nahi kar sakte")



# Example (Generic Except)


# try:
#     x = int("abc")

# except:
#     print("Kuch error hui hai!")




# Example ( The else Block )


# try:
#     result = 10 / 2 

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print(f"Division successful. Result:{result}")



# Example (The finally Block )


# try:
#     result = 10 / 0

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("This will always execute")




# Example (Putting It All Together)

def divide_numbers(a , b):
    try:
        result = a / b 

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except TypeError:
        print("Error: Invalid input type. Numbers required")
    
    else:
        print(f"Division successful. Result: {result}")

    finally:
        print("Operation complete.\n")



divide_numbers(10 , 2)
divide_numbers(10 , 0)
divide_numbers(10 , "2")

