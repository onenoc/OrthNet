from distutils.core import setup, Extension

ext = Extension('orthnet.utils.enum_dim',
	sources = ['orthnet/utils/enum_dim.i'],
	language = 'c++',
	swig_opts = ['-c++'],
	)

setup(
	name = 'orthnet',
	version = '0.1',
	keywords = ['orthogonal polynomial', 'tensorflow', 'pytorch'],
	description = 'TensorFlow and PyTorch layers for generating orthogonal polynomials',
	license = 'MIT',
	author = 'Chuan Lu',
	author_email = 'chuan-lu@uiowa.edu',
	ext_modules = [ext],
	packages = ['orthnet', 'orthnet.tensorflow', 'orthnet.pytorch', 'orthnet.utils'],
	)