import argparse
from collections import UserDict
from ruamel.yaml import YAML


class MelangeYAML(UserDict):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.width = 4096
    yaml.default_flow_style = False

    def __init__(self, path):
        self.path = path
        with open(self.path, 'r') as yaml_in:
            self.load(yaml_in)

    def load(self, f):
        self.data = self.yaml.load(f)

    def dump(self, fout):
        self.yaml.dump(self.data, fout)

    def save(self):
        with open(self.path, 'w') as yaml_out:
            self.dump(yaml_out)

    def bump_epoch(self):
        self.data['package']['epoch'] += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+')
    args = parser.parse_args()

    for f in args.filenames:
        my = MelangeYAML(f)
        # Make edits
        my.save()
    # Run `yam` after
