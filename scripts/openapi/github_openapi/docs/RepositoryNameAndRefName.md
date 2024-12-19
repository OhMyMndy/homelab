# RepositoryNameAndRefName

Conditions to target repositories by name and refs by name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_name** | [**RepositoryRulesetConditionsRefName**](RepositoryRulesetConditionsRefName.md) |  | [optional] 
**repository_name** | [**RepositoryRulesetConditionsRepositoryNameTargetRepositoryName**](RepositoryRulesetConditionsRepositoryNameTargetRepositoryName.md) |  | 

## Example

```python
from github_openapi.models.repository_name_and_ref_name import RepositoryNameAndRefName

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryNameAndRefName from a JSON string
repository_name_and_ref_name_instance = RepositoryNameAndRefName.from_json(json)
# print the JSON string representation of the object
print(RepositoryNameAndRefName.to_json())

# convert the object into a dict
repository_name_and_ref_name_dict = repository_name_and_ref_name_instance.to_dict()
# create an instance of RepositoryNameAndRefName from a dict
repository_name_and_ref_name_from_dict = RepositoryNameAndRefName.from_dict(repository_name_and_ref_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


