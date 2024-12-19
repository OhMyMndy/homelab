# StatusCheckPolicyChecksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | 
**app_id** | **int** |  | 

## Example

```python
from github_openapi.models.status_check_policy_checks_inner import StatusCheckPolicyChecksInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCheckPolicyChecksInner from a JSON string
status_check_policy_checks_inner_instance = StatusCheckPolicyChecksInner.from_json(json)
# print the JSON string representation of the object
print(StatusCheckPolicyChecksInner.to_json())

# convert the object into a dict
status_check_policy_checks_inner_dict = status_check_policy_checks_inner_instance.to_dict()
# create an instance of StatusCheckPolicyChecksInner from a dict
status_check_policy_checks_inner_from_dict = StatusCheckPolicyChecksInner.from_dict(status_check_policy_checks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


