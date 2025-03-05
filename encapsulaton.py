class bank_section:
    def __init__(self,bankname,accountnumber,pinnumber):
        self.bankname=bankname
        self._accountnumber=accountnumber
        self.__pinnumber=pinnumber
    def public(self):
        print(f" i am gowsalya account in lawspet branch{self.bankname}")
    def protect(self):
        print(f"my account numbers{self._accountnumber}")
    def private(self):
        print(f"pin numbers is{self.__pinnumber}")
obj=bank_section("lawspet","123456789023","220822")
obj.public()
obj.protect()
obj.private()
    