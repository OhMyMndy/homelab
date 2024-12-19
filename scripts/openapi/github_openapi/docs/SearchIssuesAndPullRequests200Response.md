# SearchIssuesAndPullRequests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**incomplete_results** | **bool** |  | 
**items** | [**List[IssueSearchResultItem]**](IssueSearchResultItem.md) |  | 

## Example

```python
from github_openapi.models.search_issues_and_pull_requests200_response import SearchIssuesAndPullRequests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchIssuesAndPullRequests200Response from a JSON string
search_issues_and_pull_requests200_response_instance = SearchIssuesAndPullRequests200Response.from_json(json)
# print the JSON string representation of the object
print(SearchIssuesAndPullRequests200Response.to_json())

# convert the object into a dict
search_issues_and_pull_requests200_response_dict = search_issues_and_pull_requests200_response_instance.to_dict()
# create an instance of SearchIssuesAndPullRequests200Response from a dict
search_issues_and_pull_requests200_response_from_dict = SearchIssuesAndPullRequests200Response.from_dict(search_issues_and_pull_requests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


