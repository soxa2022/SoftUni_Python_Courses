def concatenate(*args, **kwargs):
    # main_string = ""
    # for el in args:
    #     main_string += el
    main_string = ''.join(args)
    for key in kwargs:
        if key in main_string:
            main_string = main_string.replace(key, kwargs[key])
    return main_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
