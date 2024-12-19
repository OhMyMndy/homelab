# Reactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1** | **int** |  | 
**var_1** | **int** |  | 
**confused** | **int** |  | 
**eyes** | **int** |  | 
**heart** | **int** |  | 
**hooray** | **int** |  | 
**laugh** | **int** |  | 
**rocket** | **int** |  | 
**total_count** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.reactions import Reactions

# TODO update the JSON string below
json = "{}"
# create an instance of Reactions from a JSON string
reactions_instance = Reactions.from_json(json)
# print the JSON string representation of the object
print(Reactions.to_json())

# convert the object into a dict
reactions_dict = reactions_instance.to_dict()
# create an instance of Reactions from a dict
reactions_from_dict = Reactions.from_dict(reactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


