# PublicUserPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collaborators** | **int** |  | 
**name** | **str** |  | 
**space** | **int** |  | 
**private_repos** | **int** |  | 

## Example

```python
from github_openapi.models.public_user_plan import PublicUserPlan

# TODO update the JSON string below
json = "{}"
# create an instance of PublicUserPlan from a JSON string
public_user_plan_instance = PublicUserPlan.from_json(json)
# print the JSON string representation of the object
print(PublicUserPlan.to_json())

# convert the object into a dict
public_user_plan_dict = public_user_plan_instance.to_dict()
# create an instance of PublicUserPlan from a dict
public_user_plan_from_dict = PublicUserPlan.from_dict(public_user_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


