list = {"city": "Москва",
        "temperature": "20"}
print(list["city"])
list["temperature"] = type(list["temperature"])(int(list["temperature"])-5)
print(list["temperature"])
print()
a = type(5)("10")
print(a)


print(list.get("country", "Россия"))


list["date"] = "29.03.2019"
print(list)
print(len(list))











