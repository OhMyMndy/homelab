# PullRequestSimpleLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**Link**](Link.md) |  | 
**commits** | [**Link**](Link.md) |  | 
**statuses** | [**Link**](Link.md) |  | 
**html** | [**Link**](Link.md) |  | 
**issue** | [**Link**](Link.md) |  | 
**review_comments** | [**Link**](Link.md) |  | 
**review_comment** | [**Link**](Link.md) |  | 
**var_self** | [**Link**](Link.md) |  | 

## Example

```python
from github_openapi.models.pull_request_simple_links import PullRequestSimpleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestSimpleLinks from a JSON string
pull_request_simple_links_instance = PullRequestSimpleLinks.from_json(json)
# print the JSON string representation of the object
print(PullRequestSimpleLinks.to_json())

# convert the object into a dict
pull_request_simple_links_dict = pull_request_simple_links_instance.to_dict()
# create an instance of PullRequestSimpleLinks from a dict
pull_request_simple_links_from_dict = PullRequestSimpleLinks.from_dict(pull_request_simple_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


