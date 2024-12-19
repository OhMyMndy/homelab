# OrgsCreateOrUpdateCustomPropertiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**List[CustomProperty]**](CustomProperty.md) | The array of custom properties to create or update. | 

## Example

```python
from github_openapi.models.orgs_create_or_update_custom_properties_request import OrgsCreateOrUpdateCustomPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsCreateOrUpdateCustomPropertiesRequest from a JSON string
orgs_create_or_update_custom_properties_request_instance = OrgsCreateOrUpdateCustomPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsCreateOrUpdateCustomPropertiesRequest.to_json())

# convert the object into a dict
orgs_create_or_update_custom_properties_request_dict = orgs_create_or_update_custom_properties_request_instance.to_dict()
# create an instance of OrgsCreateOrUpdateCustomPropertiesRequest from a dict
orgs_create_or_update_custom_properties_request_from_dict = OrgsCreateOrUpdateCustomPropertiesRequest.from_dict(orgs_create_or_update_custom_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


