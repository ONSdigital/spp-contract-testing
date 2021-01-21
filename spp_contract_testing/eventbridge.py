from datetime import datetime

from schema import Optional, Schema


def wrap_schema_for_eventbridge(contract_schema: Schema) -> Schema:
    return Schema(
        {
            "Entries": [
                {
                    "Source": str,
                    "Detail": contract_schema,
                    Optional("DetailType"): str,
                    Optional("Time"): datetime,
                    Optional("Resources"): [str],
                    Optional("EventBusName"): str,
                }
            ]
        },
    )
