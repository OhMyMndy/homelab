# RepositoryPropertyAndRefName

Conditions to target repositories by property and refs by name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_name** | [**RepositoryRulesetConditionsRefName**](RepositoryRulesetConditionsRefName.md) |  | [optional] 
**repository_property** | [**RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty**](RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.md) |  | 

## Example

```python
from github_openapi.models.repository_property_and_ref_name import RepositoryPropertyAndRefName

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryPropertyAndRefName from a JSON string
repository_property_and_ref_name_instance = RepositoryPropertyAndRefName.from_json(json)
# print the JSON string representation of the object
print(RepositoryPropertyAndRefName.to_json())

# convert the object into a dict
repository_property_and_ref_name_dict = repository_property_and_ref_name_instance.to_dict()
# create an instance of RepositoryPropertyAndRefName from a dict
repository_property_and_ref_name_from_dict = RepositoryPropertyAndRefName.from_dict(repository_property_and_ref_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


