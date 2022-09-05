import pickle

filename="load_image.txt"
file = open(filename,'rb')
new = pickle.load(file)
print(new)

