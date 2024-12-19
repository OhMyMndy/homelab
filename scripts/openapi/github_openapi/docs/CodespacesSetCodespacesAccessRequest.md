# CodespacesSetCodespacesAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | **str** | Which users can access codespaces in the organization. &#x60;disabled&#x60; means that no users can access codespaces in the organization. | 
**selected_usernames** | **List[str]** | The usernames of the organization members who should have access to codespaces in the organization. Required when &#x60;visibility&#x60; is &#x60;selected_members&#x60;. The provided list of usernames will replace any existing value. | [optional] 

## Example

```python
from github_openapi.models.codespaces_set_codespaces_access_request import CodespacesSetCodespacesAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesSetCodespacesAccessRequest from a JSON string
codespaces_set_codespaces_access_request_instance = CodespacesSetCodespacesAccessRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesSetCodespacesAccessRequest.to_json())

# convert the object into a dict
codespaces_set_codespaces_access_request_dict = codespaces_set_codespaces_access_request_instance.to_dict()
# create an instance of CodespacesSetCodespacesAccessRequest from a dict
codespaces_set_codespaces_access_request_from_dict = CodespacesSetCodespacesAccessRequest.from_dict(codespaces_set_codespaces_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


