from itertools import zip_longest

"""
参数1：分子[1, 2,1]
参数2：分母[3, 4,1]
参数3：左右
斜纹、加强斜纹、复合斜纹
"""

def Twill_weave_matrix(param1, param2, direction):
    # 验证参数
    if not all(isinstance(x, int) and x > 0 for x in param1 + param2):
        raise ValueError("参数组必须包含正整数")
    
    # 计算矩阵大小
    rows = sum(param1) + sum(param2)
    cols = rows  # 行列数相同
    
    # 生成第一列
    first_col = []
    # 自下而上生成
    # 交替处理参数组1和参数组2的元素
    for ones, zeros in zip_longest(param1, param2, fillvalue=0):
        if ones > 0:
            first_col[0:0] = [1] * ones
        if zeros > 0:
            first_col[0:0] = [0] * zeros
    
    # 确保长度正确
    first_col = first_col[-rows:] if len(first_col) > rows else first_col
    
    # 根据方向生成矩阵
    matrix = []
    current_col = first_col.copy()
    
    for _ in range(cols):
        matrix.append(current_col.copy())
        if direction == "右":
            # 将最下面元素移到最上面
            current_col = current_col[1:] + [current_col[0]]
        elif direction == "左":
            # 将最上面元素移到最下面
            current_col = [current_col[-1]] + current_col[:-1]
    
    # 转置矩阵，使每行对应输出的一行
    matrix = list(zip(*matrix))
    
    return matrix

# 示例使用（已注释，避免导入时自动执行）
# param1 = [1, 2,1]
# param2 = [3, 4,1]
# direction = "左"
# matrix = Twill_weave_matrix(param1, param2, direction)
#
# # 打印矩阵
# for row in matrix:
#     print(" ".join(map(str, row)))