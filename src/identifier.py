####################################
### Neccessary Import Statements ###
####################################
import pandas as pd
import numpy as np
import spacy

##############################################
### Write the Class That Identifies Errors ###
##############################################
class Error_Identifier:
	"""
	Class Purpose 
	-------------
	To identify and categorize errors in recognized entity from SpaCy model and output a
	Pandas DF of categorical data associated with error types.

	Attributes
	----------
	identified_errors_table - (DataFrame)
	error_example - (Dict)

	Features:
	art_url - (str)

	frag - (int) count of fragmentatation errors found for a given article
	sos_frag - (int) count of sos frag errors for a given article
	num_frag
	title_colon_frag - (int)
	title_prefix_frag - (int)

	concat - (int)
	sos_concat - (int)
	noun_ent_concat - (int)
	company_product_concat
	conj_adv_concat
	interior_ent_concat
	contractional_concat
	comma_list_concat
	comma_ent_concat
	sports_concat
	athlete_pos_concat
	team_score_rank_concat
	hyper_concat
	colon_concat
	diseases_concat

	disambig - (int) sum of all disambig errors
	noun_ent_ambig
	punct_ambig
	sports_nickname_ambig
	mixed_casing_ambig

	TP -
	FP -
	FN -
	TN -

	Methods
	-------

	is_Frag(ent Entity, List golden_annotation):
	returns Boolean

	is_Concat(ent Entity, List golden_annotation):
	returns Boolean

	is_Disamb(ent Entity, List golden_annotation):
	returns Boolean

	Init Parameters
	---------------

	References
	----------
	1.
	"""
	#
	def __init__(self, nlp, golden_annotation, article_text):
		"""
		"""
		self.doc = nlp(article_text)
		self.found_truth_map = golden_annotation
		self.index_of_ents = [ent.start for ent in self.doc.ents]
	# Kaelan
	def is_Frag(self):

		return
	# KN
	def is_sos_frag(self):
		return

	def is_num_frag(self):
		return

	def is_title_colon_frag(self):
		return

	def is_title_prefix_frag(self):
		return

	# Sebastian
	def concat(self):
		return
	# Ivy
	def noun_ent_concat(self):
		return

	#Sophia
	def company_product_concat(self):
		return

	#Sebastian
	def conj_adv_concat(self):
		return

	# Ivy
	def interior_ent_concat(self):
		return

	# Sophia
	def contractional_concat(self):
		return

	# Alexis
	def noun_ent_ambig(self):
		return

	def main(self):
		return

