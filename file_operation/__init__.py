# file = open("NewFile.txt","w")
#
# txt = "This is our first txt in file "
# file.write(txt)
# file.close()
#
# file = open("NewFile.txt","r")
# print(file.readlines())
# file.close()
#
# file = open("NewFile.txt","a")
# txt = """
# A wiki is run using wiki software,
# otherwise known as a wiki engine.
#  A wiki engine is a type of content management system,
#  but it differs from most other such systems,
#  including blog software, in that the content
#  is created without any defined owner or leader,
#  and wikis have little inherent structure, """
#
# file.write(txt)
# file.close()
#
# import os
# # os.rename("FileNew.docx","NewFile.txt")
# os.remove("NewFile.txt")

# import os
# newfile = open("newfilecreate.txt","w+")
# for i in range (1,10):
#     newfile.write("\n Hello, welcome to python:")
# for i in range(1,10):
#     print(newfile.read())
#         newfile.seek(0)
#     print(newfile.tell())
# newfile.close()

#sequence operation
# list = ["Marketing","Content Designing","Sales"]
# print(list)
#
# print(list+["Python","Hadoop"])
# print(list*2)
#
# print('Marketing' in list)
# print(list[2])
#
# print(list[0:2])

#list indexing and slicing
# list = ["Hadoop", "Python", "Android"]
# print(list[1])
#
# # print(list[0:2])
#
# print(list[-1])

#list_remove_and_pop_up_functions

# list=[1,2,3,4,5,'a','b','c']
# print(list.pop(3))
#
# list.remove('a')
# print(list)

#list_type

# list3=[1,2,5,'Python','Hadoop']
# print(type(list3))
#
# print([x**2 for x in [1,2,3,4,5]])

#list_built_in_functions

# list=[1,2,3]
# list.append("Machine Learning")
# print(list)
#
# list.extend(['g','h'])
# print(list)
#
# list.insert(1, 'Scripting')
# print(list)
#
# list.remove(3)
# print(list)












