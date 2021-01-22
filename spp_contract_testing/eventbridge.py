import json
from datetime import datetime

from schema import And, Optional, Schema, Use


def wrap_schema_for_eventbridge(contract_schema: Schema) -> Schema:
    return Schema(
        {
            "Entries": [
                {
                    "Source": str,
                    "Detail": And(Use(json.loads), contract_schema),
                    Optional("DetailType"): str,
                    Optional("Time"): datetime,
                    Optional("Resources"): [str],
                    Optional("EventBusName"): str,
                }
            ]
        },
    )
