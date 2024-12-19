# Snapshot

Create a new snapshot of a repository's dependencies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The version of the repository snapshot submission. | 
**job** | [**SnapshotJob**](SnapshotJob.md) |  | 
**sha** | **str** | The commit SHA associated with this dependency snapshot. Maximum length: 40 characters. | 
**ref** | **str** | The repository branch that triggered this snapshot. | 
**detector** | [**SnapshotDetector**](SnapshotDetector.md) |  | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | User-defined metadata to store domain-specific information limited to 8 keys with scalar values. | [optional] 
**manifests** | [**Dict[str, Manifest]**](Manifest.md) | A collection of package manifests, which are a collection of related dependencies declared in a file or representing a logical group of dependencies. | [optional] 
**scanned** | **datetime** | The time at which the snapshot was scanned. | 

## Example

```python
from github_openapi.models.snapshot import Snapshot

# TODO update the JSON string below
json = "{}"
# create an instance of Snapshot from a JSON string
snapshot_instance = Snapshot.from_json(json)
# print the JSON string representation of the object
print(Snapshot.to_json())

# convert the object into a dict
snapshot_dict = snapshot_instance.to_dict()
# create an instance of Snapshot from a dict
snapshot_from_dict = Snapshot.from_dict(snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


