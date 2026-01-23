bill= int(input("enter total paid:"))
paid= int(input("enter amount paid:"))
def dueamount(bill,paid):
    due =bill-paid
    return due
print("due amount is ",dueamount(bill,paid))