import sys
from pathlib import Path

# Add project root to PYTHONPATH
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app import add, sub

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2
