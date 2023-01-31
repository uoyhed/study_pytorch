# 1. 텐서 생성
import torch
print(torch.tensor([[1,2],[3,4]])) # 2차원 형태의 텐서 생성
#print(torch.tensor([[1,2],[3,4]], device="cuda:0")) # GPU에 텐서 생성
print(torch.tensor([[1,2],[3,4]], dtype=torch.float64)) # dtype을 이용해서 텐서 생성

# 2. 텐서 → ndarray
temp = torch.tensor([[1,2],[3,4]])
print(temp.numpy())

#temp = torch.tensor([[1,2],[3,4]], device="cuda:0")
#print(temp.to("cpu").numpy())