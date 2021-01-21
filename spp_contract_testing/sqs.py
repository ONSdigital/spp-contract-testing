import json

from schema import And, Schema, Use


def wrap_schema_for_sqs(contract_schema: Schema) -> Schema:
    return Schema(
        {
            "Messages": [
                Schema(
                    {"body": And(Use(json.loads), contract_schema)},
                    ignore_extra_keys=True,
                ),
            ],
        },
        ignore_extra_keys=True,
    )

def wrap_schema_for_sqs_event(contract_schema: Schema) -> Schema:
    return Schema(
        {
            "Records": [
                Schema(
                    {"body": And(Use(json.loads), contract_schema)},
                    ignore_extra_keys=True,
                ),
            ],
        },
        ignore_extra_keys=True,
    )
