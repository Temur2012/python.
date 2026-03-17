import json

data ={"Model" : "Malibu",
       "Rang" : "Qora",
       "Yil":2020,
       "Narh":40000}
data_json = json.dumps(data)
print(data)
talaba_json = """{"ism":"Hasan", "familiya": "Husanov", "tyil":2000}"""
print(talaba_json[0])



import json

data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
talaba_json = """{"ism": "Hasan", "familiya": "Husanov", "tyil": 2000}"""
talaba_dict = json.loads(talaba_json)

print(talaba_dict["ism"], talaba_dict["familiya"])

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
with open('talaba_json.json', 'w') as f:
    json.dump(talaba_json, f, indent=4)

with open('data.json', 'r') as f:
    data_read = json.load(f)
print(data_read)

with open('talaba_json.json', 'r') as f:
    talaba_read = json.load(f)
print(talaba_read["ism"], talaba_read["familiya"])


with open("students.json", "r", encoding="utf-8") as f:
    data = json.load(f)















import json

with open("python.json", "r", encoding="utf-8") as f:
    data = json.load(f)

page = list(data["query"]["pages"].values())[0]
print(page["title"])
print(page["extract"])