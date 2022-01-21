gross_income=int(input("Enter gross income ="))
standard_deduction=10000
dependents=int(input("Enter the no. of dependents ="))
dependent_deduction=3000
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
print("Taxable income =",taxable_income)
tax=(taxable_income*20)/100
print("Tax =",tax)
