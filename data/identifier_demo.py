
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc
import csv

# loads a SpaCy model and creates a doc for example_article
nlp = spacy.load('en_core_web_md')
file  = open("example_article.txt")
article_string = file.read()
file.close()
article_doc = nlp(article_string)

# Constructs a list of ground truth entities from a preconstructed csv file that contains the articles annotation
annotated_data = []
with open('annotated_entities.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		annotated_data.append(row[0])


# Seperates all ground truth entities into seperate tokens so that they can be incorporated into a doc object
words = []
spaces = []
ent_position = []
i = 0
j = 0

for ann in annotated_data:
	split_commas = ann.replace(',', ' , ')
	split_colon = split_commas.replace(':', ' : ')
	split_apostophe = split_colon.replace("'", " ' ")
	split_dash = split_apostophe.replace('-', ' - ')
	split_period = split_dash.replace('.', ' . ')
	tokens = split_period.split()
	j += len(tokens)
	ent_position.append([i, j])
	i = j
	tokens_iter = iter(tokens)
	token = next(tokens_iter)
	call_next = True
	while True:
		words.append(token)
		try:
			if call_next:
				next_token = next(tokens_iter)
			call_next = True 
			if next_token not in [',', "'", ':', '.', '-'] and token not in  ["'", '-']:
				try:
					next_next_token = next(tokens_iter)
					if next_next_token == '.' and token == '.':
						spaces.append(False)
					else:
						spaces.append(True)
					token = next_token
					next_token = next_next_token
					call_next = False
				except StopIteration:
					spaces.append(True)
					token = next_token
			else:
				spaces.append(False)
				token = next_token
		except StopIteration:
			spaces.append(False)
			break

#Constructs a doc for the list of ground truth entities
annotated_data_doc = Doc(nlp.vocab, words = words, spaces = spaces)

#Constructs a span for each ground truth entity 
spans = []
for start, end in ent_position:
	spans.append(annotated_data_doc[start:end])

#Defining Error type functions

def is_frag(ent, possible_ground_truth, article_doc, spans):
	for ann_ent in possible_ground_truth:
		if ent.text in ann_ent.text and len(ent.text) < len(ann_ent.text):
			if article_doc[ent.start - 1].text in ann_ent.text or article_doc[ent.start + 1].text in ann_ent.text:
				spans.remove(ann_ent)
				return (True, ann_ent.text.replace(ent.text, '', 1))
	return (False, None)

def is_concat(ent, possible_ground_truth, article_doc, spans):
		for ann_ent in possible_ground_truth:
			if ann_ent.text in ent.text and len(ent.text) > len(ann_ent.text):
				spans.remove(ann_ent)
				return (True, ent.text.replace(ann_ent.text, '', 1))
		return (False, None)

#Constructs a dictionary with a key for each found entity and a list of all similar ground truth entities
similar_ent_ann = {}

correct_entitites = 0
num_frag = 0
num_concat = 0
spurious = 0

for ent in article_doc.ents:
	span_is_first = True
	similar_ent_ann[ent] = []
	for span in spans:
		if ent.text == span.text and span_is_first:
			spans.remove(span)
			similar_ent_ann.pop(ent)
			correct_entitites += 1
			break
		elif ent.similarity(span) > 0.65:
			span_is_first = False
			similar_ent_ann[ent].append(span)
		frag = is_frag(ent, similar_ent_ann[ent], article_doc, spans)
		if frag[0]:
			print('fragment error: {}'.format(ent))
			print('Portion missing: {}'.format(frag[1]))
			print('\n')
			num_frag += 1
			similar_ent_ann.pop(ent)
			break
		concat = is_concat(ent, similar_ent_ann[ent], article_doc, spans)
		if concat[0]:
			print('concat error: {}'.format(ent))
			print('Portion added: {}'.format(concat[1]))
			print('\n')
			num_concat += 1
			similar_ent_ann.pop(ent)
			break

for ent in similar_ent_ann.keys():
	if not similar_ent_ann[ent]:
		spurious += 1
	else:
		for ann in similar_ent_ann[ent]:
			if ent.text == ann.text:
				spans.remove(ann)
				correct_entitites += 1

print('Total Fragmented = {}'.format(num_frag))
print('Total Concatenated = {}'.format(num_concat))
print('Total Correct/TP = {}'.format(correct_entitites))
print('Total Spurious/FP = {}'.format(spurious))
print('Total Missing/FN = {}'.format(len(spans)))


