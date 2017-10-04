# All of this builds on -  Ding's "Creating Gated Cascades for Nested Conditionals Using DNA Strand Discplacement"
# Strings are assumed to be in ALL CAPS
from basic_gen import *


def generate_simple_if_gates(x,y):
	"""This program takes the X and Y nucleotide sequenes.
	It represents them according to their constituents ( [sub_seq1, sub_seq2] ).
	Then it uses these to produce the proper gates for the if statement.
	
	X and Y must be strings.
	# Strings are assumed to be in ALL CAPS
	"""

	# In the following code, I use a halved value of len(X) and len(Y).
	# Depending on the version of Python you're working with and what your intentions are
	# This may not be acceptable - You may floats or undesired rounding.
	## Thus, this solution is tentative.
	## ESPECIALLY IF WE USE AN ODD NUMBER OF NUCLEOTIDES FOR THE INPUT STRINGS

	# Going from the diagram on Ding (13)
	tmp_x = [ x[:len(x)/2], x[len(x)/2:] ]
	tmp_y = [ y[:len(y)/2], y[len(y)/2:] ]

	### a_comp_rvs, b_rvs = tmp_x[0],tmp_x[1]
	c_rvs, d_rvs = tmp_y[0],tmp_y[1]
	# comp - the compliment of the referred string.
	# rvs - the string is written with the 3' end at the 0-index.

	##### Compute First Gates - Interacts with Input

	#starting_complex_1_for_waste = [] - See Ding pg.13
	starting_complex_1_for_waste = [ reverse_string ( gen_compliment (  tmp_x[0] )) ]
	starting_complex_1_for_waste.append( reverse_string ( gen_compliment ( tmp_x[1] )))

	#starting_complex_1_for_initiator = [] - See Ding pg.13
	starting_complex_1_for_intermediary = [ tmp_x[1] ]
	starting_complex_1_for_intermediary.append( tmp_y[0] )

	print starting_complex_1_for_waste
	print starting_complex_1_for_intermediary

	##### Computes Non-trivial Second Gate - Interacts with Intermediary & Yields Output
	##### The second, last gate is really just y, so I will not write that here.
	starting_complex_2_for_waste = [ reverse_string ( gen_compliment ( tmp_x[1] ))]
	starting_complex_2_for_waste.append( reverse_string ( gen_compliment( tmp_y[0] )))

	print starting_complex_2_for_waste

# Quick test
# Mind the parity
x = 'ATCCTG'
y = 'GCATCC'

generate_simple_if_gates(x,y)