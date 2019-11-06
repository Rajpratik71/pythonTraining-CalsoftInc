def mut(bar):
    bar.append(42)
    print(bar)


answer_list = [0]
foo(answer_list)
print(answer_list)


def immut(bar):
    bar = "new value"
    print(bar)


answer_list = "old value"
foo(answer_list)
print(answer_list)
