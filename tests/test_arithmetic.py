import os
import random
import tempfile

import pytest

from arithmetic import Arithmetic


def test_generate_table_deterministic():
    random.seed(0)
    ar = Arithmetic()
    table = ar.generate_table(5, 10, options=["add", "subtract", "multiply"])
    # deterministic length and format checks
    assert len(table) == 5
    for row in table:
        assert isinstance(row, str)
        assert any(op in row for op in ["+", "-", "*"])


def test_generate_pdf_smoke(tmp_path):
    random.seed(1)
    ar = Arithmetic()
    table = ar.generate_table(10, 5, options=["add"])
    out = tmp_path / "out.pdf"
    ar.generate_pdf(table, filename=str(out), columns=2)
    assert out.exists() and out.stat().st_size > 0
