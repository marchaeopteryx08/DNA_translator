#!/usr/bin/env python3

import streamlit as st 

# Reading the CSS file
with open("styling.css") as f:
	styling = f.read()
	
# Connecting the CSS file to the Streamlit app
st.markdown(f"<style>{styling}</style>", unsafe_allow_html=True)


codon_dict = {
	'UUU': 'Phe ',  'UUC': 'Phe ',  'UUA': 'Leu ' ,  'UUG': 'Leu ',  #Phe: Phenylalanine, #Leu: Leucine
	'UCU': 'Ser ',  'UCC': 'Ser ',  'UCA': 'Ser ', 'UCG': 'Ser ',  #Ser: Serine',
	'UAU': 'Tyr ',  'UAC': 'Tyr ',  'UAA': 'STOP ',    'UAG': 'STOP ',    #Tyr: Tyrosine,     #STOP codon
	'UGU': 'Cys ',  'UGC': 'Cys ',  'UGA': 'STOP ',    'UGG': 'Trp ',  #Cys: Cystine,      #STOP codon,   #Trp: Tryptophan
	'CUU': 'Leu ',  'CUC': 'Leu ',  'CUA': 'Leu ',  'CUG': 'Leu ',  #Leu: Leucine
	'CCU': 'Pro ',  'CCC': 'Pro ',  'CCA': 'Pro ',  'CCG': 'Pro ',  #Pro: Proline
	'CAU': 'His ',  'CAC': 'His ',  'CAA': 'Gln ',  'CAG': 'Gln ',  #His: Histidine,   #Gln: Glutamine
	'CGU': 'Arg ',  'CGC': 'Arg ',  'CGA': 'Arg ',  'CGG': 'Arg ',  #Arg: Arginine
	'AUU': 'Ile ',  'AUC': 'Ile ',  'AUA': 'Ile ',  'AUG': 'Met ',  #Ile: Isoleucine,  #Met: Methionine (START CODON)
	'ACU': 'Thr ',  'ACC': 'Thr ',  'ACA': 'Thr ',  'ACG': 'Thr ',  #Thr: Threonine
	'AAU': 'Asn ',  'AAC': 'Asn ',  'AAA': 'Lys ',  'AAG': 'Lys ',  #Asn: Asparigine,  #Lys: Lysine
	'AGU': 'Ser ',  'AGC': 'Ser ',  'AGA': 'Arg ',  'AGG': 'Arg ',  #Ser: Serine,      #Arg: Arginine
	'GUU': 'Val ',  'GUC': 'Val ',  'GUA': 'Val ',  'GUG': 'Val ',  #Val: Valine, 
	'GCU': 'Ala ',  'GCC': 'Ala ',  'GCA': 'Ala ',  'GCG': 'Ala ',  #Ala: Alanine
	'GAU': 'Asp ',  'GAC': 'Asp ',  'GAA': 'Glu ',  'GAG': 'Glu ',  #Asp: Aspartic acid,   #Glu: Glutamic acid
	'GGU': 'Gly ',  'GGC': 'Gly ',  'GGA': 'Gly ',  'GGG': 'Gly ', 
	
}	


if 'step' not in st.session_state:
	st.session_state.step = 1
	
def next_step():
	st.session_state.step += 1

# Main
st.title('DNA translator')

# Display the messages and indicate which number they are
if st.session_state.step == 1:
	st.write("Welcome to the DNA to RNA and Amino Acid Online converter. Here, you can input any DNA sequence of your choice and have it translated to an amino acid chain, representing the real biological process. Are you a starter in molecular biology, or are you a high school student studying genetics? Then this will help.")
	if st.button('Next', on_click=next_step):
		pass  # The button click will add onto the step 
		
elif st.session_state.step == 2:
	st.write("In molecular biology, the processes of transcription and translation are some of the most important aspects of this field. These processes ultimately lead to producing amino acid chains, the essential building blocks of proteins. Without any of these, the human body would not be able to live healthily and cellular functions would cease.")
	if st.button('Next', on_click=next_step):
		pass 
		
elif st.session_state.step == 3:
	st.write("Before we proceed, a few introductions will to be given in case you are not familiar with this process. In molecular biology, we have five primary nucleotides: A (Adenine), T (Thymine), G (Guanine), C (Cytosine) and U (Uracil), the latter being exclusive to RNA sequences. Each nucleotide binds with one another - in DNA sequences, adenine is paired with thymine, and guanine is paired with cytosine. This is the same for RNA sequences, but adenine now pairs with uracil.")
	if st.button('Next', on_click=next_step):
		pass 
		
elif st.session_state.step == 4:
	st.write(" ★ Transcription and translation are both carried out in multiple environments of the cell. Transcription (DNA --> mRNA) occurs within a cell's nucleus, and the newly copied mRNA sequence exits the nucleus via nuclear pores, leading us to our second process: translation (mRNA --> proteins).")
	if st.button('Next', on_click=next_step):
		pass  
		
elif st.session_state.step == 5:
	st.write(" ★ Translation occurs within ribosomes that are scattered throughout the cytoplasm, a liquid composed of water, multiple salts and other components. To allow protein synthesis (remember the pairs: A with U, G with C), mRNA interacts with other molecular structures such as tRNA (transfer RNA), but this will not be important in our code.")
	if st.button('Next', on_click=next_step):
		pass 			
	
elif st.session_state.step == 6:
	st.write("With these notes set, you may proceed.")
	if st.button('Start', on_click=next_step):
		pass  	
			
		
elif st.session_state.step >= 7:
	
	def transcribe_and_translate(dna_seq):
		# Replacing and corresponding nucleotides
		rna_seq = dna_seq.replace('A', 'U').replace('T', 'A').replace('C', 'X').replace('G', 'C').replace('X', 'G')
		
		# Translating an RNA sequence to amino acids
		amino_acids = ""
		for i in range(0, len(rna_seq), 3):
			codon = rna_seq[i:i+3]
			if len(codon) == 3:
				amino_acids += codon_dict.get(codon, "") 
				
		return dna_seq, rna_seq, amino_acids
		
	def main():
		st.title("DNA -> RNA and Amino Acid converter")
		
		# Message that asks the user to input a DNA sequence
		dna_seq = st.text_input("Submit a DNA sequence. Your sequence should consist of the nucleotides A, C, G, and T. It can be of any length. When done, press enter!").upper()
		
		# Checking whether the DNA sequence contains all nucleotides or not
		if not all(nucleotide in ['A', 'T', 'C', 'G'] for nucleotide in dna_seq):
			st.write("You have submitted an invalid DNA sequence. Please input a sequence containing only A, T, C, and G.")
		else:
			#Transcribe and translate function, with lines for each result given
			try:
				dna, rna, amino_acid_chain = transcribe_and_translate(dna_seq)
				st.write(f"\nDNA sequence entered:\n{dna}")
				st.write(f"\nRNA sequence:\n{rna}")
				st.write(f"\nAmino acid chain:\n{amino_acid_chain}")
			#KeyError message appears if the user did not input a valid sequence.
			except KeyError:
				st.write("There was an error in processing your sequence. Please check the input and try again.")
				
	if __name__ == "__main__":
		main()
		
	