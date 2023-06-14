def calculate_tax(yearly_salary):

    tax_brackets = [
        (0, 22000, 0.1),
        (22001, 89450, 0.12),
        (89451, 190750, 0.22),
        (190751, 364200, 0.24),
        (364201, 462500, 0.32),
        (462501, 693750, 0.35),
        (693750, float('inf'), 0.37)
    ]

    tax_owed = 0
    salary_remaining = yearly_salary

    for bracket in tax_brackets:
        bracket_min, bracket_max, tax_rate = bracket
        if salary_remaining <= 0:
            break

        taxable_income = min(salary_remaining, bracket_max - bracket_min + 1)
        tax_owed += taxable_income * tax_rate
        salary_remaining -= taxable_income

    return tax_owed



salary = int(input("How much does your household bring in a year?: "))
tax_owed = calculate_tax(salary)
print("Total tax owed:", "$",tax_owed, sep="")
