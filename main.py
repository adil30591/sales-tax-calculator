# This is a coding Task from Adil for Itemis.

# Extract input from test file and put it in lines list

def extract_input():
    try:
        return [line.strip() for line in open('test.txt', "r")]
    except FileNotFoundError as e:
        print('File Not Found', e)


# all tax calculation will happen here
def tax_calculator():
    exempt_items = ["book", "chocolate", "capsule", "pills"]
    purchase = extract_input()
    for line in purchase:
        raw_str, _, item_price = line.rsplit(maxsplit=2)
        # currently as it is read from file,so it is string explicitly converting to float
        item_price = float(item_price)
        item_str = raw_str[2:]
        quantity = int(raw_str[0])
        if not any(e_item in raw_str[2:] for e_item in exempt_items):
            print("true")
        if "import" in raw_str:
            print("imported")

if __name__ == '__main__':
    tax_calculator()
