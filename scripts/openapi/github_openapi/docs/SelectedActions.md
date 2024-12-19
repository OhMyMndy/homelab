# SelectedActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_owned_allowed** | **bool** | Whether GitHub-owned actions are allowed. For example, this includes the actions in the &#x60;actions&#x60; organization. | [optional] 
**verified_allowed** | **bool** | Whether actions from GitHub Marketplace verified creators are allowed. Set to &#x60;true&#x60; to allow all actions by GitHub Marketplace verified creators. | [optional] 
**patterns_allowed** | **List[str]** | Specifies a list of string-matching patterns to allow specific action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example, &#x60;monalisa/octocat@*&#x60;, &#x60;monalisa/octocat@v2&#x60;, &#x60;monalisa/*&#x60;.  &gt; [!NOTE] &gt; The &#x60;patterns_allowed&#x60; setting only applies to public repositories. | [optional] 

## Example

```python
from github_openapi.models.selected_actions import SelectedActions

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedActions from a JSON string
selected_actions_instance = SelectedActions.from_json(json)
# print the JSON string representation of the object
print(SelectedActions.to_json())

# convert the object into a dict
selected_actions_dict = selected_actions_instance.to_dict()
# create an instance of SelectedActions from a dict
selected_actions_from_dict = SelectedActions.from_dict(selected_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


