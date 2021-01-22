# SPP Contract Testing

This repo provides some tools and wrappers to make testing contracts from [spp-contracts](https://github.com/ONSdigital/spp-contracts)
easy and safe.

## Install

### Pip

```sh
pip install git+https://github.com/ONSdigital/spp-contract-testing.git@main
```

### Poetry

```sh
poetry add --dev git+https://github.com/ONSdigital/spp-contract-testing.git@main
```

## Usage

```python
import spp_contracts
from spp_contract_testing import meets_contract

def test_lambda_handler():
    assert meets_contract(spp_contracts.SNAPSHOT, event)
```

### Wrappers

This repo provides a number of wrappers to make sure you can safely test your contracts within common schema.

For example if you receive your events from SQS, your actual contract will be received with some wrapped context.
To reduce human error and to make sure you don't have to worry about the standard SQS side of the contract we provide
wrapper functions:

| Wrapper                                 | Description                                                                                                                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `wrap_schema_for_eventbridge`           | If you send events to eventbridge using the `put_events` method, your message will need to be wrapped with `Entries` and some other eventbridge specific schema information |
| `wrap_schema_for_sqs`                   | This wrapper is compatable with messages that you would receive using `receive_message`                                                                                     |
| `wrap_schema_for_sqs_event`             | If your running a lambda that is triggered by an SQS event then the format of your event will be slightly different                                                         |
| `wrap_schema_for_sqs_eventbridge_event` | If eventbridge sends an event to an SQS queue to trigger a lambda your event format is different again                                                                      |

#### Example

```python
import spp_contracts
from spp_contract_testing import meets_contract, wrap_schema_for_sqs_event

def test_lambda_handler():
    assert meets_contract(wrap_schema_for_sqs_event(spp_contracts.SNAPSHOT), event)
```

## Contributing

1. Raise an Issue or just a PR for any features you think would be useful.
1. Please run `make format lint test` before submitting a PR.

**Note**: This repo uses [poetry](https://python-poetry.org/) to manage dependencies. To install: `pip3 install poetry` and to install dependencies `poetry install`.
