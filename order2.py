class OrderSystem:
    def _init_(self):
        self.total_amount = 0

    def calculate_bill(self):
      
       items_count = int(input("Enter number of items: "))
        for i in range(items_count):
            price = float(input(f"Enter price for item {i+1}: "))
            self.total_amount += price 

        #  Taking other details
        dist = float(input("Enter distance: "))
        customer_type = input("Enter customer type (prime/normal): ")
        pmode = input("Enter payment mode (online/offline): ")
       #Adding discount
        if self.total_amount >= 1000:
            self.total_amount -= (self.total_amount * 0.10) 
        elif self.total_amount >= 500:
            self.total_amount -= (self.total_amount * 0.05) 
        # Prime customer check
        if customer_type == "prime" and self.total_amount > 1000:
            self.total_amount -= (self.total_amount * 0.15)

        # Distance and Payment charges
        if dist > 10:
            self.total_amount += 100
        elif dist > 5:
         self.total_amount += 50

        if pmode == "offline":
            self.total_amount += 20

        print("Final Bill Amount:", self.total_amount)

order = OrderSystem()
order.calculate_bill()
