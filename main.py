# This is a coding Task from Adil for Itemis.

# Extract input from test file and put it in lines list

def extract_input():
    try:
        lines = [line.strip() for line in open('test.txt', "r")]
        print(lines)
    except FileNotFoundError as e:
        print('File Not Found', e)

# all tax calculation will happen here
def tax_calculator():

if __name__ == '__main__':
    extract_input()
