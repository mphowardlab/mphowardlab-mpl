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
python3 install.py -o ~/myproject/styles
```

Use the `-j` option to limit the journal styles that are installed. One or more
of the following values can be specified:

* `acs`: American Chemical Society (ACS) journals
* `aip`: American Institute of Physics (AIP) journals

The default value is `all`, which will install all of the above.

To uninstall, simply remove the files that you installed. This is easier in a
project than in the configuration directory!

For best results, you should make sure to install the Microsoft fonts.

## Using styles

### Specify a style

The following styles *may* exist (but are not required) for each `<journal>`:

* `<journal>`: default one-panel figure
* `<journal>-tall`: one-column two-panel figure
* `<journal>-wide`: two-column figure

To use a style in your plot, load it at the top of your script. You should **always**
load the `mphowardlab` style first, followed by any options for a particular journal.

Example for a one-panel AIP figure with styles installed in shared directory:
```python
import matplotlib.pyplot as plt
plt.style.use(['mphowardlab','aip'])
```

Example for a one-panel AIP figure with styles installed in a project:
```python
import matplotlib.pyplot as plt
plt.style.use(['./mphowardlab.mplstyle','./aip.mplstyle'])
```

### Colors

The default color cyle implements the following colors that may be manually specified
in plot commands:

* `C0`: red
* `C1`: blue
* `C2`: green
* `C3`: orange
* `C4`: purple
* `C5`: pink
* `C6`: gold
* `C7`: grey
* `C8`: black

## Adding new styles

New journal styles can be added to this collection using the following steps:

1. Choose a journal name prefix that is not already taken.
2. Create as many style files as you want, always including the prefix and
   following the naming conventions listed above.
3. Add this prefix to the list of choices in `install.py`.

For detailed style file options, see this [tutorial][2] with an example
`matplotlibrc` file.

[1]: https://matplotlib.org
[2]: https://matplotlib.org/stable/tutorials/introductory/customizing.html
