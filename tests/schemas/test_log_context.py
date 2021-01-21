import pytest

from spp_contract_testing.schemas import validate_log_level


@pytest.mark.parametrize("log_level", [20, "INFO", "WARNING", 50])
def test_validate_log_level(log_level):
    assert validate_log_level(log_level)


@pytest.mark.parametrize("log_level", [200, "MADE UP", "DOES NOT EXIST", -30])
def test_validate_log_level_fail(log_level):
    assert validate_log_level(log_level) is False
