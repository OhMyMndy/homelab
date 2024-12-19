# SCIMSourceRequest

SCIMSource Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.scim_source_request import SCIMSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMSourceRequest from a JSON string
scim_source_request_instance = SCIMSourceRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMSourceRequest.to_json())

# convert the object into a dict
scim_source_request_dict = scim_source_request_instance.to_dict()
# create an instance of SCIMSourceRequest from a dict
scim_source_request_from_dict = SCIMSourceRequest.from_dict(scim_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


