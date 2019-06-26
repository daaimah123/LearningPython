class A: 
    def do_something(self):
        print('Method Defined In: A')

class B(A): 
    def do_something(self):
        print('Method Defined In: B')

class C(A): 
    def do_something(self):
        print('Method Defined In: C')

class D(B, C): 
    pass
    # def do_something(self):
    #     print('Method Defined In: D')

thing = D()
thing.do_something()