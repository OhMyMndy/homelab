# OrgsUpdatePatAccessesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to apply to the fine-grained personal access token. | 
**pat_ids** | **List[int]** | The IDs of the fine-grained personal access tokens. | 

## Example

```python
from github_openapi.models.orgs_update_pat_accesses_request import OrgsUpdatePatAccessesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsUpdatePatAccessesRequest from a JSON string
orgs_update_pat_accesses_request_instance = OrgsUpdatePatAccessesRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsUpdatePatAccessesRequest.to_json())

# convert the object into a dict
orgs_update_pat_accesses_request_dict = orgs_update_pat_accesses_request_instance.to_dict()
# create an instance of OrgsUpdatePatAccessesRequest from a dict
orgs_update_pat_accesses_request_from_dict = OrgsUpdatePatAccessesRequest.from_dict(orgs_update_pat_accesses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


