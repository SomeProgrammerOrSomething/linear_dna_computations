# This will use a Deep-First Search algorithm
# To generate/find usable strands of length n

nucleotides = {'A':('T','pur'),	'C':('G','pyr'),	'G':('C','pur'),	'T':('A','pyr')}
base_groups = {'pur':['A','G'], 'pyr':['C','T']}
word_bank = []
old_nmer = []

quadraplex_count = 4 # This is for book-keeping to correct against uncertainty and mistakes.
# quadraplex_count = raw_input("How long can a string of G's be until it is unacceptable - produces a complex: ")
# (Seeman 2015, pg 18) and ( Lam, Beraldi, Tannahill, and Balasubramanian 2013 )
non_usable_word_bank = ['G'*quadraplex_count]

def error_check(strand):
	if is_palindrome(strand):
		return True
	elif self_compliment(strand):
		return True
	elif strictly_wrong(strand):
		return True
	elif uses_old_nmer(strand):
		return True
	else:
		return False

def reverse_string(strand):
	return strand[::-1]

def is_palindrome(strand):
	if len(strand) > 1:
		##print "Debug: Pal_True"
		return ( strand == strand[::-1] )
	else:
		##print "Debug: Pal_False"
		return False

def gen_compliment(strand):
	compliment = ''
	index = 0
	for index in range(len(strand)):
		compliment += nucleotides[strand[index]][0]
	return compliment

def self_compliment(strand):
	half = len(strand)//2 #For Py2 and Py3 this yields the integral, math_floor
	if len(strand)%2 == 0:
		#Even Case:
		#	First half in comparisson to 2nd half
		#	X1 X2 || X3 X4
		##print "Debug: Compliment-Even: "
		print strand[:half] == gen_compliment( strand[half:] )

		return strand[:half] == gen_compliment( strand[half:] )
	else:
		#Odd Case:
		#	First partial chunk in chunk in comparisson to 2nd partial chunk
		#	X1 X2 |(X3)| X4 X5
		##print "Debug: Compliment-Odd: "
		print strand[:half] == gen_compliment( strand[half+1:] )

		return strand[:half] == gen_compliment( strand[half+1:])

def strictly_wrong(strand):
	return strand in non_usable_word_bank

def uses_old_nmer(n_mer):
	return n_mer in old_nmer