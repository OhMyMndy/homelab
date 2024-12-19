# TransactionApplicationResponse

Transactional creation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** |  | 
**logs** | **List[str]** |  | 

## Example

```python
from authentik_openapi.models.transaction_application_response import TransactionApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionApplicationResponse from a JSON string
transaction_application_response_instance = TransactionApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionApplicationResponse.to_json())

# convert the object into a dict
transaction_application_response_dict = transaction_application_response_instance.to_dict()
# create an instance of TransactionApplicationResponse from a dict
transaction_application_response_from_dict = TransactionApplicationResponse.from_dict(transaction_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


