
def Basket_weave_matrix(param1, param2):
    """
生成重平组织矩阵
numerator: 分子列表 [分子1, 分子2, ...]
denominator: 分母列表 [分母1, 分母2, ...]
返回: 方平平组织矩阵
"""
      
    def generate_column(param1, param2):
        """生成一个原始列，按 param1 和 param2 的节奏排列 1 和 0。"""
        col = []
        for p1, p2 in zip(param1, param2):
            col.extend([1] * p1)
            col.extend([0] * p2)
        return col

    def invert_column(col):
        """将原始列翻转（1变0，0变1）"""
        return [1 - c for c in col]

    def generate_columns(param1, param2):
        """按 param1 和 param2 定义的次数生成原始列和相反列"""
        original = generate_column(param1, param2)
        opposite = invert_column(original)
        col_block = []

        for p1, p2 in zip(param1, param2):
            col_block.extend([original] * p1)
            col_block.extend([opposite] * p2)
        return col_block

    # 步骤1：行数 = sum(param1) + sum(param2)
    num_rows = sum(param1) + sum(param2)

    # 步骤2-4：构造列块
    columns = generate_columns(param1, param2)


    # 按列转为矩阵（列转行），但顺序是自下而上
    matrix = []
    for i in range(num_rows):
        row = [col[-(i + 1)] for col in columns]  # 注意：负索引从末尾向前取
        matrix.append(row)

    return matrix


# 示例（仅在直接运行时执行）
if __name__ == "__main__":
    matrix1 = Basket_weave_matrix([4,3,2], [3,2,1])
    # 输出矩阵
    for row in matrix1:
        print(' '.join(map(str, row)))

