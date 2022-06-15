#pyhton is object oriented ,funcional oriented and procedure oriented programming
# in python we can define a function inside a function. in node js we can call a function we cannot define
def check_scope():
    def do_local():
        test="local test"
    def do_non_local():
        nonlocal test
        test="non local test"
    def do_global():
        test="global test"

    test="default"#this test is working in this case
    do_local()
    print("test value after do local: "+test)
    do_non_local()
    print("test value after do non local: " + test)

check_scope()