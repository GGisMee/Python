# 18__sets
utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("spoon")
utensils.clear()
utensils.update(dishes)
dinner_table = utensils.union(dishes)
for i in dinner_table:
   print(i)

print(utensils.difference(dishes)) # allt utom skillnaden alltså utan knife i detta fallet
print(utensils.intersection(dishes)) # bara skillnaden alltså med knife i detta fallet

for i in utensils:
    print(i) #annan orning än i utensils # kan bara ha ett av samma värde alltså inte två knife som nu utan 1 printa
