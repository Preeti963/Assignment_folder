
from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi

def main():
    print("Welcome to Finance App!")

    income = float(input("Enter your annual income: "))
    tax_rate = float(input("Enter tax rate (e.g., 0.1 for 10%): "))
    tax = calculate_tax(income, tax_rate)
    print(f"Your tax to pay: Rs.{tax:.2f}")

    principal = float(input("Enter loan principal amount: "))
    annual_rate = float(input("Enter annual interest rate (e.g., 0.08 for 8%): "))
    years = int(input("Enter loan tenure in years: "))
    emi = calculate_emi(principal, annual_rate, years)
    print(f"Your monthly EMI: Rs.{emi:.2f}")

if __name__ == "__main__":
    main()
