# ReposCreateTagProtectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** | An optional glob pattern to match against when enforcing tag protection. | 

## Example

```python
from github_openapi.models.repos_create_tag_protection_request import ReposCreateTagProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateTagProtectionRequest from a JSON string
repos_create_tag_protection_request_instance = ReposCreateTagProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateTagProtectionRequest.to_json())

# convert the object into a dict
repos_create_tag_protection_request_dict = repos_create_tag_protection_request_instance.to_dict()
# create an instance of ReposCreateTagProtectionRequest from a dict
repos_create_tag_protection_request_from_dict = ReposCreateTagProtectionRequest.from_dict(repos_create_tag_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


