from example import assert_true

import pytest


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or above")
def test_assert_true():

    assert assert_true()
