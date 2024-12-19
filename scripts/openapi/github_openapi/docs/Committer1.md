# Committer1

Metaproperties for Git author/committer information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** | The git author&#39;s name. | 
**username** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.committer1 import Committer1

# TODO update the JSON string below
json = "{}"
# create an instance of Committer1 from a JSON string
committer1_instance = Committer1.from_json(json)
# print the JSON string representation of the object
print(Committer1.to_json())

# convert the object into a dict
committer1_dict = committer1_instance.to_dict()
# create an instance of Committer1 from a dict
committer1_from_dict = Committer1.from_dict(committer1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


