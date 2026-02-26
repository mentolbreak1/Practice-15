from typing import Optional, Any, Tuple
from src.tree_node import TreeNode


class BinarySearchTree:
    """Класс бинарного дерева поиска"""
    
    def __init__(self):
        """Инициализация пустого дерева"""
        self.root = None
        self.size = 0
    
    def insert(self, key: Any, value: Any) -> None:
        """
        Вставка элемента в дерево
        
        Args:
            key: Ключ для вставки
            value: Значение для вставки
        """
        self.root = self._insert_recursive(self.root, key, value)
        self.size += 1
    
    def _insert_recursive(self, node: Optional[TreeNode], key: Any, value: Any) -> TreeNode:
        """
        Рекурсивная вставка элемента
        
        Args:
            node: Текущий узел
            key: Ключ
            value: Значение
            
        Returns:
            TreeNode: Новый или обновленный узел
        """
        # Если достигли пустого места, создаем новый узел
        if node is None:
            return TreeNode(key, value)
        
        # Вставка в левое поддерево
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        # Вставка в правое поддерево
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        # Если ключ уже существует, обновляем значение
        else:
            node.value = value
            self.size -= 1  # коррекция размера, так как это не новая вставка
            return node
        
        # Обновление высоты
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))
        
        return node
    
    def search(self, key: Any) -> Optional[Any]:
        """
        Поиск значения по ключу
        
        Args:
            key: Ключ для поиска
            
        Returns:
            Optional[Any]: Значение, если ключ найден, иначе None
        """
        node = self._search_recursive(self.root, key)
        return node.value if node else None
    
    def _search_recursive(self, node: Optional[TreeNode], key: Any) -> Optional[TreeNode]:
        """
        Рекурсивный поиск узла по ключу
        
        Args:
            node: Текущий узел
            key: Ключ для поиска
            
        Returns:
            Optional[TreeNode]: Найденный узел или None
        """
        if node is None or node.key == key:
            return node
        
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def delete(self, key: Any) -> bool:
        """
        Удаление элемента по ключу
        
        Args:
            key: Ключ для удаления
            
        Returns:
            bool: True если элемент был удален, False если не найден
        """
        self.root, deleted = self._delete_recursive(self.root, key)
        if deleted:
            self.size -= 1
        return deleted
    
    def _delete_recursive(self, node: Optional[TreeNode], key: Any) -> Tuple[Optional[TreeNode], bool]:
        """
        Рекурсивное удаление элемента
        
        Args:
            node: Текущий узел
            key: Ключ для удаления
            
        Returns:
            Tuple[Optional[TreeNode], bool]: (Новый корень поддерева, был ли удален элемент)
        """
        if node is None:
            return None, False
        
        deleted = False
        
        # Поиск узла для удаления
        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
        else:
            # Нашли узел для удаления
            deleted = True
            
            # Случай 1: Нет детей или только один ребенок
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            
            # Случай 2: Есть оба ребенка
            # Находим минимальный узел в правом поддереве
            min_node = self._find_min(node.right)
            # Копируем его ключ и значение в текущий узел
            node.key = min_node.key
            node.value = min_node.value
            # Удаляем минимальный узел из правого поддерева
            node.right, _ = self._delete_recursive(node.right, min_node.key)
        
        # Обновление высоты
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))
        
        return node, deleted
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """
        Нахождение узла с минимальным ключом в поддереве
        
        Args:
            node: Корень поддерева
            
        Returns:
            TreeNode: Узел с минимальным ключом
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def height(self) -> int:
        """
        Получение высоты дерева
        
        Returns:
            int: Высота дерева (0 для пустого дерева)
        """
        return self._get_height(self.root)
    
    def _get_height(self, node: Optional[TreeNode]) -> int:
        """
        Получение высоты узла
        
        Args:
            node: Узел
            
        Returns:
            int: Высота узла (0 для None)
        """
        return node.height if node else 0
    
    def is_balanced(self) -> bool:
        """
        Проверка сбалансированности дерева
        
        Returns:
            bool: True если дерево сбалансировано, иначе False
        """
        return self._is_balanced_recursive(self.root)[0]
    
    def _is_balanced_recursive(self, node: Optional[TreeNode]) -> Tuple[bool, int]:
        """
        Рекурсивная проверка сбалансированности
        
        Args:
            node: Текущий узел
            
        Returns:
            Tuple[bool, int]: (Сбалансировано ли поддерево, высота поддерева)
        """
        if node is None:
            return True, 0
        
        # Проверка левого поддерева
        left_balanced, left_height = self._is_balanced_recursive(node.left)
        if not left_balanced:
            return False, 0
        
        # Проверка правого поддерева
        right_balanced, right_height = self._is_balanced_recursive(node.right)
        if not right_balanced:
            return False, 0
        
        # Проверка баланса текущего узла
        balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        
        return balanced, height
    
    def inorder_traversal(self) -> list:
        """
        Обход дерева in-order (для проверки)
        
        Returns:
            list: Список ключей в порядке возрастания
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[TreeNode], result: list) -> None:
        """Рекурсивный in-order обход"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def __len__(self) -> int:
        """Количество элементов в дереве"""
        return self.size
    
    def __repr__(self) -> str:
        """Строковое представление дерева"""
        return f"BinarySearchTree(size={self.size}, root={self.root.key if self.root else None})"
