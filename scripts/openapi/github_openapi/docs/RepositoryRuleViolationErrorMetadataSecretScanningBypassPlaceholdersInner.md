# RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placeholder_id** | **str** | The ID of the push protection bypass placeholder. This value is returned on any push protected routes. | [optional] 
**token_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_violation_error_metadata_secret_scanning_bypass_placeholders_inner import RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner from a JSON string
repository_rule_violation_error_metadata_secret_scanning_bypass_placeholders_inner_instance = RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner.to_json())

# convert the object into a dict
repository_rule_violation_error_metadata_secret_scanning_bypass_placeholders_inner_dict = repository_rule_violation_error_metadata_secret_scanning_bypass_placeholders_inner_instance.to_dict()
# create an instance of RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner from a dict
repository_rule_violation_error_metadata_secret_scanning_bypass_placeholders_inner_from_dict = RepositoryRuleViolationErrorMetadataSecretScanningBypassPlaceholdersInner.from_dict(repository_rule_violation_error_metadata_secret_scanning_bypass_placeholders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


