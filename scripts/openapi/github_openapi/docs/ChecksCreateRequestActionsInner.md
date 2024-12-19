# ChecksCreateRequestActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The text to be displayed on a button in the web UI. The maximum size is 20 characters. | 
**description** | **str** | A short explanation of what this action would do. The maximum size is 40 characters. | 
**identifier** | **str** | A reference for the action on the integrator&#39;s system. The maximum size is 20 characters. | 

## Example

```python
from github_openapi.models.checks_create_request_actions_inner import ChecksCreateRequestActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksCreateRequestActionsInner from a JSON string
checks_create_request_actions_inner_instance = ChecksCreateRequestActionsInner.from_json(json)
# print the JSON string representation of the object
print(ChecksCreateRequestActionsInner.to_json())

# convert the object into a dict
checks_create_request_actions_inner_dict = checks_create_request_actions_inner_instance.to_dict()
# create an instance of ChecksCreateRequestActionsInner from a dict
checks_create_request_actions_inner_from_dict = ChecksCreateRequestActionsInner.from_dict(checks_create_request_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


