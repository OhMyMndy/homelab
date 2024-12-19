# CopilotDotcomPullRequests

Usage metrics for Copilot for pull requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_engaged_users** | **int** | The number of users who used Copilot for Pull Requests on github.com to generate a pull request summary at least once. | [optional] 
**repositories** | [**List[CopilotDotcomPullRequestsRepositoriesInner]**](CopilotDotcomPullRequestsRepositoriesInner.md) | Repositories in which users used Copilot for Pull Requests to generate pull request summaries | [optional] 

## Example

```python
from github_openapi.models.copilot_dotcom_pull_requests import CopilotDotcomPullRequests

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotDotcomPullRequests from a JSON string
copilot_dotcom_pull_requests_instance = CopilotDotcomPullRequests.from_json(json)
# print the JSON string representation of the object
print(CopilotDotcomPullRequests.to_json())

# convert the object into a dict
copilot_dotcom_pull_requests_dict = copilot_dotcom_pull_requests_instance.to_dict()
# create an instance of CopilotDotcomPullRequests from a dict
copilot_dotcom_pull_requests_from_dict = CopilotDotcomPullRequests.from_dict(copilot_dotcom_pull_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


