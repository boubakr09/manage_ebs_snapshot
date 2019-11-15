## Manage AWS EBS volumes snapshots

In general organizations protect critical and valuable data by doing regular backups (like ebs snapshot [see my repo](https://github.com/boubakr09/create_ebs_snapshot)). They are charged for the storage of the EBS snapshot they created. To reduce storage costs they can automate the deletion of old snapshots.



## Run test

Use the [manage_ebs_snapshot.py](https://github.com/boubakr09/manage_ebs_snapshot/blob/master/manage_ebs_snapshot.py) script and customize it to your situation

Run the bellow command:

```
python3 manage_ebs_snapshots.py
```
