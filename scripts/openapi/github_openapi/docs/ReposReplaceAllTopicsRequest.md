# ReposReplaceAllTopicsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | An array of topics to add to the repository. Pass one or more topics to _replace_ the set of existing topics. Send an empty array (&#x60;[]&#x60;) to clear all topics from the repository. **Note:** Topic &#x60;names&#x60; cannot contain uppercase letters. | 

## Example

```python
from github_openapi.models.repos_replace_all_topics_request import ReposReplaceAllTopicsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposReplaceAllTopicsRequest from a JSON string
repos_replace_all_topics_request_instance = ReposReplaceAllTopicsRequest.from_json(json)
# print the JSON string representation of the object
print(ReposReplaceAllTopicsRequest.to_json())

# convert the object into a dict
repos_replace_all_topics_request_dict = repos_replace_all_topics_request_instance.to_dict()
# create an instance of ReposReplaceAllTopicsRequest from a dict
repos_replace_all_topics_request_from_dict = ReposReplaceAllTopicsRequest.from_dict(repos_replace_all_topics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


