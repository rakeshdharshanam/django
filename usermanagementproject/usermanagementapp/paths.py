import os 
# from usermanagementproject import settings

file = os.path.abspath(os.getcwd())
folder = os.path.join(file,"files\\users.txt")
f = os.path.exists(folder)
# print(folder)
# print(f)
