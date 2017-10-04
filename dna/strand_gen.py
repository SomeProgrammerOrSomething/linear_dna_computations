from basic_gen import *
import random

# PreAllocations/Setup
nucleo_list = ['A','C','G','T']

def generate(max,mode):
	gen_string = ''
	counter = 0

	while True:
		if mode == '1':
			#print "You have chosen Deterministic"
			gen_string += nucleo_list[counter]
		else:
			#print "You have chosen Non-Deterministic"
			gen_string += nucleo_list[ random.randint(0,3) ]

		if error_check(gen_string) and ( len(gen_string) > 1 ):
			counter += 1
			gen_string = gen_string[:-1]
			##print "DEBUG - Error L1 ", gen_string

			if counter >= 4:
				gen_string = gen_string[:-1]
				counter = 0
		else:
			counter = 0
		##print "DEBUG - Post ", gen_string

		if ( len(gen_string) >= max_length ):
			print gen_string
			return
		else:
			continue

max_length = int ( raw_input( "Enter the desired length of the strand - as an integer: ") )

mode_selection = raw_input('How should strands be generated: \
							 \n 1) Deterministically \
							 \n 2) Non-Deterministcally \
							 \n\t')

strand = generate(max_length,mode_selection)