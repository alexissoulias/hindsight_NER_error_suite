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
	def __init__(self, nlp, golden_annotation, article_text):
		"""
		"""
		self.doc = nlp(article_text)
		self.golden_annotation = golden_annotation

	def is_Frag(ent):
		for gold_entity in self.golden_annotation:
			if ent.text in gold_entity:
				if len(ent.text) < len(gold_entity):
					return (True, gold_entity)
		return (False, None)

	def sos_frag(index,  gold_entity):
		return

	def main(self):
		ent_text = []
		for ent in doc.ents:
			ent_text.append(ent.text)
		ent_indexes = [token.i for token in doc if token.text in ent_text]
