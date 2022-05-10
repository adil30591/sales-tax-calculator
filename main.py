# This is a coding Task from Adil for Itemis.

# Extract input from test file and put it in lines list

def extract_input():
    try:
        return [line.strip() for line in open('test.txt', "r")]
    except FileNotFoundError as e:
        print('File Not Found', e)

def myround(x, digits=2, base=.05):
  return round(base * round(float(x)/base),digits)

# all tax calculation will happen here
def tax_calculator():
    exempt_items = ["book", "chocolate", "capsule", "pills"]
    sales_tax_total = 0
    summe = 0
    p = lambda x: x / 100
    purchase = extract_input()
    for line in purchase:
        sales_tax_basic = 0
        sales_tax_import = 0
        raw_str, _, item_price = line.rsplit(maxsplit=2)
        # currently as it is read from file,so it is string explicitly converting to float
        item_price = float(item_price)
        item_str = raw_str[2:]
        quantity = int(raw_str[0])
        # if item is not exempted apply sales tax
        if not any(e_item in raw_str[2:] for e_item in exempt_items):
            sales_tax_basic = myround(item_price * p(10))
            print(sales_tax_basic)
            sales_tax_total += sales_tax_basic
        if "import" in raw_str:
            sales_tax_import = myround(item_price * p(5))
            print(sales_tax_import)
            sales_tax_total += sales_tax_import
        item_price += sales_tax_basic + sales_tax_import
        # final item price includes all the sales tax applicable
        print(str(quantity) + " " + item_str + ": " + str(round(item_price, 2)))
        summe += item_price
    print("Sales Taxes: {0:.2f}".format(sales_tax_total))
    print("Total: {0:.2f}".format(summe))
if __name__ == '__main__':
    tax_calculator()
