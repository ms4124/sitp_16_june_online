# # print("helllooooooooo")
# # num=3
# # print(num)

# # name ="mohit"
# # print(name)
# # print(type(name))
# # print(type(num))
# # print(type(3.14))
# # a=input("naam likh")
# # print(a)

# name ="mohit"
# print(name)
# print(type(name))
# print(len(name))
# print(name[0:3])

#DAY 3#


# name="mohit soni"
# print(name)
# name.upper
# print(name.upper())
# print(name.title())
# print(name.lower())
# print(name.capitalize())
# name.swapcase()
# print(name.swapcase()) #cuurent case ko upper-lower,lower-upper karta he
# name.count("o,i")
# print(name.count("o"))
# print(name.count("i"))
# print("my name is ",name)
# print("my name is "+name)
# first="mohit"
# last="soni"
# print(f"my name is {first} and my last name is {last}")
# print("my name is {} and my last name is {}".format(first,last))
# print("my name is "+first+" "+last)
# print("my name is {} {} ".format(first,last))
# print(first + " " + last)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LIST<<<<<<<<<<<<<<<<<<<<<<<<<<<#

# lst=[1,2,3,4,5,6,6,6,6,"mohit",6.23]
# len(lst)
# print(len(lst))
# print(type(lst))
# #INDEXING
# print(lst[0])
# print(lst[4])

# #SLICING

# lst[0:5]
# print(lst[0:5])
# print(lst[0:5:2]) #0 se 5 tak 2 se 2

# lst.append(500)
# print(lst)
#lst.pop()
#print(lst)

# lst.pop(3)
# print(lst)
# lst.insert(2,222)
# print(lst)
# lst.remove(6)

# lst.clear()
# print(lst)

# lst.reverse()
# print(lst)
# lst.count(2)
# print(lst.count(6))
# lst.sort()

#<<<<<<<<<<<<<<<<<TUPLE>>>>>>>>>>>>>>>>#

# tpl=(1,2,3,4,5,6,"mohit",3.1234)

# print(tpl)
# print(type(tpl))
# print(len(tpl))

# #INDEXING

# print(tpl[0])
# print(tpl[4])
# #SLICING
# print(tpl[0:5]) 
# print(tpl[0:5:2])
# print(tpl[::-1])


# print(2 in tpl)
# print(2 not in tpl)

# tpl1=(1,2,3,5,3,33,4,5,)
# print(max(tpl1))
# print(min(tpl1))
# print(sum(tpl1))
# print(len(tpl1))

#TYPECASTING

# a=int(input("enter ur nuber"))
# b=int(input("enter ur nuber"))2

# print(type(a))
# print(type(b))
# print(a)
# print(b)

#Tuple Unpacking#
# abc=1,2,3
# a,b,c=abc
# print(a)
# print(b)
# print(c)  #<<<<<<<

# tpl1=(1,2,3,4,5,7)
# tpl2=(6,7,8,9,10,11)
# print(tpl1+tpl2)
# print(tpl1*3)

#TASK2 -----> access 7,8 from the list
# tpl=(1,2,3,4,[1,2,3,4,7,8])
# print(tpl)
# print(tpl[4])
# tpl[4].append(5)
# print(tpl)  #<<<<<<<


#<<<<<<<<<<<<<<<<<<DICTIONARRY>>>>>>>>>>>>>>#

# dct ={"name":"sachin","age":25,"city":"mumbai"}
# print(dct)
# print(dct["name"])
# print(dct["age"])
# print(type(dct))
# print(len(dct))
# print(dct.keys())
# print(dct.values())
# print(dct.items())
# print(dct.get("name"))
# print(dct.get("age"))

# dct['address']="jaipur"
# print(dct)

#TASK3-----> dictionary ki value ko update kese kare

# dct["age"]=50
# print(dct)

#variablenae.update(indext:value)

# del dct["age"]
# print(dct)

# print(dct.keys())
# print(dct.values())
# dct.pop("age")

# print("name"in dct) #ANSWER IN TRUE FALSE
# print("age"in dct) #ANSWER IN TRUE FALSE

# dct1={}
# print(dct1)
# print(type(dct1))
# print(len(dct1)) #ANSWER IN 0

#<<<<<<<<<<<<<SET>>>>>>>>>>>>#

# sat={1,2,3,4,5,6,6454,65,23,23}
# print(sat)
# print(type(sat))
# sat.add(100)
# print(sat)
# # sat.remove(1)
# # print(sat)
# sat.discard(100)
# sat.discard(3)
# sat.clear()


# mylist=[1,2,3,4,5,6,7]
# print(mylist)
# print(type(mylist))
# myset=set(mylist) #we did typecasting here
# print(myset)
# print(type(myset))


#<<<<<<<<<<<operators perform karo>>>>>>>>>>>#

