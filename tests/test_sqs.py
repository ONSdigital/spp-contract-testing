import pytest
import schema

from spp_contract_testing import (
    wrap_schema_for_sqs,
    wrap_schema_for_sqs_event,
    wrap_schema_for_sqs_eventbridge_event,
)


def test_wrap_schema_for_sqs(contract_schema):
    sqs_schema = wrap_schema_for_sqs(contract_schema)
    test_data = {"Messages": [{"Body": '{"foo": "baz", "bar": 20}'}]}
    assert sqs_schema.validate(test_data)


def test_wrap_schema_for_sqs_not_json(contract_schema):
    sqs_schema = wrap_schema_for_sqs(contract_schema)
    test_data = {"Messages": [{"Body": {"foo": "baz", "bar": 20}}]}
    with pytest.raises(schema.SchemaError) as error:
        sqs_schema.validate(test_data)
    assert (
        "Key 'Body' error:\n"
        + "loads({'foo': 'baz', 'bar': 20}) raised TypeError('the JSON object must be str, bytes or bytearray, not dict')"  # noqa: E501
    ) in str(error.value)


def test_wrap_schema_for_sqs_event(contract_schema):
    sqs_schema = wrap_schema_for_sqs_event(contract_schema)
    test_data = {"Records": [{"body": '{"foo": "baz", "bar": 20}'}]}
    assert sqs_schema.validate(test_data)


def test_wrap_schema_for_sqs_event_not_json(contract_schema):
    sqs_schema = wrap_schema_for_sqs_event(contract_schema)
    test_data = {"Records": [{"body": {"foo": "baz", "bar": 20}}]}
    with pytest.raises(schema.SchemaError) as error:
        sqs_schema.validate(test_data)
    assert (
        "Key 'body' error:\n"
        + "loads({'foo': 'baz', 'bar': 20}) raised TypeError('the JSON object must be str, bytes or bytearray, not dict')"  # noqa: E501
    ) in str(error.value)


def test_wrap_schema_for_sqs_eventbrdige_event(contract_schema):
    sqs_schema = wrap_schema_for_sqs_eventbridge_event(contract_schema)
    test_data = {"Records": [{"body": '{"detail": {"foo": "baz", "bar": 20}}'}]}
    assert sqs_schema.validate(test_data)


def test_wrap_schema_for_sqs_eventbridge_event_not_json(contract_schema):
    sqs_schema = wrap_schema_for_sqs_eventbridge_event(contract_schema)
    test_data = {"Records": [{"body": {"foo": "baz", "bar": 20}}]}
    with pytest.raises(schema.SchemaError) as error:
        sqs_schema.validate(test_data)
    assert (
        "Key 'body' error:\n"
        + "loads({'foo': 'baz', 'bar': 20}) raised TypeError('the JSON object must be str, bytes or bytearray, not dict')"  # noqa: E501
    ) in str(error.value)
