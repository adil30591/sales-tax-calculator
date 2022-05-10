# This is a coding Task from Adil for Itemis.

# Extract input from test file and put it in lines list
def extract_input():
    try:
        return [line.strip() for line in open('test.txt', "r")]
    except FileNotFoundError as e:
        print('File Not Found', e)


def myround(x, digits=2, base=.05):
    return round(base * round(float(x) / base), digits)


# all tax calculation will happen here
def tax_calculator():
    # Basic items declaration which are exempt from sales tax
    exempt_items = ["book", "chocolate", "capsule", "pills"]
    sales_tax_total = 0
    total = 0

    def percent_calc(x, y):
        return x * (y / 100)

    # Get data from file test.txt
    purchase = extract_input()
    for line in purchase:
        # initializing
        sales_tax_basic = 0
        sales_tax_import = 0
        # split from right two times first for price second to drop "at" from string
        raw_str, _, item_price = line.rsplit(maxsplit=2)
        # currently as it is read from file,so it is string explicitly converting to float
        item_price = float(item_price)
        # Item extracted from whole String 2: mean leave first 2 and grab the rest
        item_str = raw_str[2:]
        # Quantity from first index of string
        quantity = int(raw_str[0])

        # if item is not exempted apply sales tax
        if not any(e_item in raw_str[2:] for e_item in exempt_items):
            sales_tax_basic = myround(percent_calc(item_price, 10)) * quantity
            sales_tax_total += sales_tax_basic

        # If import in string calculate import additional tax
        if "import" in raw_str:
            sales_tax_import = myround(percent_calc(item_price, 5)) * quantity
            sales_tax_total += sales_tax_import

        # final item price includes all the sales tax applicable
        item_price = (item_price * quantity) + sales_tax_basic + sales_tax_import
        print(str(quantity) + " " + item_str + ": " + str(round(item_price, 2)))
        total += item_price

    # Sales Tax and Total upto two decimal places
    print("Sales Taxes: {0:.2f}".format(sales_tax_total))
    print("Total: {0:.2f}".format(total))


if __name__ == '__main__':
    tax_calculator()
