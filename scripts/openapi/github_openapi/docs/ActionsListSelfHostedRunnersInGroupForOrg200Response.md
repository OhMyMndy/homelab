# ActionsListSelfHostedRunnersInGroupForOrg200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **float** |  | 
**runners** | [**List[Runner]**](Runner.md) |  | 

## Example

```python
from github_openapi.models.actions_list_self_hosted_runners_in_group_for_org200_response import ActionsListSelfHostedRunnersInGroupForOrg200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsListSelfHostedRunnersInGroupForOrg200Response from a JSON string
actions_list_self_hosted_runners_in_group_for_org200_response_instance = ActionsListSelfHostedRunnersInGroupForOrg200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsListSelfHostedRunnersInGroupForOrg200Response.to_json())

# convert the object into a dict
actions_list_self_hosted_runners_in_group_for_org200_response_dict = actions_list_self_hosted_runners_in_group_for_org200_response_instance.to_dict()
# create an instance of ActionsListSelfHostedRunnersInGroupForOrg200Response from a dict
actions_list_self_hosted_runners_in_group_for_org200_response_from_dict = ActionsListSelfHostedRunnersInGroupForOrg200Response.from_dict(actions_list_self_hosted_runners_in_group_for_org200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


