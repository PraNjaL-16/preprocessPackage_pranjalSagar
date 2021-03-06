from preprocess_pranjalSagar import utils

__version__ = '0.0.4'

# these methods can be accessed by user from outside
# as these methods name do not have starting underscroe
# methods will be called from 'utils.py'

def get_wordcounts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_avg_wordlength(x):	
	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):	
	return utils._get_stopwords_counts(x)

def get_hastag_counts(x):	
	return utils._get_hastag_counts(x)

def get_mention_counts(x):
	return utils._get_mention_counts(x)

def get_digit_counts(x):
	return utils._get_digit_counts(x)

def get_uppercases_counts(x):	
	return utils._get_uppercases_counts(x)	

def to_lower(x):	
	return utils._to_lower(x)	

def cont_exp(x):
	return utils._cont_exp(x)		

def get_emails(x):
	return utils._get_emails(x)	

def remove_emails(x):
	return utils._remove_emails(x)	

def get_urls(x):
	return utils._get_urls(x)

def remove_urls(x):	
	return utils._remove_urls(x)

def remve_rt(x):
	return utils._remve_rt(x)		

def remove_special_chars(x):
	return utils._remove_special_chars(x)	

def remove_html_tags(x):
	return utils._remove_html_tags(x)	

def remove_accented_chars(x):	
	return utils._remove_accented_chars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_base(x):
	return utils._make_base(x)	

def get_value_counts(df, col):
	return utils._get_value_counts(df, col)

def remove_common_words(x, freq, n=20):
	return utils._remove_common_words(x, freq, n)	

def remove_rarewords(x, freq, n=20):
	return utils._remove_rarewords(x, freq, n)	

def spelling_correctin(x):
	return utils._spelling_correctin(x)