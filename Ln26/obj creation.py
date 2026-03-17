class employee:
    def __init__(Self):
        print("object created")
    def __del__(self):
        print("destructor called")

def create_obj():
    print("making object ...")
    obj=employee()
    print("function end")
    return obj

print("calling create_obj function ...")
obj=create_obj()
print("program end")