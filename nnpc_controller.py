# nnpc_controller.py
# Simple demo implementation of a neural-network predictive controller (NNPC)
# MIT License

import numpy as np
import torch
import torch.nn as nn

class DynamicsNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 16), nn.ReLU(),
            nn.Linear(16, 16), nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.net(x)

model = DynamicsNN()
N = 10

def nnpc_control(y, y_ref):
    u = 0.0
    for k in range(N):
        inp = torch.tensor([y, y_ref[k], u], dtype=torch.float32)
        y_pred = model(inp)
        err = (y_ref[k] - y_pred)**2
        u = u + 0.01 * err.item()
    return u

if __name__ == "__main__":
    y = 0.0
    y_ref = np.ones(10) * 1.0
    u = nnpc_control(y, y_ref)
    print("NNPC output:", u)
