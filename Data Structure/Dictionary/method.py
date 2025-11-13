dict_1 = {"name":"any","age":21,"city":"pune"}
print("given Dictionary:",dict_1)

#get
print(dict_1.get("name"))

#update
dict_2 = {"anand":19 ,"sarvesh":19}
dict_1.update(dict_2)
print("updated dictionary:",dict_1)

#copy
new_dic = dict_1.copy()
print("copy dictionary:",new_dic)

#pop
# age = new_dic.pop("age")
# print("delete dictionary item (age):",new_dic)

#popitem
# new_dic.popitem()
# print("delete last item dectionary:",new_dic)

#clear
# new_dic.clear()
# print("delete all item dectionary:",new_dic)

#keys
print("show dictionary key:",new_dic.keys())

#fromkeys
given_dict = ["one","two","three"]
dict.fromkeys(given_dict,"uniq")
print("all dict add uniq name:",given_dict)