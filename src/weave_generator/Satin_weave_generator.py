import sys

def Stain_weave_matrix(param1, param2, direction):
    """
    生成缎纹矩阵
    param1: 枚数
    param2: 飞数
    direction: 经纬面 ('经面' 或 '纬面')
    
    返回:
        缎纹矩阵
    """
    size = param1
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    
    if direction == "经面":
        # 经面缎纹：经线浮在表面，每列只有一个组织点，向上移动飞数

        # 在第一列的最底行放置1
        matrix[size-1][0] = 1

        # 生成其他列
        for j in range(1, size):
            # 从最底行开始，每列向上移动param2个位置
            row_index = (size - 1 - j * param2) % size
            matrix[row_index][j] = 1

        # 经面缎纹：在生成的经面缎纹基础上反转（0变1，1变0）
        matrix = [[1 - cell for cell in row] for row in matrix]
            
    else:  # 纬面
        # 纬面缎纹：纬线浮在表面，每行只有一个组织点，向右移动飞数

        # 在第一行的第一列放置1
        matrix[0][0] = 1

        # 生成其他行
        for i in range(1, size):
            # 从第一列开始，每行向右移动param2个位置
            col_index = (i * param2) % size
            matrix[i][col_index] = 1

        # 纬面缎纹：将行反转（第一行变成最后一行）
        matrix = matrix[::-1]
    
    return matrix
