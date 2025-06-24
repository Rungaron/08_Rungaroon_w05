# คำนวณภาษี
salary = 15000
tax = 0.07
ot_time = 10
ot_rate = 200

gross_pay = salary + (ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay = gross_pay - tax_pay

print(f"{net_pay}")