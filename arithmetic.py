import random
from fpdf import FPDF

class Arithmetic:
    def addict(self, n, result=False, max_result=20):
        # Generate two random numbers a and b such that their sum is less than or equal to max_result
        while True:
            a = random.randint(1, n)
            b = random.randint(1, n)
            if result:
                c = f"{a}+{b}={a+b}" 
            else:
                c = f"{a}+{b}={' ' * len(str(a + b))}"
            if a + b <= max_result:
                break
        return c
    
    def subtract(self, n, result=False):
        a = random.randint(1, n)
        b = n + 1
        while b > a:
            b = random.randint(1, n)
        if result:
            c = f"{a}-{b}={a-b}"
        else:
            c = f"{a}-{b}={' ' * len(str(a - b))}"
        return c
    
    def multiply(self, n, result=False):
        a = random.randint(1, n)
        b = random.randint(1, n)
        if result:
            c = f"{a}*{b}={a*b}"
        else:
            c = f"{a}*{b}={' ' * len(str(a * b))}"
        return c

    def generate_pdf(self, text, filename="output.pdf", columns=1):
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        square_size = 5  # in mm
        print_rec = False  # Print rectangle around the text

        n_lines = len(text) // columns + (len(text) % columns > 0)
        print(n_lines, columns)
        if n_lines > 40:
            raise ValueError("Too many lines to fit in a single page.")
        if isinstance(text, list):  # Check if text is a table
            text = "\n".join(text)  # Convert table to string format
        start_column_x = 10  # Starting x position for columns
        start_column_y = 10  # Starting y position for rows
        x, y = start_column_x, start_column_y  # Starting position
        line = 1
        prev_char = ' '
        column = 1  # Track the current column
        for char in text:
            if char == "\n":  # Handle line break
                x = start_column_x
                y += square_size + 1
                line += 1
                if line > n_lines:
                    line = 1
                    y = start_column_y  # Reset y position for new column
                    start_column_x = 70 * column + 10  # Adjust x position for new column
                    x = start_column_x
                    column += 1
                    print(column, x, y)
                print_rec = False
                continue
            if prev_char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and not print_rec:
                x += -3
                # print(prev_char, char)
            # print(prev_char, char)
            prev_char = char
            if print_rec:
                pdf.rect(x, y, square_size, square_size)  # Draw square
            pdf.text(x + 1, y + 4, char)  # Add character inside square
            x += square_size + 1  # Move to the next position
            if char == "=":
                print_rec = True  # Reset rectangle printing after '='
        pdf.output(filename)
    

    def generate_table(self, num_examples, max_num, optons=["addict"]):
        # Generate a table of arithmetic problems based on the selected options
        table = []
        print(len(optons), optons)
        for i in range(num_examples):
            operation = random.choice(optons)
            print(operation)
            if operation == "addict":
                row = self.addict(max_num, False, 10)
            elif operation == "subtract":
                row = self.subtract(max_num, False)
            elif operation == "multiply":
                row = self.multiply(max_num, False)
            else:
                raise ValueError(f"Unknown operation: {operation}")
            table.append(row)
        return table
        

if __name__ == "__main__":
    arith = Arithmetic()
    # Example usage
    options = ["addict", "subtract"]
    arith.generate_pdf(arith.generate_table(120, 10, options), "example.pdf", 3)
