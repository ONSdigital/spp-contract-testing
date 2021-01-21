import json

from schema import And, Schema, Use


# This is what you would see if you uses boto3 client.receive_messages()
def wrap_schema_for_sqs(contract_schema: Schema) -> Schema:
    return Schema(
        {
            "Messages": [
                Schema(
                    {"Body": And(Use(json.loads), contract_schema)},
                    ignore_extra_keys=True,
                ),
            ],
        },
        ignore_extra_keys=True,
    )


# This is what you would see as the input event for a lambda triggered by sqs
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
