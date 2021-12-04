from dataclasses import dataclass
import pathlib


@dataclass
class TrainInput:
    batch_size: int
    dataset: pathlib.Path
    lr: float = 0.1
