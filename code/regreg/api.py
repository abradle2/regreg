"""
A collection of commonly used RegReg functions and objects
"""

from atoms import (l1norm, l2norm, supnorm, 
                   positive_part, constrained_max, affine_atom as linear_atom,
                   constrained_positive_part, max_positive_part)
from cones import (nonnegative, nonpositive, nonnegative_definite, nonpositive_definite,
                   zero, zero_constraint, affine_cone as linear_cone)

from linear_constraints import (projection, projection_complement)

from affine import (identity, selector, affine_transform, normalize, linear_transform, composition as affine_composition, affine_sum, affine_reshape)
from smooth import (quadratic, linear, logistic_loglikelihood, poisson_loglikelihood, multinomial_loglikelihood, smooth_atom, affine_smooth, signal_approximator, trace, logdet)

from factored_matrix import (factored_matrix, compute_iterative_svd, soft_threshold_svd)

from separable import separable
from container import container
from algorithms import FISTA
from admm import admm_problem
from blocks import blockwise

from conjugate import conjugate
from composite import (composite, nonsmooth as nonsmooth_composite,
                       smooth as smooth_composite, smoothed as smoothed_atom)
