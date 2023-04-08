# untuk membuat table
from tabulate import tabulate

# square root, untuk menghitung euclidean distance
from math import sqrt

class Membership:
    
    # inisialisasi data
    database_user = {
        'Sumbul': 'Platinum', 
        'Ana': 'Gold', 
        'Cahya': 'Platinum'
    }
    
    table_membership = {
        'Platinum' : ['Platinum', 15, 'Voucher Makanan + Voucher Ojek Online + Voucher Liburan + Cashback max 30%'],
        'Gold' : ['Gold', 10, 'Voucher Makanan + Voucher Ojek Online'],
        'Silver' : ['Silver', 8, 'Voucher Makanan'],
        'Standard' : ['Standard', 5, '-']
    }
    
    table_requirements = {
        'Platinum': ['Platinum', 8, 15],
        'Gold' : ['Gold', 6, 10],
        'Silver' : ['Silver', 5, 7],
        'Standard' : ['Standard', 1, 3]
    }
    
    def __init__(self, username):
        self.username = username
        self.database_user[username] = ''
        
        
    def check_all_membership(self):
        table = [value for key, value in self.table_membership.items()]
        header = ['Membership', 'Diskon %', 'Benefit']
        print(tabulate(table, header))
        
        
    def check_requirements(self):
        table = [value for key, value in self.table_requirements.items()]
        header = ['Membership', 'Monthly Expense', 'Monthly Income']
        print(tabulate(table, header))
        
        
    def predict_membership(self, username, monthly_expense, monthly_income):
        distance = {}
        
        for key, value in self.table_requirements.items():
            temp = round(sqrt((monthly_expense - self.table_requirements[key][1])**2 \
                        + (monthly_income - self.table_requirements[key][2])**2), 2)
            distance[key] = temp
            
        print(f'Hasil perhitungan Euclidean Distance dari user {username} adalah {distance}')
        
        for key, value in distance.items():
            if value == min(distance.values()):
                self.database_user[username] = key
                return key
          
    
    def check_membership(self, username):
        if username in self.database_user.keys():
            return self.database_user[username]
    
    
    def calculate_bill(self, username, list_harga):
        total = sum(list_harga)
        
        try:
            if username in self.database_user.keys():
                membership_type = self.database_user[username]
                if membership_type != '':
                    discount = self.table_membership[membership_type][1] / 100
                    return (1 - discount) * total
                else: 
                    raise Exception(f'Lakukan prediksi membership pada user {username}')
            else:
                raise Exception('User tidak ditemukan')

        except Exception as e:
            print(e)


peni = Membership('peni')
peni.check_all_membership()
peni.check_requirements()
print(peni.predict_membership(peni.username, 1, 2))
print(peni.calculate_bill(peni.username, [150_000, 200_000, 400_000]))