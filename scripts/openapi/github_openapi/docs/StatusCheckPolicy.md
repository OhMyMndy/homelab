# StatusCheckPolicy

Status Check Policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**strict** | **bool** |  | 
**contexts** | **List[str]** |  | 
**checks** | [**List[StatusCheckPolicyChecksInner]**](StatusCheckPolicyChecksInner.md) |  | 
**contexts_url** | **str** |  | 

## Example

```python
from github_openapi.models.status_check_policy import StatusCheckPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCheckPolicy from a JSON string
status_check_policy_instance = StatusCheckPolicy.from_json(json)
# print the JSON string representation of the object
print(StatusCheckPolicy.to_json())

# convert the object into a dict
status_check_policy_dict = status_check_policy_instance.to_dict()
# create an instance of StatusCheckPolicy from a dict
status_check_policy_from_dict = StatusCheckPolicy.from_dict(status_check_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


