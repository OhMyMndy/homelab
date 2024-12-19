# OrgsUpdatePatAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action to apply to the fine-grained personal access token. | 

## Example

```python
from github_openapi.models.orgs_update_pat_access_request import OrgsUpdatePatAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsUpdatePatAccessRequest from a JSON string
orgs_update_pat_access_request_instance = OrgsUpdatePatAccessRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsUpdatePatAccessRequest.to_json())

# convert the object into a dict
orgs_update_pat_access_request_dict = orgs_update_pat_access_request_instance.to_dict()
# create an instance of OrgsUpdatePatAccessRequest from a dict
orgs_update_pat_access_request_from_dict = OrgsUpdatePatAccessRequest.from_dict(orgs_update_pat_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


