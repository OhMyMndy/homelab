# FeedLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline** | [**LinkWithType**](LinkWithType.md) |  | 
**user** | [**LinkWithType**](LinkWithType.md) |  | 
**security_advisories** | [**LinkWithType**](LinkWithType.md) |  | [optional] 
**current_user** | [**LinkWithType**](LinkWithType.md) |  | [optional] 
**current_user_public** | [**LinkWithType**](LinkWithType.md) |  | [optional] 
**current_user_actor** | [**LinkWithType**](LinkWithType.md) |  | [optional] 
**current_user_organization** | [**LinkWithType**](LinkWithType.md) |  | [optional] 
**current_user_organizations** | [**List[LinkWithType]**](LinkWithType.md) |  | [optional] 
**repository_discussions** | [**LinkWithType**](LinkWithType.md) |  | [optional] 
**repository_discussions_category** | [**LinkWithType**](LinkWithType.md) |  | [optional] 

## Example

```python
from github_openapi.models.feed_links import FeedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of FeedLinks from a JSON string
feed_links_instance = FeedLinks.from_json(json)
# print the JSON string representation of the object
print(FeedLinks.to_json())

# convert the object into a dict
feed_links_dict = feed_links_instance.to_dict()
# create an instance of FeedLinks from a dict
feed_links_from_dict = FeedLinks.from_dict(feed_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


