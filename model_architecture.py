"""
Digit CNN definition (PyTorch sketch).

Three conv blocks + global average pool + linear head. Small enough to
run on CPU; replace with whatever your training pipeline produced.
"""
try:
    import torch
    import torch.nn as nn
except ImportError:  # keep file importable without torch in the demo
    torch = None
    nn = type("nn", (), {"Module": object, "Conv2d": object, "BatchNorm2d": object,
                          "ReLU": object, "MaxPool2d": object, "Linear": object,
                          "AdaptiveAvgPool2d": object, "Sequential": object})


class DigitCNN(nn.Module):  # type: ignore
    def __init__(self, n_classes: int = 10):
        super().__init__()
        self.body = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
        )
        self.head = nn.Linear(128, n_classes)

    def forward(self, x):
        z = self.body(x).flatten(1)
        return self.head(z)
