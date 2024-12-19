# OrgRepoCustomPropertyValues

List of custom property values for a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_id** | **int** |  | 
**repository_name** | **str** |  | 
**repository_full_name** | **str** |  | 
**properties** | [**List[CustomPropertyValue]**](CustomPropertyValue.md) | List of custom property names and associated values | 

## Example

```python
from github_openapi.models.org_repo_custom_property_values import OrgRepoCustomPropertyValues

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRepoCustomPropertyValues from a JSON string
org_repo_custom_property_values_instance = OrgRepoCustomPropertyValues.from_json(json)
# print the JSON string representation of the object
print(OrgRepoCustomPropertyValues.to_json())

# convert the object into a dict
org_repo_custom_property_values_dict = org_repo_custom_property_values_instance.to_dict()
# create an instance of OrgRepoCustomPropertyValues from a dict
org_repo_custom_property_values_from_dict = OrgRepoCustomPropertyValues.from_dict(org_repo_custom_property_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


