units_consumed = int(input("Enter unit value: "))
is_senior_citizen = (input("Are you senior citizen(yes/no):"))
has_solar_panel = input(" Are you having solar panel (yes/no):")
payment_mode = input("payment mode(online/offline):")
#base charge calculation
if units_consumed <= 100:
    base_bill = units_consumed* 3
elif units_consumed <= 300:
    base_bill = (100*3) + (units_consumed - 100) *5
else:
    base_bill = (100*3) + (200*5)+(units_consumed -300)*8
#senior citizen discount
if is_senior_citizen == "yes":
    total_bill = base_bill * 0.90
else:
    total_bill = base_bill
#Solar panel
if has_solar_panel == "yes":
 if units_consumed <= 250:
  base_bill = base_bill - 500
else:
   base_bill = base_bill - 300
# payment mode surcharge
surcharge = 0
if payment_mode == "offline":
   if base_bill <1000:
    surcharge += 50
   elif base_bill>=1000:
    surcharge += 100
elif payment_mode == "online":
  total_bill = base_bill + surcharge
#Minimum payable
if total_bill < 200:
   total_bill = 200
print("Final Bill Amount:",total_bill)

