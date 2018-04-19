import tensorflow as tf
import torch
import numpy as np
from .poly import Poly

class Jacobi(Poly):
	"""
	Jacobi Polynomials
	"""
	def __init__(self, module, degree, x, alpha, beta, *args, **kw):
		"""
		input:
			module: ['tensorflow', 'torch', 'numpy']
			degree: highest degree of polynomial
			x: a tensor of shape [Nsample*Nparameter], each row is a sample point, each column represents a parameter
			alpha, beta: the parameters of Jacobi polynomials
		"""
		if module == 'tensorflow':
			initial = [lambda x: tf.ones_like(x), lambda x: 0.5*(alpha+beta+2)*x+0.5*(alpha-beta)]
			recurrence = lambda p1, p2, n, x: ((2*n+alpha+beta-1)*tf.multiply((2*n+alpha+beta)*(2*n+alpha+beta-2)*x+alpha**2-beta**2, p1) - 2*(n+alpha-1)*(n+beta-1)*(2*n+alpha+beta)*p2)/(2*n*(n+alpha+beta)*(2*n+alpha+beta-2))
		elif module == 'torch':
			initial = [lambda x: torch.ones_like(x), lambda x: x*0.5*(alpha+beta+2)+0.5*(alpha-beta)]
			recurrence = lambda p1, p2, n, x: ((x*(2*n+alpha+beta)*(2*n+alpha+beta-2)+alpha**2-beta**2)*p1*(2*n+alpha+beta-1) - p2*(n+alpha-1)*(n+beta-1)*(2*n+alpha+beta))*2/(2*n*(n+alpha+beta)*(2*n+alpha+beta-2))
		elif module == 'numpy':
			initial = [lambda x: np.ones_like(x), lambda x: 0.5*(alpha+beta+2)*x+0.5*(alpha-beta)]
			recurrence = lambda p1, p2, n, x: ((2*n+alpha+beta-1)*((2*n+alpha+beta)*(2*n+alpha+beta-2)*x+alpha**2-beta**2)*p1 - 2*(n+alpha-1)*(n+beta-1)*(2*n+alpha+beta)*p2)/(2*n*(n+alpha+beta)*(2*n+alpha+beta-2))			
		Poly.__init__(self, module, degree, x, initial, recurrence, *args, **kw)

