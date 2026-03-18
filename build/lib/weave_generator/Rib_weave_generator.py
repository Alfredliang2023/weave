def Rib_weave_matrix(numerator, denominator, direction):
    """
    生成重平组织矩阵
    numerator: 分子列表 [分子1, 分子2, ...]
    denominator: 分母列表 [分母1, 分母2, ...]
    direction: '经' 或 '纬'向
    返回: 重平组织矩阵
    """
    if len(numerator) != len(denominator):
        raise ValueError("分子和分母的数量必须相同")

    param_groups = list(zip(numerator, denominator))

    if direction == '经':
        # 计算行数（所有参数的和）
        total_rows = sum(sum(group) for group in param_groups)
        cols = 2
        matrix = [[0 for _ in range(cols)] for _ in range(total_rows)]

        # 生成第一列
        current_row = total_rows - 1  # 从底部开始

        # 处理每组参数
        for group in param_groups:
            # 放置1
            for _ in range(group[0]):
                matrix[current_row][0] = 1
                current_row -= 1
            # 放置0
            for _ in range(group[1]):
                matrix[current_row][0] = 0
                current_row -= 1

        # 生成第二列（反转第一列的值）
        for i in range(total_rows):
            matrix[i][1] = 1 - matrix[i][0]

    else:  # 纬面
        # 计算列数（所有参数的和）
        total_cols = sum(sum(group) for group in param_groups)
        rows = 2
        matrix = [[0 for _ in range(total_cols)] for _ in range(rows)]

        # 生成第一行
        current_col = 0

        # 处理每组参数
        for group in param_groups:
            # 放置0
            for _ in range(group[0]):
                matrix[0][current_col] = 0
                current_col += 1
            # 放置1
            for _ in range(group[1]):
                matrix[0][current_col] = 1
                current_col += 1

        # 生成第二行（反转第一行的值）
        for j in range(total_cols):
            matrix[1][j] = 1 - matrix[0][j]

    return matrix


# 示例使用（仅在直接运行时执行）
if __name__ == "__main__":
    numerator = [3, 2]  # 分子
    denominator = [2, 1]  # 分母
    direction = '纬'  # 方向：'经' 或 '纬'
    matrix = Rib_weave_matrix(numerator, denominator, direction)
    # 打印矩阵
    for row in matrix:
        print(" ".join(map(str, row)))