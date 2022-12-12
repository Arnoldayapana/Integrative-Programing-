#SalaryDeductions.py
def tax(gross):
    return gross * 0.12


def rate(hour):
    return 500 * hour


def TotalDeductions(tax2, insurance, loan):
    return tax2 + insurance + loan