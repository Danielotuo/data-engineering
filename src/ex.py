import logging

# Configure logging settings
logging.basicConfig(filename='data_validation.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def is_data_valid(data):
    logging.debug(f"Checking validity of data: {data}")

    # Assuming data validation logic
    if validate_data(data):
        logging.info(f"Data: {data} is valid.")
    else:
        logging.error(f"Error! Invalid data detected: {data}")


def validate_data(data):
    # Placeholder for data validation logic
    # Return True if data is valid, otherwise False
    return len(data) > 0  # Example: Data is valid if it's not empty


def main():
    sample_data = "ExampleData"

    # Example usage of is_data_valid function
    is_data_valid(sample_data)


if __name__ == "__main__":
    main()
