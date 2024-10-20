# Homework for Module 1, topic "Dictionaries and Sets".
my_dict = {"Pi": 3.141593, "e": 2.718282, "Tau": 6.283185, "Golden Ratio": 1.618034}
print("Dictionary:", my_dict)
print("Existing value:", my_dict["Golden Ratio"])
print("Non-existing value:", my_dict.get("Lambda"))
my_dict.update({"Root2": 1.414214, "Root3": 1.732051})
print("Deleted value", my_dict.pop("Tau"))
print("Modified dictionary:", my_dict)
print()
my_set = {17, "Pi", 3.14, "e", 2.72, "Golden Ratio", 3.14, "e", True, 17}
print("Set:", my_set)
my_set.update(["20.10.2024", "Huawei"])
my_set.remove("Golden Ratio")
print("Modified set:", my_set)
