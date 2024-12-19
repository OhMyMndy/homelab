# CopilotDotcomPullRequestsRepositoriesInnerModelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the model used for Copilot code completion suggestions. If the default model is used will appear as &#39;default&#39;. | [optional] 
**is_custom_model** | **bool** | Indicates whether a model is custom or default. | [optional] 
**custom_model_training_date** | **str** | The training date for the custom model. | [optional] 
**total_pr_summaries_created** | **int** | The number of pull request summaries generated using Copilot for Pull Requests in the given repository. | [optional] 
**total_engaged_users** | **int** | The number of users who generated pull request summaries using Copilot for Pull Requests in the given repository and model. | [optional] 

## Example

```python
from github_openapi.models.copilot_dotcom_pull_requests_repositories_inner_models_inner import CopilotDotcomPullRequestsRepositoriesInnerModelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotDotcomPullRequestsRepositoriesInnerModelsInner from a JSON string
copilot_dotcom_pull_requests_repositories_inner_models_inner_instance = CopilotDotcomPullRequestsRepositoriesInnerModelsInner.from_json(json)
# print the JSON string representation of the object
print(CopilotDotcomPullRequestsRepositoriesInnerModelsInner.to_json())

# convert the object into a dict
copilot_dotcom_pull_requests_repositories_inner_models_inner_dict = copilot_dotcom_pull_requests_repositories_inner_models_inner_instance.to_dict()
# create an instance of CopilotDotcomPullRequestsRepositoriesInnerModelsInner from a dict
copilot_dotcom_pull_requests_repositories_inner_models_inner_from_dict = CopilotDotcomPullRequestsRepositoriesInnerModelsInner.from_dict(copilot_dotcom_pull_requests_repositories_inner_models_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


