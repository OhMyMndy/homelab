# RepositoryRuleViolationError

Repository rule violation was detected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**metadata** | [**RepositoryRuleViolationErrorMetadata**](RepositoryRuleViolationErrorMetadata.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_violation_error import RepositoryRuleViolationError

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleViolationError from a JSON string
repository_rule_violation_error_instance = RepositoryRuleViolationError.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleViolationError.to_json())

# convert the object into a dict
repository_rule_violation_error_dict = repository_rule_violation_error_instance.to_dict()
# create an instance of RepositoryRuleViolationError from a dict
repository_rule_violation_error_from_dict = RepositoryRuleViolationError.from_dict(repository_rule_violation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


