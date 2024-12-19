# StarredRepository

Starred Repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starred_at** | **datetime** |  | 
**repo** | [**Repository**](Repository.md) |  | 

## Example

```python
from github_openapi.models.starred_repository import StarredRepository

# TODO update the JSON string below
json = "{}"
# create an instance of StarredRepository from a JSON string
starred_repository_instance = StarredRepository.from_json(json)
# print the JSON string representation of the object
print(StarredRepository.to_json())

# convert the object into a dict
starred_repository_dict = starred_repository_instance.to_dict()
# create an instance of StarredRepository from a dict
starred_repository_from_dict = StarredRepository.from_dict(starred_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


