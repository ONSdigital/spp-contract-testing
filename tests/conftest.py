import pytest
from schema import Schema


@pytest.fixture
def contract_schema():
    return Schema({"foo": str, "bar": int})


@pytest.fixture
def log_context_schema():
    return Schema(
        {
            "log_context": Schema(
                {"log_correlation_id": str, "log_level": str}, ignore_extra_keys=True
            )
        }
    )
