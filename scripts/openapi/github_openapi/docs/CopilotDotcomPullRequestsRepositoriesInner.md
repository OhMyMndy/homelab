# CopilotDotcomPullRequestsRepositoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Repository name | [optional] 
**total_engaged_users** | **int** | The number of users who generated pull request summaries using Copilot for Pull Requests in the given repository. | [optional] 
**models** | [**List[CopilotDotcomPullRequestsRepositoriesInnerModelsInner]**](CopilotDotcomPullRequestsRepositoriesInnerModelsInner.md) | List of model metrics for custom models and the default model. | [optional] 

## Example

```python
from github_openapi.models.copilot_dotcom_pull_requests_repositories_inner import CopilotDotcomPullRequestsRepositoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotDotcomPullRequestsRepositoriesInner from a JSON string
copilot_dotcom_pull_requests_repositories_inner_instance = CopilotDotcomPullRequestsRepositoriesInner.from_json(json)
# print the JSON string representation of the object
print(CopilotDotcomPullRequestsRepositoriesInner.to_json())

# convert the object into a dict
copilot_dotcom_pull_requests_repositories_inner_dict = copilot_dotcom_pull_requests_repositories_inner_instance.to_dict()
# create an instance of CopilotDotcomPullRequestsRepositoriesInner from a dict
copilot_dotcom_pull_requests_repositories_inner_from_dict = CopilotDotcomPullRequestsRepositoriesInner.from_dict(copilot_dotcom_pull_requests_repositories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


