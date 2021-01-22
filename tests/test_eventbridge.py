import json

import pytest
import schema

from spp_contract_testing import wrap_schema_for_eventbridge


def test_wrap_schema_for_eventbridge(contract_schema):
    eventbridge_schema = wrap_schema_for_eventbridge(contract_schema)
    test_data = {
        "Entries": [{"Source": "test", "Detail": json.dumps({"foo": "baz", "bar": 20})}]
    }
    assert eventbridge_schema.validate(test_data)


def test_wrap_schema_for_eventbridge_fail(contract_schema):
    eventbridge_schema = wrap_schema_for_eventbridge(contract_schema)
    test_data = {"Entries": [{"Source": "test"}]}
    with pytest.raises(schema.SchemaError) as error:
        eventbridge_schema.validate(test_data)
    assert "{'Source': 'test'}\nMissing key: 'Detail'" in str(error.value)
