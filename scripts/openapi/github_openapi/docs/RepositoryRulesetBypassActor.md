# RepositoryRulesetBypassActor

An actor that can bypass rules in a ruleset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_id** | **int** | The ID of the actor that can bypass a ruleset. If &#x60;actor_type&#x60; is &#x60;OrganizationAdmin&#x60;, this should be &#x60;1&#x60;. If &#x60;actor_type&#x60; is &#x60;DeployKey&#x60;, this should be null. &#x60;OrganizationAdmin&#x60; is not applicable for personal repositories. | [optional] 
**actor_type** | **str** | The type of actor that can bypass a ruleset. | 
**bypass_mode** | **str** | When the specified actor can bypass the ruleset. &#x60;pull_request&#x60; means that an actor can only bypass rules on pull requests. &#x60;pull_request&#x60; is not applicable for the &#x60;DeployKey&#x60; actor type. Also, &#x60;pull_request&#x60; is only applicable to branch rulesets. | [optional] [default to 'always']

## Example

```python
from github_openapi.models.repository_ruleset_bypass_actor import RepositoryRulesetBypassActor

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetBypassActor from a JSON string
repository_ruleset_bypass_actor_instance = RepositoryRulesetBypassActor.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetBypassActor.to_json())

# convert the object into a dict
repository_ruleset_bypass_actor_dict = repository_ruleset_bypass_actor_instance.to_dict()
# create an instance of RepositoryRulesetBypassActor from a dict
repository_ruleset_bypass_actor_from_dict = RepositoryRulesetBypassActor.from_dict(repository_ruleset_bypass_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


