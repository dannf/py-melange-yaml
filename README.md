# A Python class for modifying melange YAML files

Make edits to Melange YAML files with Python. The class handles the basics of loading YAML files into a Python object, and dumping it back out again. It also has a bump_epoch() method. You still need to run `yam` after editing.

## Example: Adding a CXXFLAGS environment variable

```python
#!/usr/bin/env python3

import argparse
from MelangeYAML import MelangeYAML

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+')
    args = parser.parse_args()

    for f in args.filenames:
        my = MelangeYAML(f)
        e = my['environment'] = my.get('environment', {})
        ee = e['environment'] = e.get('environment', {})
        if 'CXXFLAGS' in ee.keys():
            if ee['CXXFLAGS'] == '-fdelete-null-pointer-checks':
                continue
            raise Exception("CXXFLAGS is already set to something else")
        ee['CXXFLAGS'] = '-fdelete-null-pointer-checks'
		my.bump_epoch()
        my.save()
```
