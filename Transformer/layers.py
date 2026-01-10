import torch
import math
import torch.nn as nn
import torch.nn.functional as F

# Scaled Dot Product Attention§
class Attention(nn.Module):
  def __init__(self):
    super(Attention, self).__init__()

  def forward(self, q, k, v):
    d_k = k.dim()
    dot = torch.matmul(q, k.transpose(-2, -1))
    s = F.softmax(dot/math.sqrt(d_k), dim=-1)
    print(s)
    output = torch.matmul(s, v)
    return output