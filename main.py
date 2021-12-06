import argparse
import json
import pathlib

import dacite

from standard_input import TrainInput


def main(inp: TrainInput) -> None:
    print(inp)
    # do training


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to JSON")
    args = parser.parse_args()

    inp = dacite.from_dict(
        TrainInput,
        json.load(open(args.input)),
        dacite.Config(type_hooks={pathlib.Path: pathlib.Path}),
    )
    main(inp)
