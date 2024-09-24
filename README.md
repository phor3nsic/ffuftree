# ffuftree
*Get output from ffuf and pipe it into ffuftree*

```

                                *
                               / \
                              ffuf\
                             /     \
                            ffuf    ffuf
                           /    ffuf \
                          ffuf        \
                         /     ffuf   ffuf
                         -------||-------

                         by: phor3nsic

```

### Install

- via pipx:

```sh
pipx install git+https://github.com/phor3nsic/ffuftree
```
- via pip:

```sh
pip install git+https://github.com/phor3nsic/ffuftree
```

### Example

After running ffuf and saving the output to `ffuf_output.json` and executing the following command:

```sh
cat ffuf_output.json | ffuftree
└── example.com
    └── api
        └── v2
            ├── users
            ├── affiliates
            ├── settings
            ├── campaigns
            ├── ping
            ├── transactions
            └── directlinks
```
