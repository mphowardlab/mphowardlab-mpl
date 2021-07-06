# mphowardlab-mpl

A collection of [matplotlib][1] style files compatible with
various scientific journals.

## Installing

Use `install.py` to make a copy of the style files. There are a few installation
options:

1. Detect and install all styles to the shared matplotlib configuration directory:
```bash
python3 install.py
```

2. Install to a specific directory (e.g., a project)
```bash
python3 install.py ~/myproject/styles
```

Use the `-j` option to limit the journal styles that are installed. One or more
of the following values can be specified:

* `acs`: American Chemical Society (ACS) journals
* `aip`: American Institute of Physics (AIP) journals

The default value is `all`, which will install all of the above.

To uninstall, simply remove the files that you installed. This is easier in a
project than in the configuration directory!

## Adding new styles

New journal styles can be added to this collection using the following steps:

1. Choose a journal name prefix that is not already taken.
2. Create as many style files as you want, including the prefix somewhere
   in the filename. It is suggested to prepend it to keep this organized.
3. Add this prefix to the list of choices in `install.py`.

For detailed style file options, see this [tutorial][2] with an example
`matplotlibrc` file.

[1]: https://matplotlib.org
[2]: https://matplotlib.org/stable/tutorials/introductory/customizing.html
