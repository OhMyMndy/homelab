# RepositoryIdAndRefName

Conditions to target repositories by id and refs by name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_name** | [**RepositoryRulesetConditionsRefName**](RepositoryRulesetConditionsRefName.md) |  | [optional] 
**repository_id** | [**RepositoryRulesetConditionsRepositoryIdTargetRepositoryId**](RepositoryRulesetConditionsRepositoryIdTargetRepositoryId.md) |  | 

## Example

```python
from github_openapi.models.repository_id_and_ref_name import RepositoryIdAndRefName

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryIdAndRefName from a JSON string
repository_id_and_ref_name_instance = RepositoryIdAndRefName.from_json(json)
# print the JSON string representation of the object
print(RepositoryIdAndRefName.to_json())

# convert the object into a dict
repository_id_and_ref_name_dict = repository_id_and_ref_name_instance.to_dict()
# create an instance of RepositoryIdAndRefName from a dict
repository_id_and_ref_name_from_dict = RepositoryIdAndRefName.from_dict(repository_id_and_ref_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


