# ActionsWorkflowAccessToRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **str** | Defines the level of access that workflows outside of the repository have to actions and reusable workflows within the repository.  &#x60;none&#x60; means the access is only possible from workflows in this repository. &#x60;user&#x60; level access allows sharing across user owned private repositories only. &#x60;organization&#x60; level access allows sharing across the organization. | 

## Example

```python
from github_openapi.models.actions_workflow_access_to_repository import ActionsWorkflowAccessToRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsWorkflowAccessToRepository from a JSON string
actions_workflow_access_to_repository_instance = ActionsWorkflowAccessToRepository.from_json(json)
# print the JSON string representation of the object
print(ActionsWorkflowAccessToRepository.to_json())

# convert the object into a dict
actions_workflow_access_to_repository_dict = actions_workflow_access_to_repository_instance.to_dict()
# create an instance of ActionsWorkflowAccessToRepository from a dict
actions_workflow_access_to_repository_from_dict = ActionsWorkflowAccessToRepository.from_dict(actions_workflow_access_to_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


