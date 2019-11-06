if __name__ == "__main__":
    sample_list = range(10)

    new_list = [i for i in sample_list if i % 2 == 0]
    new_dict = {i: i for i in sample_list if i % 2 == 0}
    new_set = {i for i in sample_list if i % 2 == 0}
    new_gen = (i for i in sample_list if i % 2 == 0)

    print(f"Input List: {sample_list}")
    print(f"Using List comprehension {type(new_list)}: {new_list}")
    print(f"Using Dict comprehension {type(new_dict)}: {new_dict}")
    print(f"Using Set comprehension {type(new_set)}: {new_set}")
    print(f"Using Generator comprehension {type(new_gen)}: {new_gen}")
    print([i for i in new_gen])
