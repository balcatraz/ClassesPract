import InsectClass as i


def main():
    mantis = i.Insect()

    print("The Mantis has flown ", mantis.get_lof(), " miles.", sep="")

    mantis.fly()

    print("The Mantis has flown ", mantis.get_lof(), " miles.", sep="")


main()
