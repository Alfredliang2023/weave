import numpy as np
from .Twill_weave_generator import Twill_weave_matrix

import math

def diamond_weave_generator(numerators, denominators, kj, kw):
    """
    菱形组织生成函数
    参数:
        numerators: 分子数组
        denominators: 分母数组
        kj: 整数参数，用于计算列方向的组织大小
        kw: 整数参数，用于计算行方向的组织大小
    返回:
        生成的菱形组织矩阵
    """
    # 计算组织大小
    Rj = 2 * kj - 2
    Rw = 2 * kw - 2

    # 调用Twill weave_generator中的Twill_weave_matrix生成基础矩阵
    base_matrix = Twill_weave_matrix(numerators, denominators, "右")

    # 将基础矩阵转换为numpy数组以便操作
    base_matrix = np.array(base_matrix)

    # 计算循环次数
    base_rows, base_cols = base_matrix.shape
    col_repeats = math.ceil(kj / base_cols)
    row_repeats = math.ceil(kw / base_rows)

    # 生成大基础矩阵
    large_base_matrix = np.tile(base_matrix, (row_repeats, col_repeats))

    # 从大基础矩阵的左下角取kj列和kw行形成left_down矩阵
    # 注意：numpy数组的索引是从0开始的，所以我们需要适当调整
    rows, cols = large_base_matrix.shape
    start_row = rows - kw
    end_row = rows
    start_col = 0
    end_col = kj

    left_down = large_base_matrix[start_row:end_row, start_col:end_col]

    # 以left_down矩阵的最后一列为对称轴生成right_down矩阵
    right_down = np.fliplr(left_down[:, :-1])  # 不包括最后一列，因为它是对称轴

    # 将left_down和right_down左右拼接生成down矩阵
    down = np.hstack((left_down, right_down))
    
    # 以down矩阵的最上一行为对称轴生成up矩阵
    up = np.flipud(down[1:, :])  # 不包括最上一行，因为它是对称轴

    # 将up和down上下拼接生成最终矩阵
    final_matrix = np.vstack((up, down))

    # 根据要求截取矩阵
    # 列数为：Rj = 2kj - 2（自左向右截取）
    # 行数为：Rw = 2kw - 2（自下而上截取）
    rows, cols = final_matrix.shape

    # 确保截取的范围不超过矩阵的实际大小
    Rj = min(Rj, cols)
    Rw = min(Rw, rows)

    # 自左向右截取列
    final_matrix = final_matrix[:, :Rj]

    # 自下而上截取行（numpy数组的索引是从上到下的，所以需要从末尾开始取）
    final_matrix = final_matrix[rows-Rw:, :]

    return final_matrix

# 示例使用
if __name__ == "__main__":
    numerators = [3]
    denominators = [3]
    kj = 9
    kw = 9
    
    result = diamond_weave_generator(numerators, denominators, kj, kw)