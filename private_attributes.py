class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)

A1 = Account("12345", "abcde")
print(A1.acc_no)
print(A1.reset_pass)