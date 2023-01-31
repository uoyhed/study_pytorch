import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([3, 4, 6])

# 텐서간 연산이 가능하다.
# 다만, 텐서 간의 타입이 같아야 한다.
print(a - b)
print(b - a)