import os

def process_file(input_filepath, output_filepath):
    """
    Processes a file, placing each value on a new line and removing commas.

    Args:
        input_filepath: Path to the input file.
        output_filepath: Path to the output file.
    """
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile, \
                open(output_filepath, 'w', encoding='utf-8') as outfile:
            for line in infile:
                values = line.strip().split(',')  # Split by comma, remove leading/trailing whitespace
                for value in values:
                    outfile.write(value.strip() + '\n')  # Write each value to a new line

        print(f"File '{input_filepath}' processed successfully. Results written to '{output_filepath}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example Usage:  Replace with your actual file paths
input_file = "itog.txt"  # Or input.csv, etc.
output_file = "itog-1.txt"

# Ensure the input file exists before proceeding.  You can add more robust file type checks here if needed.
if os.path.exists(input_file):
    process_file(input_file, output_file)
else:
    print(f"Error: Input file '{input_file}' does not exist.")

