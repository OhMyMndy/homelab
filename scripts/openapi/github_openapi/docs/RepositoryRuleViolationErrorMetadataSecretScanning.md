# RepositoryRuleViolationErrorMetadataSecretScanning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_placeholders** | [**List[RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner]**](RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_violation_error_metadata_secret_scanning import RepositoryRuleViolationErrorMetadataSecretScanning

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleViolationErrorMetadataSecretScanning from a JSON string
repository_rule_violation_error_metadata_secret_scanning_instance = RepositoryRuleViolationErrorMetadataSecretScanning.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleViolationErrorMetadataSecretScanning.to_json())

# convert the object into a dict
repository_rule_violation_error_metadata_secret_scanning_dict = repository_rule_violation_error_metadata_secret_scanning_instance.to_dict()
# create an instance of RepositoryRuleViolationErrorMetadataSecretScanning from a dict
repository_rule_violation_error_metadata_secret_scanning_from_dict = RepositoryRuleViolationErrorMetadataSecretScanning.from_dict(repository_rule_violation_error_metadata_secret_scanning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


