import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()


setuptools.setup(
	# name of python package (should be unique)
	name = 'preprocess_pranjalSagar',
	# can be anything
	version = '0.0.4',
	author = 'Pranjal Sagar',
	author_email = 'pranjalsagar2001@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'],
	python_requires = '>=3.5'
	)