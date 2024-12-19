# RepositoryRuleViolationErrorMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_scanning** | [**RepositoryRuleViolationErrorMetadataSecretScanning**](RepositoryRuleViolationErrorMetadataSecretScanning.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_violation_error_metadata import RepositoryRuleViolationErrorMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleViolationErrorMetadata from a JSON string
repository_rule_violation_error_metadata_instance = RepositoryRuleViolationErrorMetadata.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleViolationErrorMetadata.to_json())

# convert the object into a dict
repository_rule_violation_error_metadata_dict = repository_rule_violation_error_metadata_instance.to_dict()
# create an instance of RepositoryRuleViolationErrorMetadata from a dict
repository_rule_violation_error_metadata_from_dict = RepositoryRuleViolationErrorMetadata.from_dict(repository_rule_violation_error_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


