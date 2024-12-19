# RepositoryRulesetLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**RepositoryRulesetLinksSelf**](RepositoryRulesetLinksSelf.md) |  | [optional] 
**html** | [**RepositoryRulesetLinksHtml**](RepositoryRulesetLinksHtml.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_ruleset_links import RepositoryRulesetLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetLinks from a JSON string
repository_ruleset_links_instance = RepositoryRulesetLinks.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetLinks.to_json())

# convert the object into a dict
repository_ruleset_links_dict = repository_ruleset_links_instance.to_dict()
# create an instance of RepositoryRulesetLinks from a dict
repository_ruleset_links_from_dict = RepositoryRulesetLinks.from_dict(repository_ruleset_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


