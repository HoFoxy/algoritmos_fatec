
birth_year = int(input("Insira seu ano de nascimento!"))
year_now = 2023
years_old = year_now - birth_year
months = years_old*12
days = years_old * 365
weeks = years_old * 52.17
print(f"Você nasceu em {birth_year}, tem {years_old} anos, {months} meses, {weeks:.0f} semanas e {days} dias")