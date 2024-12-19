# ReposCreateOrUpdateCustomPropertiesValuesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**List[CustomPropertyValue]**](CustomPropertyValue.md) | A list of custom property names and associated values to apply to the repositories. | 

## Example

```python
from github_openapi.models.repos_create_or_update_custom_properties_values_request import ReposCreateOrUpdateCustomPropertiesValuesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateOrUpdateCustomPropertiesValuesRequest from a JSON string
repos_create_or_update_custom_properties_values_request_instance = ReposCreateOrUpdateCustomPropertiesValuesRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateOrUpdateCustomPropertiesValuesRequest.to_json())

# convert the object into a dict
repos_create_or_update_custom_properties_values_request_dict = repos_create_or_update_custom_properties_values_request_instance.to_dict()
# create an instance of ReposCreateOrUpdateCustomPropertiesValuesRequest from a dict
repos_create_or_update_custom_properties_values_request_from_dict = ReposCreateOrUpdateCustomPropertiesValuesRequest.from_dict(repos_create_or_update_custom_properties_values_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


