MENU_ITEM = {
    "R1_Pizza": {"special_content": "bla,bla,bla", "price": 1000},
    "R2_Pizza": {"special_content": "bla,bla,bla", "price": 3000},
    "R3_Pizza": {"special_content": "bla,bla,bla", "price": 5000},
    "R4_Pizza": {"special_content": "bla,bla,bla", "price": 6000},
}


class Bill:
    def __init__(self, menu_item, my_purchase, name):
        self.menu_item = menu_item
        self.__my_bucket = my_purchase
        self.__total_amt = 0
        self.customer_name = name

    def __str__(self) -> str:
        return "Our Menu: " + ", ".join(self.menu_item.keys())

    def finalAmount(self, discount=None):
        
        if discount is None:
            bill = self.get_bill()
            

            for key in bill:
                count = bill[key]['count']
                cost = bill[key]['cost']
                self.__total_amt += count*cost
        return self.__total_amt
    
    def get_total(self):
        return self.finalAmount()

    def get_bill(self):
        return self.__my_bucket

    def storeBill(self):
        import random

        num = random.randint(1, 10000)
        bill_name = self.customer_name + str(num)
        with open(bill_name, 'w') as f:
            f.write("Customer Name: " + self.customer_name + "\n")
            f.write("Purchased Items:\n")
            for item, data in self.__my_bucket.items():
                f.write(f"{item}: {data['count']} x {data['cost']} = {data['count'] * data['cost']}\n")
            f.write("Total Amount: " + str(self.get_total()))


my_purchase = {
    "R1_Pizza": {"count": 1, "cost": 1000},
    "R2_Pizza": {"count": 2, "cost": 2000},
}

#bill_cust1 = Bill(MENU_ITEM, my_purchase, "Ashesh")
#bill_cust1.storeBill()

#Above code disobey SRP principles
#because if we want to make changes int save method like save in differrent storage 
#and also if somme private method above is changed and its impact will be propagated to 
#save which will create conflict so breaking into different class


class SaveBillDb:
    def storeBill(self, Bill):
        import random

        num = random.randint(1, 10000)
        bill_name = Bill.customer_name + str(num)
        with open(bill_name, 'w') as f:
            f.write("Customer Name: " + Bill.customer_name + "\n")
            f.write("Purchased Items:\n")
            for item, data in Bill.get_bill().items():
                f.write(f"{item}: {data['count']} x {data['cost']} = {data['count'] * data['cost']}\n")
            f.write("Total Amount: " + str(Bill.get_total()))

bill_cust1 = Bill(MENU_ITEM, my_purchase, "Ashesh")
savedb1 = SaveBillDb()
savedb1.storeBill(bill_cust1)