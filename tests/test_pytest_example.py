import pytest

import sys

from src.example import assert_true


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or above")
def test_assert_true():

    assert assert_true()
