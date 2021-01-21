import json
import logging
from typing import Union

from schema import And, Schema, Use


def validate_log_level(log_level: Union[str, int]) -> bool:
    level = logging.getLevelName(log_level)
    if type(level) == str and "Level" in level:
        return False
    return True


LOG_CONTEXT = Schema(
    {
        "log_correlation_id": str,
        "log_level": validate_log_level,
    },
    ignore_extra_keys=True,
)

LOG_CONTEXT_JSON = Schema(And(Use(json.loads), LOG_CONTEXT))
