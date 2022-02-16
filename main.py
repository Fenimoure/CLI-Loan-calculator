import math
import argparse

parser = argparse.ArgumentParser(description="Calculate things related to loans.")

parser.add_argument("--type", default=0)
parser.add_argument("--principal", default=0)
parser.add_argument("--payment", default=0)
parser.add_argument("--periods", default=0)
parser.add_argument("--interest", default=0)
arguments = parser.parse_args()


def calc_differentiating():
    p = float(arguments.principal)
    n = int(arguments.periods)
    i = float(arguments.interest) * 0.01 / 12
    D_mth = [int(math.ceil(p / n + i * (p - (p * m) / n))) for m in range(n)]
    overpayment = int(sum(D_mth) - p)
    for i in range(len(D_mth)):
        print("Month " + str(i + 1) + ': ' + "payment is " + str(D_mth[i]))
    print("\nOverpayment = " + str(overpayment))


def calc_annuity(inp):
    if inp == 'n':
        loan_principal = float(arguments.principal)
        monthly_payment = int(arguments.payment)
        loan_interest = float(arguments.interest) * 0.01
        i = loan_interest / 12
        num_of_payments = math.log((monthly_payment / (monthly_payment - i * loan_principal)), (1 + i))
        years = round(num_of_payments) // 12
        months = math.ceil(num_of_payments) % 12
        overpayment = math.ceil(math.ceil(num_of_payments) * monthly_payment - loan_principal)
        message = "It will take "
        message += (str(years) + " year" + "s " * (years != 1)) * (years != 0)
        message += "and " * (years != 0 and months != 0)
        message += (str(months) + " month" + "s" * (months != 1)) * (months != 0)
        message += " to repay this loan!"
        print(message, "\n\nOverpayment = ", overpayment)
    elif inp == 'a':
        loan_principal = float(arguments.principal)
        num_of_payments = int(arguments.periods)
        loan_interest = float(arguments.interest) * 0.01
        i = loan_interest / 12 * 1
        monthly_payment = math.ceil(loan_principal * (i * pow(1 + i, num_of_payments))/(pow(1 + i, num_of_payments) - 1))
        overpayment = math.ceil(monthly_payment * num_of_payments - loan_principal)
        print("Your monthly payment = " + str(monthly_payment) + "!")
        print("\nOverpayment = ", overpayment)
    elif inp == 'p':
        annuity_payment = float(arguments.payment)
        num_of_payments = int(arguments.periods)
        loan_interest = float(arguments.interest) * 0.01
        i = loan_interest / 12 * 1
        loan_principal = round(annuity_payment / ((i * pow(1 + i, num_of_payments))/(pow(1 + i, num_of_payments) - 1)))
        overpayment = math.ceil(num_of_payments * annuity_payment - loan_principal)
        print("Your loan principal = " + str(loan_principal) + "!")
        print("\nOverpayment = ", overpayment)


if arguments.type == "diff" and float(arguments.principal) * int(arguments.periods) * float(arguments.interest):
    calc_differentiating()
elif arguments.type == "annuity":
    if not arguments.periods and float(arguments.payment) * float(arguments.principal) * float(arguments.interest):
        calc_annuity('n')
    elif not arguments.payment and int(arguments.periods) * float(arguments.principal) * float(arguments.interest):
        calc_annuity('a')
    elif not arguments.principal and int(arguments.periods) * float(arguments.payment) * float(arguments.interest):
        calc_annuity('p')
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
