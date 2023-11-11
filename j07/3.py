thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["brand"] = "bmw"
print(thisdict.keys())
print(thisdict.values())
dict2 = dict(thisdict)
print(thisdict)
print(dict2)