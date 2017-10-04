# All of this builds on -  Ding's "Creating Gated Cascades for Nested Conditionals Using DNA Strand Discplacement"
# Strings are assumed to be in ALL CAPS
from basic_gen import *

"""This code assumes the user is 'given' the Input 1 & Input 2 strands.
It also relies on the user submitting the text of the desired outputs.
In this case, the 'outputs' are Initiator 1 and Initiator 2"""


def generate_nested_conditional_gates(input1,input2,init1,init2):


	tmp_input1 = [ input1[:len(input1)/2], input1[len(input1)/2:] ] #c'a >
	tmp_input2 = [ input2[:len(input2)/2], input2[len(input2)/2:] ] #m'a >
	a = tmp_input1[1] #a>
	c = gen_compliment ( tmp_input1[0] ) #c>
	m = gen_compliment ( tmp_input2[0] ) #m>

	#y
	#d

	#x
	#g

	### The following values SHOULD be randomly generated according to necessary preset AND user-defined parameters.
	b = "ACTGAACCTTGG" #"Random" String of 12 ( How long should it be??? ) Nucleotides #b>
	e = 'AACCT'  #In practice, e should be randomly generated, but * ~5 nucleotides long * ( Ding 15 ) #e>
	w = 'GGTCAACTTAGC' #"Random" String of 14 (How long should it be??? Any other restrictions? ) #w>
	z = 'CCGGATGTTTCC' #"Random", but length matches w (I think it must, but double check. ) #z>


	### Let's Begin Generation.
	### Since Input1, Input2, Initiator1, and Initiator2 are known.
	### We need only generate the intermediary complexes

	print tmp_input1
	print tmp_input2



# Quick test
# Mind the parity
# Mind the equal lengths
input1 = 'ATCCTG'+ 'AAGCCA'
input2 = 'GCATCC'+ 'CCACGG'
init1 = 'AAACTTACC' + 'AGAGCTGG'
init2 = 'GGCCAATAC' + 'CAGACCGA'
generate_nested_conditional_gates(input1,input2,init1,init2)