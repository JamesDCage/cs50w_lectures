print("Hello, world!")

def say_hi(name):
    print("Hello ", name)

def say_bye(name):
    print("Goodbye, ", name)

def say_it(with_what, to_who):
    return with_what(to_who)

say_it(say_hi, "Fred")


say_hi("Jimmy")

print(say_it)