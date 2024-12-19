# CodeSecurityDetachConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_repository_ids** | **List[int]** | An array of repository IDs to detach from configurations. | [optional] 

## Example

```python
from github_openapi.models.code_security_detach_configuration_request import CodeSecurityDetachConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeSecurityDetachConfigurationRequest from a JSON string
code_security_detach_configuration_request_instance = CodeSecurityDetachConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(CodeSecurityDetachConfigurationRequest.to_json())

# convert the object into a dict
code_security_detach_configuration_request_dict = code_security_detach_configuration_request_instance.to_dict()
# create an instance of CodeSecurityDetachConfigurationRequest from a dict
code_security_detach_configuration_request_from_dict = CodeSecurityDetachConfigurationRequest.from_dict(code_security_detach_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


