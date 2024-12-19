# OrgsUpdate422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**documentation_url** | **str** |  | 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.orgs_update422_response import OrgsUpdate422Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsUpdate422Response from a JSON string
orgs_update422_response_instance = OrgsUpdate422Response.from_json(json)
# print the JSON string representation of the object
print(OrgsUpdate422Response.to_json())

# convert the object into a dict
orgs_update422_response_dict = orgs_update422_response_instance.to_dict()
# create an instance of OrgsUpdate422Response from a dict
orgs_update422_response_from_dict = OrgsUpdate422Response.from_dict(orgs_update422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


