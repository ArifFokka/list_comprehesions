"""
x= [i for i in range(5)]
print(x, type(x))


x=['1','2', '3', '89']
print(x)
y=[int(i) for  i in x]
print(y)

myStrings = 'hi airf there are'
myStrings = [s.strip() for s in myStrings]
print(myStrings)

vec = [[1,2,3], [4,5,6], [7,8,9]]
tek =[num for elem in vec for num in elem]
print(tek)

# Dictionary comprehesions
print({i: str(i) for i in range(5)})

my_dict = {1:"dog", 2:"cat", 3:"hamster"}
print( {value:key for key, value in my_dict.items()})
print( {key:value for key, value in my_dict.items()})
print( {key for key in my_dict.keys()})
print( {key for key in my_dict.values()})
{'hamster': 3, 'dog': 1, 'cat': 2}
"""
#How to Handle Exceptions
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("you cannot divide by zero ")
#
# try:
#     d = {1: 1, 2: 2, 3: 3}
#     print(d[10])
# except KeyError:
#     print('that key dos not exit')
#
# my_list = [1, 2, 3, 4, 5]
# try:
#     print(my_list[lkasj])
# except IndexError:
#     print('That index is not in the list!')
# except:
#     print('some others error')
#
#
# my_dict = [1, 2, 3, 4, 5]
# try:
#     value = my_dict["-d"]
# except (IndexError, KeyError, TypeError,SyntaxError):
#     print("An IndexError or KeyError occurred! or TypeError")
# finally:
#     print("don't know")
#
# my_dict = [1, 2, 3, 4, 5]
# try:
#     value = my_dict["-d"]
# except SyntaxError:
#     print('Invalid SyntexEror')
# except (IndexError, KeyError, TypeError,SyntaxError):
#     print("An IndexError or KeyError occurred! or TypeError")
# else:
#     print("don't know")

#
# my_dict = {"a":1, "b":2, "c":3}
# try:
#     value = my_dict["a"]
# except KeyError:
#     print("A KeyError occurred!")
# else:
#     print("No error occurred!")
# finally:
#     print("The finally statement ran!")
#

#Problems Solving -- Exercise: let consider a list ( mylist = [1,23,45,’hello’, ‘43’, -23, ‘-56’,’one’, 5.6] )
# a) ake another list (anotherList) which contain the int values of mylist ( user try except here )

mylist = [1, 23, 45, 'hello', '43', -23, '-56', 'one', 5.6]

anotherList=[]
for i in mylist:
    try:
        anotherList.append(int(i))

    except:
        continue
print(anotherList)

#B) anotherList = [ 1, 23, 45, 43,-23,-56]
print(sorted(anotherList))
anotherList.sort(reverse=True)
print(anotherList)

mylist = [1, 23, 45, 'hello', '43', -23, '-56', 'one', 5.6]
# C) Print the values of anotherList using List Comprehensions
print([i for i in mylist])
mylist = [1, 23, 45, 'hello', '43', -23, '-56', 'one', 5.6]
anotherList=[]
[anotherList.append(a) for a in mylist if type(a) == int]
print(anotherList)


