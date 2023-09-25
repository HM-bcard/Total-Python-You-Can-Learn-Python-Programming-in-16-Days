strin = ',:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#'
print(strin.lstrip(' ,:_%# '))

# 2

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3,'orange')

# 3

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = phone_brands.isdisjoint(tv_brands)
