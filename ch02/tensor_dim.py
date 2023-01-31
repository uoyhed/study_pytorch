import torch

# 텐서의 차원 조작 -> torch.tensor.view 사용
temp = torch.tensor([[1,2], [3,4]]) # 2x2 행렬
print(temp.shape)
print('-------------------------')
print(temp.view(4,1)) # 2x2 -> 4x1
print('-------------------------')
print(temp.view(-1)) # 2x2 -> 1차원으로 변경
print(temp.view(-1).shape) # torch.Size([4])
print('-------------------------')
print(temp.view(1, -1)) # 2x2 -> 1x? => 1x4로 변경
print(temp.view(1, -1).shape) # torch.Size([1, 4])
print('-------------------------')
print(temp.view(-1, 1)) # 2x2 -> ?x1 => 4x1로 변경
print(temp.view(-1, 1).shape) # torch.Size([4, 1])