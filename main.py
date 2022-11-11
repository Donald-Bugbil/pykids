import containers.string_container as strCon

stcon = strCon.StringContainer("Donald", "Bugbil", "Moore", "Marian")
stcon_two = strCon.StringContainer("Apana", "Ayine", "Aduko", "John")

total = stcon + stcon_two

if __name__ == "__main__":
    print(total)