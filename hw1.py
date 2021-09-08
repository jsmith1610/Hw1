import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
f = open(input_file, "rt")
print("Files are open")
w = open(output_file, "wt")
for line in f:
    for word in line.split():
        w.writelines(word + '\n')
w.close()
f.close()
print("Files are closed")
