# OrganizationFullPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**space** | **int** |  | 
**private_repos** | **int** |  | 
**filled_seats** | **int** |  | [optional] 
**seats** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.organization_full_plan import OrganizationFullPlan

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationFullPlan from a JSON string
organization_full_plan_instance = OrganizationFullPlan.from_json(json)
# print the JSON string representation of the object
print(OrganizationFullPlan.to_json())

# convert the object into a dict
organization_full_plan_dict = organization_full_plan_instance.to_dict()
# create an instance of OrganizationFullPlan from a dict
organization_full_plan_from_dict = OrganizationFullPlan.from_dict(organization_full_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


