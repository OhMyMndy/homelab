# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | 
**description** | **str** |  | 
**events_url** | **str** |  | 
**hooks_url** | **str** |  | 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | 
**issues_url** | **str** |  | 
**login** | **str** |  | 
**members_url** | **str** |  | 
**node_id** | **str** |  | 
**public_members_url** | **str** |  | 
**repos_url** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


