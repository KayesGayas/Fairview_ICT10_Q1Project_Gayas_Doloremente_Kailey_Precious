# Project Reciept and SKU 
from pyscript import document


Me_nu = {
    'Buldak Carbonara': 75.00,
    'Buldak 2x Spicy': 65.00,
    'Buldak Cheese': 104.00,
    'Buldak Creamy Carbonara': 68.00,
    'Buldak Spicy': 106.00,

    'Iced Tea': 55.00,
    'Fresh Milk': 60.00,

    'Coke': 45.00,

    'Chocolate Slice': 120.00,
    'Ice Cream': 45.00
}


def generate_receipt(event=None):

    subtotal = 0.00

    buldakcarbonara = document.getElementById(
        'buldakcarbonara'
    ).checked

    buldak2xspicy = document.getElementById(
        'buldak2xspicy'
    ).checked

    buldakcheese = document.getElementById(
        'buldakcheese'
    ).checked

    buldakcreamycarbonara = document.getElementById(
        'buldakcreamycarbonara'
    ).checked

    buldakspicy = document.getElementById(
        'buldakspicy'
    ).checked

    icedtea = document.getElementById(
        'icedtea'
    ).checked

    freshmilk = document.getElementById(
        'freshmilk'
    ).checked

    coke = document.getElementById(
        'coke'
    ).checked

    chocolateslice = document.getElementById(
        'chocolateslice'
    ).checked

    icecream = document.getElementById(
        'icecream'
    ).checked


    subtotal += buldakcarbonara * Me_nu[
        'Buldak Carbonara'
    ]

    subtotal += buldak2xspicy * Me_nu[
        'Buldak 2x Spicy'
    ]

    subtotal += buldakcheese * Me_nu[
        'Buldak Cheese'
    ]

    subtotal += buldakcreamycarbonara * Me_nu[
        'Buldak Creamy Carbonara'
    ]

    subtotal += buldakspicy * Me_nu[
        'Buldak Spicy'
    ]

    subtotal += icedtea * Me_nu[
        'Iced Tea'
    ]

    subtotal += freshmilk * Me_nu[
        'Fresh Milk'
    ]

    subtotal += coke * Me_nu[
        'Coke'
    ]

    subtotal += chocolateslice * Me_nu[
        'Chocolate Slice'
    ]

    subtotal += icecream * Me_nu[
        'Ice Cream'
    ]


    vat = subtotal * 0.12

    total_amount = subtotal + vat


    receipt = f"""
    <h3>=== Receipt ===</h3>

    Buldak Carbonara: ₱{buldakcarbonara * Me_nu['Buldak Carbonara']:.2f}<br>

    Buldak 2x Spicy: ₱{buldak2xspicy * Me_nu['Buldak 2x Spicy']:.2f}<br>

    Buldak Cheese: ₱{buldakcheese * Me_nu['Buldak Cheese']:.2f}<br>

    Buldak Creamy Carbonara: ₱{buldakcreamycarbonara * Me_nu['Buldak Creamy Carbonara']:.2f}<br>

    Buldak Spicy: ₱{buldakspicy * Me_nu['Buldak Spicy']:.2f}<br>

    Iced Tea: ₱{icedtea * Me_nu['Iced Tea']:.2f}<br>

    Fresh Milk: ₱{freshmilk * Me_nu['Fresh Milk']:.2f}<br>

    Coke: ₱{coke * Me_nu['Coke']:.2f}<br>

    Chocolate Slice: ₱{chocolateslice * Me_nu['Chocolate Slice']:.2f}<br>

    Ice Cream: ₱{icecream * Me_nu['Ice Cream']:.2f}<br>

    <br>

    Subtotal: ₱{subtotal:.2f}<br>

    VAT: ₱{vat:.2f}<br>

    Total Amount: ₱{total_amount:.2f}
    """

    document.getElementById(
        "receipt_result"
    ).innerHTML = receipt


def generate_sku(event=None):

    category = document.getElementById(
        "category"
    ).value

    product = document.getElementById(
        "product"
    ).value

    stock = document.getElementById(
        "stock"
    ).value


    if category == "" or product == "" or stock == "":

        document.getElementById(
            "sku"
        ).innerHTML = "Please fill in all fields."

        return


    category = category[:3].upper()

    product = product[:3].upper()


    sku = category + "-" + product + "-" + stock


    document.getElementById(
        "sku"
    ).innerHTML = sku
