class Central_gov: # suepr_parent
    def funds(self):
        print("central gov funds")
    def s_funds(self):
        print('Central gov fund')
class State_gov(Central_gov): # Parent
    def s_funds(self):
        print('State gov fund')
        super().s_funds()
    def funds(self):
        print('Central fund in State')
        #super().funds()
s = State_gov()
s.s_funds()
class Local_gov(State_gov): # child
    pass
l = Local_gov()
l.funds()
l.s_funds()