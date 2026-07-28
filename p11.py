# (11) File Read and Write
with open("test.txt", "w") as f:
 f.write("Hello World this is python programme...")
with open("test.txt", "r") as f:
 content = f.read()
 print("File content:", content)