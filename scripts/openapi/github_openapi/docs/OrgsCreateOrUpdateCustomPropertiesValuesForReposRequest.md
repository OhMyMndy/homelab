# OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_names** | **List[str]** | The names of repositories that the custom property values will be applied to. | 
**properties** | [**List[CustomPropertyValue]**](CustomPropertyValue.md) | List of custom property names and associated values to apply to the repositories. | 

## Example

```python
from github_openapi.models.orgs_create_or_update_custom_properties_values_for_repos_request import OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest from a JSON string
orgs_create_or_update_custom_properties_values_for_repos_request_instance = OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest.to_json())

# convert the object into a dict
orgs_create_or_update_custom_properties_values_for_repos_request_dict = orgs_create_or_update_custom_properties_values_for_repos_request_instance.to_dict()
# create an instance of OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest from a dict
orgs_create_or_update_custom_properties_values_for_repos_request_from_dict = OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest.from_dict(orgs_create_or_update_custom_properties_values_for_repos_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


