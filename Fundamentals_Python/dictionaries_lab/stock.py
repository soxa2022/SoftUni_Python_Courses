data = input().split()
lst_products = input().split()
my_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
# for i in range(0, len(data), 2):
#     key = data[i]
#     value = int(data[i + 1])
#     my_dict[key] = value
for product in lst_products:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
