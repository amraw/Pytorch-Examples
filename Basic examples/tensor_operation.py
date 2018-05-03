import torch

tensor = torch.zeros(4, 4)
tensor2 = torch.rand(4,4)
print(tensor)

print(torch.numel(tensor))

print(tensor.mm(tensor2))