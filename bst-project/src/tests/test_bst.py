import pytest
from src.bst import BinarySearchTree
from src.tree_node import TreeNode


class TestBinarySearchTree:
    """Тесты для класса BinarySearchTree"""
    
    def setup_method(self):
        """Подготовка перед каждым тестом"""
        self.bst = BinarySearchTree()
    
    def test_insert_and_search(self):
        """Тест вставки и поиска"""
        # Вставка элементов
        self.bst.insert(5, "five")
        self.bst.insert(3, "three")
        self.bst.insert(7, "seven")
        self.bst.insert(1, "one")
        
        # Проверка поиска
        assert self.bst.search(5) == "five"
        assert self.bst.search(3) == "three"
        assert self.bst.search(7) == "seven"
        assert self.bst.search(1) == "one"
        assert self.bst.search(10) is None
        
        # Проверка размера
        assert len(self.bst) == 4
    
    def test_insert_duplicate(self):
        """Тест вставки дублирующегося ключа"""
        self.bst.insert(5, "five")
        self.bst.insert(5, "new_five")
        
        assert self.bst.search(5) == "new_five"
        assert len(self.bst) == 1  # размер не должен увеличиться
    
    def test_delete_leaf_node(self):
        """Тест удаления листового узла"""
        self.bst.insert(5, "five")
        self.bst.insert(3, "three")
        self.bst.insert(7, "seven")
        
        assert self.bst.delete(3) == True
        assert self.bst.search(3) is None
        assert len(self.bst) == 2
        assert self.bst.inorder_traversal() == [5, 7]
    
    def test_delete_node_with_one_child(self):
        """Тест удаления узла с одним ребенком"""
        self.bst.insert(5, "five")
        self.bst.insert(3, "three")
        self.bst.insert(2, "two")  # левый ребенок от 3
        
        assert self.bst.delete(3) == True
        assert self.bst.search(3) is None
        assert len(self.bst) == 2
        assert self.bst.inorder_traversal() == [2, 5]
    
    def test_delete_node_with_two_children(self):
        """Тест удаления узла с двумя детьми"""
        self.bst.insert(5, "five")
        self.bst.insert(3, "three")
        self.bst.insert(7, "seven")
        self.bst.insert(2, "two")
        self.bst.insert(4, "four")
        
        assert self.bst.delete(3) == True
        assert self.bst.search(3) is None
        assert len(self.bst) == 4
        assert self.bst.inorder_traversal() == [2, 4, 5, 7]
    
    def test_delete_nonexistent(self):
        """Тест удаления несуществующего ключа"""
        self.bst.insert(5, "five")
        
        assert self.bst.delete(10) == False
        assert len(self.bst) == 1
    
    def test_height_empty_tree(self):
        """Тест высоты пустого дерева"""
        assert self.bst.height() == 0
    
    def test_height_single_node(self):
        """Тест высоты дерева с одним узлом"""
        self.bst.insert(5, "five")
        assert self.bst.height() == 1
    
    def test_height_balanced_tree(self):
        """Тест высоты сбалансированного дерева"""
        self.bst.insert(5, "five")
        self.bst.insert(3, "three")
        self.bst.insert(7, "seven")
        self.bst.insert(2, "two")
        self.bst.insert(4, "four")
        
        assert self.bst.height() == 3
    
    def test_is_balanced_empty(self):
        """Тест сбалансированности пустого дерева"""
        assert self.bst.is_balanced() == True
    
    def test_is_balanced_single(self):
        """Тест сбалансированности дерева с одним узлом"""
        self.bst.insert(5, "five")
        assert self.bst.is_balanced() == True
    
    def test_is_balanced_balanced_tree(self):
        """Тест сбалансированности сбалансированного дерева"""
        self.bst.insert(5, "five")
        self.bst.insert(3, "three")
        self.bst.insert(7, "seven")
        self.bst.insert(2, "two")
        self.bst.insert(4, "four")
        
        assert self.bst.is_balanced() == True
    
    def test_is_balanced_unbalanced_tree(self):
        """Тест сбалансированности несбалансированного дерева"""
        self.bst.insert(5, "five")
        self.bst.insert(4, "four")
        self.bst.insert(3, "three")
        self.bst.insert(2, "two")
        self.bst.insert(1, "one")
        
        assert self.bst.is_balanced() == False
    
    def test_complex_operations(self):
        """Тест комплексных операций"""
        # Вставка элементов
        values = [50, 30, 70, 20, 40, 60, 80]
        for v in values:
            self.bst.insert(v, str(v))
        
        assert len(self.bst) == 7
        assert self.bst.is_balanced() == True
        
        # Удаление элементов
        self.bst.delete(20)
        self.bst.delete(30)
        
        assert len(self.bst) == 5
        assert self.bst.inorder_traversal() == [40, 50, 60, 70, 80]
        
        # Проверка сбалансированности после удалений
        assert self.bst.is_balanced() == True
