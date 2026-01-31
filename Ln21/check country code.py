country_code={"Saudi Arabia":"00966","Pakistan":"0092","Canada":"0001"}

print("The country code of Saudi Arabia is")
print(country_code.get("Saudi Arabia","NOT FOUND"))

print("The country code of USA is")
print(country_code.get("USA","NOT FOUND"))