# CodespaceRuntimeConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_port_privacy_settings** | **List[str]** | The privacy settings a user can select from when forwarding a port. | [optional] 

## Example

```python
from github_openapi.models.codespace_runtime_constraints import CodespaceRuntimeConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of CodespaceRuntimeConstraints from a JSON string
codespace_runtime_constraints_instance = CodespaceRuntimeConstraints.from_json(json)
# print the JSON string representation of the object
print(CodespaceRuntimeConstraints.to_json())

# convert the object into a dict
codespace_runtime_constraints_dict = codespace_runtime_constraints_instance.to_dict()
# create an instance of CodespaceRuntimeConstraints from a dict
codespace_runtime_constraints_from_dict = CodespaceRuntimeConstraints.from_dict(codespace_runtime_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


