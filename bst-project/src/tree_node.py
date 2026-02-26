class TreeNode:
    """Класс узла бинарного дерева"""
    
    def __init__(self, key, value):
        """
        Инициализация узла дерева
        
        Args:
            key: Ключ узла
            value: Значение узла
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # высота для удобства вычислений
        
    def __repr__(self):
        """Строковое представление узла"""
        return f"TreeNode({self.key}: {self.value})"
