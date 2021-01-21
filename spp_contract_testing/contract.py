from typing import Any

from schema import Schema


def meets_contract(contract_schema: Schema, data: Any) -> bool:
    return contract_schema.validate(data)
