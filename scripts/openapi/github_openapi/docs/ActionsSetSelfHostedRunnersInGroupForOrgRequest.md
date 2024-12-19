# ActionsSetSelfHostedRunnersInGroupForOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runners** | **List[int]** | List of runner IDs to add to the runner group. | 

## Example

```python
from github_openapi.models.actions_set_self_hosted_runners_in_group_for_org_request import ActionsSetSelfHostedRunnersInGroupForOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetSelfHostedRunnersInGroupForOrgRequest from a JSON string
actions_set_self_hosted_runners_in_group_for_org_request_instance = ActionsSetSelfHostedRunnersInGroupForOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsSetSelfHostedRunnersInGroupForOrgRequest.to_json())

# convert the object into a dict
actions_set_self_hosted_runners_in_group_for_org_request_dict = actions_set_self_hosted_runners_in_group_for_org_request_instance.to_dict()
# create an instance of ActionsSetSelfHostedRunnersInGroupForOrgRequest from a dict
actions_set_self_hosted_runners_in_group_for_org_request_from_dict = ActionsSetSelfHostedRunnersInGroupForOrgRequest.from_dict(actions_set_self_hosted_runners_in_group_for_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


