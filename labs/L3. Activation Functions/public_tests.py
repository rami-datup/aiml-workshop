import numpy as np
import tensorflow as tf


def test_my_softmax(target):
    """Unit test for the my_softmax exercise.

    Compares the learner's implementation against tf.nn.softmax on a small
    vector and checks that the result is a valid probability distribution.
    """
    z = np.array([1., 2., 3., 4.])
    a = np.asarray(target(z), dtype=float)
    atf = np.asarray(tf.nn.softmax(z), dtype=float)

    assert a.shape == atf.shape, \
        f"Wrong shape. Expected {atf.shape}, got {a.shape}."
    assert np.allclose(a, atf, atol=1e-6), \
        f"Wrong values. Expected {atf}, got {a}."
    assert np.isclose(np.sum(a), 1.0, atol=1e-6), \
        "The softmax output should sum to one."
    assert np.all(a >= 0), \
        "All softmax outputs should be non-negative."

    print("\033[92m All tests passed.")
