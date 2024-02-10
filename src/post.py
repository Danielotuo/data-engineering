# import logging

# # Configure logging settings
# logging.basicConfig(filename='positive_number_checks.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


# def is_positive(number):
#     logging.debug(f"Checking if {number} is positive.")
#     if number > 0:
#         logging.info(f"{number} is a positive number.")
#     else:
#         logging.error(f"Error! {number} is not a positive number.")


# # Example usage
# is_positive(2024)


class InvalidDataFormat(Exception):
    """Exception raised if data has an invalid format.

    Attributes:
        data -- input data
        message -- error description
    """

    def __init__(self, data):
        self.data = data
        self.message = f"Invalid data format detected: {self.data}"

        super().__init__(self.message)


try:
    # Simulating data validation
    user_input = input("Enter data for validation: ")

    if not user_input.isnumeric():
        raise InvalidDataFormat(user_input)

except InvalidDataFormat as error:
    print(f"Error: {error}. Please enter numeric data.")
except Exception as error:
    print(f"An unexpected error occurred: {error}")
finally:
    print("This code will always execute, even if an exception is raised.")
