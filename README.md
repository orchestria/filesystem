# File system agent and tool

Agent and tool collection to interact with the local file system.

## Usage

Copy:

```
$ hatch run copy_file.py '{{"source": "/tmp/foo", "target": "/tmp/bar"}}'
{"status": "success"}
```

Move:

```
$ hatch run move_file.py '{{"source": "/tmp/foo", "target": "/tmp/bar"}}'
{"status": "success"}
```

List:

```
$ hatch run list_files.py '{{"path": "/tmp"}}'
["bar", "baz"]
```

Remove:

```
$ hatch run remove_files.py '{{"files": ["/tmp/bar"]}}'
Are you sure you want to remove the following files?
- /tmp/bar [y/n] (n): n
{"status": "cancelled"}
```

## License

The repo is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
