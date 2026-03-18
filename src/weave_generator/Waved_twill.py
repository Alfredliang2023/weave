import numpy as np
from .matrix_operations import fraction_matrix, fly_transform

def Waved_twill_generate(numerators, denominators, direction, k_value):
    """
    生成山形斜纹组织矩阵
    参数:
        numerators: 分子列表
        denominators: 分母列表
        direction: 'Kj'或'Kw'，表示方向
        k_value: 整数，'Kj'或'Kw'的值
    返回:
        生成山形斜纹矩阵
    """
    # 计算k值（分子分母之和）
    k = sum(numerators) + sum(denominators)
    
    if direction.upper() == 'KJ':
        # 1. 生成第1列
        first_col = fraction_matrix(numerators, denominators, 'J')
        result = first_col.copy()
        
        # 2. 使用fly_transform(n=1)继续生成k_value-1列
        current_col = first_col.copy()
        for _ in range(k_value - 1):
            current_col = fly_transform(current_col, 1)
            result = np.hstack((result, current_col))
        
        # 3. 使用fly_transform(n=-1)对最后一列进行变换，生成k_value-2列
        last_col = result[:, -1].reshape(-1, 1)  # 获取最后一列
        current_col = last_col.copy()
        for _ in range(k_value - 2):
            current_col = fly_transform(current_col, -1)
            result = np.hstack((result, current_col))

        # 经向（Kj）：将行反转（第一行变成最后一行）
        result = result[::-1]

    elif direction.upper() == 'KW':
        # 1. 生成最后一行
        last_row = fraction_matrix(numerators, denominators, 'W')
        
        # 2. 使用fly_transform(n=1)对最后一行进行变换，生成k_value-1行（自下而上）
        rows_list = [last_row]  # 从下往上存储行
        current_row = last_row.copy()
        for _ in range(k_value - 1):
            current_row = fly_transform(current_row, 1)
            rows_list.append(current_row)  # 添加到列表末尾（自下而上）
        
        # 3. 使用fly_transform(n=-1)对最后生成的行进行变换，生成k_value-2行（自下而上）
        top_row = rows_list[-1].copy()  # 获取最上面的行
        current_row = top_row.copy()
        for _ in range(k_value - 2):
            current_row = fly_transform(current_row, -1)
            rows_list.append(current_row)  # 添加到列表末尾（自下而上）
        
        # 将所有行组合成最终矩阵（从上到下排列）
        result = np.vstack(rows_list[::-1])  # 反转列表以从上到下排列
    
    else:
        raise ValueError("direction必须是'Kj'或'Kw'")
    
    return result

# 测试代码
if __name__ == "__main__":
    # 测试示例1: Kj方向
    print("测试示例1 (Kj方向):")
    numerators = [3, 2]
    denominators = [1, 2]
    direction = "Kj"
    k_value = 8  # 指定k_value值
    
    result = Waved_twill_generate(numerators, denominators, direction, k_value)
    print("生成的波浪斜纹组织矩阵：")
    print(result)
    print("\n矩阵形状:", result.shape)
    
    # 测试示例2: Kw方向
    print("\n测试示例2 (Kw方向):")
    numerators = [3, 2]
    denominators = [2, 1]
    direction = "Kw"
    k_value = 10  # 指定k_value值
    
    result = Waved_twill_generate(numerators, denominators, direction, k_value)
    print("生成的波浪斜纹组织矩阵：")
    print(result)
    print("\n矩阵形状:", result.shape)