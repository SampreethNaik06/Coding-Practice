# to create the upi id creation


# class UpiId:
#     def __init__(self,id,bank_id):
#         self.my_id = id 
#         self.my_bank_id = bank_id
#     def __repr__(self):
#         return "upi " + self.my_id + "@ " + self.my_bank_id
#     def __eq__(self,other):
#         return self.my_bank_id == other.my_bank_id and self.my_id == other.my_id
        

# sam = UpiId("1234567891","okaxis")
# lan = UpiId("1234567891","okaxis")
# print(sam == lan)
# print(sam is lan)

# create a dictionary  and take key as  phone number 

def create_handle(uid,bank_id):
    return (uid,bank_id)

def read_id(uh):
    return uh[0]

def read_bank_id(ug):
    return ug[1]




print(create_handle("sampreeth","@okaxis"))



class UpiPaymentTx:
    pass

class upi(UpiPaymentTx):
    def __int__():
        pass
class upireceipt(upi):
    pass

