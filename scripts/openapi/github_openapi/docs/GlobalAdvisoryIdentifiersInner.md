# GlobalAdvisoryIdentifiersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of identifier. | 
**value** | **str** | The identifier value. | 

## Example

```python
from github_openapi.models.global_advisory_identifiers_inner import GlobalAdvisoryIdentifiersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalAdvisoryIdentifiersInner from a JSON string
global_advisory_identifiers_inner_instance = GlobalAdvisoryIdentifiersInner.from_json(json)
# print the JSON string representation of the object
print(GlobalAdvisoryIdentifiersInner.to_json())

# convert the object into a dict
global_advisory_identifiers_inner_dict = global_advisory_identifiers_inner_instance.to_dict()
# create an instance of GlobalAdvisoryIdentifiersInner from a dict
global_advisory_identifiers_inner_from_dict = GlobalAdvisoryIdentifiersInner.from_dict(global_advisory_identifiers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


