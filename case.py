class Switch:
    def case_1(self):
        print('January')
    def case_2(self):
        print('February')
    def case_3(self):
        print('March')
    def case_4(self):
        print('April')
    def case_5(self):
        print('May')
    def case_6(self):
        print('June')
    def case_7(self):
        print('July')
    def case_8(self):
        print('August')
    def case_9(self):
        print('September')
    def case_10(self):
        print('October')
    def case_11(self):
        print('November')
    def case_12(self):
        print('December')

    def case(self, cases):
        method = 'case_' + str(cases)
        return getattr(self, method)()
        
print(f"O resultado foi:")
Switch().case(12)
