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



import datetime


class UpiPaymentTx:

    def __init__(self, sender_handle, receiver_handle, amount):
        self.sender_handle = sender_handle
        self.receiver_handle = receiver_handle
        self.amount = amount
        self.status = "PENDING"
        self.timestamp = datetime.datetime.now()


class Upi(UpiPaymentTx):

    def __init__(self, sender_handle, receiver_handle, amount):
        super().__init__(sender_handle, receiver_handle, amount)

    def execute_payment(self):
        if self.amount > 0:
            self.status = "SUCCESS"
            print(
                f"Transaction Successful: Sent ₹{self.amount} to {self.receiver_handle}"
            )
        else:
            self.status = "FAILED"
            print("Transaction Failed: Invalid amount.")
        return self.status


class UpiReceipt(Upi):

    def generate_receipt(self):
        print("\n===============================")
        print("     UPI TRANSACTION RECEIPT   ")
        print("===============================")
        print(f"Date & Time : {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"From        : {self.sender_handle}")
        print(f"To          : {self.receiver_handle}")
        print(f"Amount      : ₹{self.amount}")
        print(f"Status      : {self.status}")
        print("===============================\n")


# Example Usage
receipt = UpiReceipt(
    sender_handle="sampreeth@okaxis", receiver_handle="rahul@okhdfc", amount=500
)
receipt.execute_payment()
receipt.generate_receipt()



# create a dictionary  and take key as  phone number 

# Dictionary using Phone Number as the Key
# upi_user_db = {
#     "9876543210": {"user_id": "sampreeth", "bank_id": "@okaxis"},
#     "9123456789": {"user_id": "rahul", "bank_id": "@okhdfc"},
#     "9988776655": {"user_id": "ananya", "bank_id": "@ybl"},
# }


# def get_upi_id(phone_number):
#     """Retrieve user ID, bank ID, and full handle using phone number."""
#     user = upi_user_db.get(phone_number)
#     if user:
#         full_handle = f"{user['user_id']}{user['bank_id']}"
#         return {
#             "user_id": user["user_id"],
#             "bank_id": user["bank_id"],
#             "full_handle": full_handle,
#         }
#     return "Phone number not registered."


# # Example Usage
# phone_input = "9876543210"
# user_details = get_upi_id(phone_input)

# print(f"Phone Number : {phone_input}")
# print(f"User ID      : {user_details['user_id']}")
# print(f"Bank ID      : {user_details['bank_id']}")
# print(f"Full Handle  : {user_details['full_handle']}")
