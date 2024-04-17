import numpy as np
from numpy_list import list_op
from numpy.testing import assert_array_equal, assert_

def test_arit_progress():
    assert_array_equal(list_op.arit_progress(1, 2, 2, 3),
                       np.matrix([[1, 3, 5],
                                  [7, 9, 11]]))

def test_geom_progress():
    assert_array_equal(list_op.geom_progress(1,2,2,3),
                       np.matrix([[1,2,4],
                                 [8,  16,  32]]))



