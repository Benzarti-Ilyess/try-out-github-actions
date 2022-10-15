import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or above")
def test_assert_true():
  
  assert 1 == 1
