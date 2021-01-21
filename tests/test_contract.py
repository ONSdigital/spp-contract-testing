import pytest
import schema

from spp_contract_testing import schemas, validate_contract


@pytest.mark.parametrize(
    "schema,data",
    [
        (pytest.lazy_fixture("contract_schema"), {"foo": "baz", "bar": 20}),
        (pytest.lazy_fixture("contract_schema"), {"foo": "fwibble", "bar": 1}),
        (
            pytest.lazy_fixture("contract_schema"),
            {"foo": "a longer sentence should still be fine", "bar": 999999},
        ),
        (
            schemas.LOG_CONTEXT,
            {"log_correlation_id": "asdasdr", "log_level": "INFO"},
        ),
        (
            schemas.LOG_CONTEXT,
            {
                "log_correlation_id": "asdasdr",
                "log_level": "INFO",
                "extra": 20,
            },
        ),
        (
            schemas.LOG_CONTEXT_JSON,
            '{"log_correlation_id": "asdasdr", "log_level": "INFO"}',
        ),
        (
            schemas.LOG_CONTEXT_JSON,
            '{"log_correlation_id": "asdasdr","log_level": "INFO","extra": 20}',
        ),
    ],
)
def test_validate_contract(schema, data):
    assert validate_contract(schema, data)


@pytest.mark.parametrize(
    "error_type,error_string,schema,data",
    [
        (
            schema.SchemaMissingKeyError,
            "Missing keys: 'bar', 'foo'",
            pytest.lazy_fixture("contract_schema"),
            {},
        ),
        (
            schema.SchemaError,
            "Key 'foo' error:\n20 should be instance of 'str'",
            pytest.lazy_fixture("contract_schema"),
            {"foo": 20, "bar": "20"},
        ),
        (
            schema.SchemaError,
            (
                "Key 'log_level' error:\n"
                + "validate_log_level('MADE UP') should evaluate to True"
            ),
            schemas.LOG_CONTEXT,
            {"log_correlation_id": "asdasdr", "log_level": "MADE UP"},
        ),
    ],
)
def test_validate_contract_fail(error_type, error_string, schema, data):
    with pytest.raises(error_type) as error:
        validate_contract(schema, data)
    assert str(error.value) == error_string
