import CellPhoneClass as c


def main():
    phone = c.cellphone("Apple", "iPhone 11", 700.00)

    print(phone.get_manufact(), phone.get_model(), phone.get_retail_price())

    phone.set_manufact("Samsung")
    phone.set_model("Galaxy")
    phone.set_retail_price(500.00)

    print(phone.get_manufact(), phone.get_model(), phone.get_retail_price())


main()
