# ReposTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner** | **str** | The username or organization name the repository will be transferred to. | 
**new_name** | **str** | The new name to be given to the repository. | [optional] 
**team_ids** | **List[int]** | ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories. | [optional] 

## Example

```python
from github_openapi.models.repos_transfer_request import ReposTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposTransferRequest from a JSON string
repos_transfer_request_instance = ReposTransferRequest.from_json(json)
# print the JSON string representation of the object
print(ReposTransferRequest.to_json())

# convert the object into a dict
repos_transfer_request_dict = repos_transfer_request_instance.to_dict()
# create an instance of ReposTransferRequest from a dict
repos_transfer_request_from_dict = ReposTransferRequest.from_dict(repos_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


