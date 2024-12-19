# Verification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | 
**reason** | **str** |  | 
**payload** | **str** |  | 
**signature** | **str** |  | 
**verified_at** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.verification import Verification

# TODO update the JSON string below
json = "{}"
# create an instance of Verification from a JSON string
verification_instance = Verification.from_json(json)
# print the JSON string representation of the object
print(Verification.to_json())

# convert the object into a dict
verification_dict = verification_instance.to_dict()
# create an instance of Verification from a dict
verification_from_dict = Verification.from_dict(verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


