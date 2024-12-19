# Committer

Metaproperties for Git author/committer information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**email** | **str** |  | 
**name** | **str** | The git author&#39;s name. | 
**username** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.committer import Committer

# TODO update the JSON string below
json = "{}"
# create an instance of Committer from a JSON string
committer_instance = Committer.from_json(json)
# print the JSON string representation of the object
print(Committer.to_json())

# convert the object into a dict
committer_dict = committer_instance.to_dict()
# create an instance of Committer from a dict
committer_from_dict = Committer.from_dict(committer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


