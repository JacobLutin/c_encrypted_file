import sys
import random

def check_sum(key):
	char_sum = 0
	for c in key:
		char_sum += ord(c)
	sys.stdout.write("{0:3} | {1}       \r".format(char_sum, key))
	sys.stdout.flush()
	return char_sum


def generate(key_sum):

	key = 'A'
	char_sum = ord(key)

	while char_sum < key_sum:
		
		if key_sum - char_sum <= 90:
			char = chr(key_sum - char_sum)
		else:
			char = 'A'

		key += char
		char_sum += ord(char)
	print(key, char_sum)
	return key, char_sum


def generate_random_keys(key_sum):
	key = ""
	while True:
		key += random.choice("abcdefhijklmnoprstuvwxyzABCDEFHIJKLMNOPRSTUVWXYZ-_")
		sum = check_sum(key)
		if sum > key_sum:
			key = ""
		elif sum == key_sum:
			print("Found valid key: {}".format(key))
	
		
generate_random_keys(997)		
