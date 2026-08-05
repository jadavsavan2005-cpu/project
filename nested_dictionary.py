student={
"name":"rahul kumar",

"subjects":{
"phy":97,
"chem":98,
"math":95
}

}

print(list(student.keys()))  #return all keys
print("\n")

print(list(student.values())) #returns all values
print("\n")
print("welcome")

print(list(student.items())) #returns all(key,val)pairs as tuples
print("\n")

print(student["name"]) #error
print("\n")

print(student.get("name2")) #no error->none #returns the key according to value
print("\n")


student.update({"city":"delhi"})#inserts the specified items to the dictionary
print("\n")

new_dict={"name":"neha kumar","age":16}
student.update(new_dict)
print(student)
