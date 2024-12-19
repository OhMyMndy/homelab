# CommitParentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.commit_parents_inner import CommitParentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommitParentsInner from a JSON string
commit_parents_inner_instance = CommitParentsInner.from_json(json)
# print the JSON string representation of the object
print(CommitParentsInner.to_json())

# convert the object into a dict
commit_parents_inner_dict = commit_parents_inner_instance.to_dict()
# create an instance of CommitParentsInner from a dict
commit_parents_inner_from_dict = CommitParentsInner.from_dict(commit_parents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


