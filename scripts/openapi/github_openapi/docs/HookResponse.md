# HookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from github_openapi.models.hook_response import HookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HookResponse from a JSON string
hook_response_instance = HookResponse.from_json(json)
# print the JSON string representation of the object
print(HookResponse.to_json())

# convert the object into a dict
hook_response_dict = hook_response_instance.to_dict()
# create an instance of HookResponse from a dict
hook_response_from_dict = HookResponse.from_dict(hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


