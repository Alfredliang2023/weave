"""
矩阵操作工具模块
提供组织矩阵的基本操作功能
"""

import numpy as np

def transpose_matrix(matrix):
    """转置矩阵"""
    return np.array(matrix).T.tolist()

def concatenate_matrices_horizontal(matrices):
    """水平拼接矩阵"""
    return np.hstack(matrices).tolist()

def concatenate_matrices_vertical(matrices):
    """垂直拼接矩阵"""
    return np.vstack(matrices).tolist()

def repeat_matrix(matrix, rows, cols):
    """重复矩阵"""
    return np.tile(matrix, (rows, cols)).tolist()

def rotate_matrix(matrix, times=1):
    """旋转矩阵（90度）"""
    result = np.array(matrix)
    for _ in range(times):
        result = np.rot90(result)
    return result.tolist()

def flip_matrix_horizontal(matrix):
    """水平翻转矩阵"""
    return np.fliplr(np.array(matrix)).tolist()

def flip_matrix_vertical(matrix):
    """垂直翻转矩阵"""
    return np.flipud(np.array(matrix)).tolist()

def crop_matrix(matrix, start_row, start_col, rows, cols):
    """裁剪矩阵"""
    arr = np.array(matrix)
    return arr[start_row:start_row+rows, start_col:start_col+cols].tolist()

def pad_matrix(matrix, pad_value=0, top=0, bottom=0, left=0, right=0):
    """填充矩阵边缘"""
    return np.pad(np.array(matrix),
                  ((top, bottom), (left, right)),
                  mode='constant',
                  constant_values=pad_value).tolist()

def get_matrix_dimensions(matrix):
    """获取矩阵维度"""
    return len(matrix), len(matrix[0]) if matrix else 0

def fraction_matrix(numerators, denominators, mode):
    """
    生成分数矩阵（组织矩阵的第一列或第一行）
    参数:
        numerators: 分子列表
        denominators: 分母列表
        mode: 'J' 表示经向（生成列），'W' 表示纬向（生成行）
    返回:
        numpy数组形式的列或行向量
    """
    from itertools import zip_longest

    # 合并分子分母，交替插入
    combined = []
    for num, den in zip_longest(numerators, denominators, fillvalue=0):
        if num > 0:
            combined.extend([1] * num)
        if den > 0:
            combined.extend([0] * den)

    # 转换为numpy数组
    result = np.array(combined)

    # 根据模式返回列向量或行向量
    if mode == 'J':
        return result.reshape(-1, 1)  # 返回列向量
    elif mode == 'W':
        return result.reshape(1, -1)  # 返回行向量
    else:
        raise ValueError("mode必须是'J'或'W'")

def fly_transform(vector, n=1):
    """
    飞数变换：对向量进行循环移位
    参数:
        vector: 输入向量（numpy数组）
        n: 移位数，正数向下/向右移位，负数向上/向左移位
    返回:
        变换后的向量
    """
    if len(vector.shape) == 1:
        # 一维数组
        return np.roll(vector, n)
    elif vector.shape[0] == 1:
        # 行向量，向右滚动
        return np.roll(vector, n)
    else:
        # 列向量，向下滚动
        return np.roll(vector, n)
