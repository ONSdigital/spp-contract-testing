from typing import Any

from schema import Schema


def validate_contract(contract_schema: Schema, data: Any) -> bool:
    return contract_schema.validate(data)
