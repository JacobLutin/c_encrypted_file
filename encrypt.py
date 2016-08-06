import os
import random

def flip_byte(in_bytes):
	i = random.randint(0, len(in_bytes))
	c = chr(random.randint(0, 0xFF))
	return in_bytes[:i]+c+in_bytes[i+1:]

def copy_binary():
	with open("license_2", "rb") as orig_f, open("license_2_new", "wb") as new_f:
		new_f.write(flip_byte(orig_f.read()))

def compare(fn1, fn2):
	with open(fn1) as f1, open(fn2) as f2:
		return f1.read() == f2.read()

def check_output():
	#os.system("./license_2 AAAA-228-1488-KEY > orig_output")
	os.system("(./license_2_new ; ./license_2_new AAAA-228-1488-KEY) > new_output")
	return compare("orig_output", "new_output") 

def check_gdb():
	#os.system("echo disassemble main | gdb license_2 > orig_gdb")
	os.system("echo disassemble main | gdb license_2_new > new_gdb")
	return compare("orig_gdb", "new_gdb")

os.system("cp license_2 license_2_new")

while True:
	#os.system("rm -rf license_2_new new_gdb new_output")
	#os.system("ls")
	copy_binary()
	if check_output() and not check_gdb():
		print("FOUND POSSIBLE FAIL\n\n\n")
		os.system("tail new_gdb")
		raw_input()
