import unittest
from binary_tree import BinaryTree

# EJERCICIO 1
class Node(unittest.TestCase):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        nuevo_nodo = Node(data)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo_nodo

    def buscar(self, data):
        actual = self.head
        while actual is not None:
            if actual.data == data:
                return True
            actual = actual.next
        return False

    def borrar(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        actual = self.head
        while actual.next is not None:
            if actual.next.data == data:
                actual.next = actual.next.next
                return
            actual = actual.next

    def listar(self):
        lista_datos = []
        actual = self.head
        while actual is not None:
            lista_datos.append(actual.data)
            actual = actual.next
        return lista_datos


lista = LinkedList()

lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.agregar(40)

resultado = lista.buscar(20)
print(resultado)

lista.borrar(30)

datos = lista.listar()
print(datos)


# EJERCICIO 2
class Node(unittest.TestCase):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def agregar(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._agregar_recursivo(data, self.root)

    def _agregar_recursivo(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._agregar_recursivo(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._agregar_recursivo(data, current_node.right)

    def buscar(self, data):
        return self._buscar_recursivo(data, self.root)

    def _buscar_recursivo(self, data, current_node):
        if current_node is None:
            return False
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._buscar_recursivo(data, current_node.left)
        else:
            return self._buscar_recursivo(data, current_node.right)

    def borrar(self, data):
        self.root = self._borrar_recursivo(data, self.root)

    def _borrar_recursivo(self, data, current_node):
        if current_node is None:
            return current_node
        if data < current_node.data:
            current_node.left = self._borrar_recursivo(data, current_node.left)
        elif data > current_node.data:
            current_node.right = self._borrar_recursivo(
                data, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                min_node = self._encontrar_minimo(current_node.right)
                current_node.data = min_node.data
                current_node.right = self._borrar_recursivo(
                    min_node.data, current_node.right)
        return current_node

    def _encontrar_minimo(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def listar(self):
        lista_datos = []
        self._listar_recursivo(self.root, lista_datos)
        return lista_datos

    def _listar_recursivo(self, current_node, lista_datos):
        if current_node is not None:
            self._listar_recursivo(current_node.left, lista_datos)
            lista_datos.append(current_node.data)
            self._listar_recursivo(current_node.right, lista_datos)
            
# EJERCICIO 3

# Test Linked List

# Test BinaryTree
class BinaryTreeTests(unittest.TestCase):
    def test_agregar(self):
        tree = BinaryTree()
        tree.agregar(2)
        tree.agregar(1)
        self.assertEqual(tree.listar(), [1, 2])

    def test_buscar(self):
        tree = BinaryTree()
        tree.agregar(2)
        self.assertTrue(tree.buscar(2))
        self.assertFalse(tree.buscar(9))

    def test_borrar(self):
        tree = BinaryTree()
        tree.agregar(5)
        tree.agregar(2)
        tree.agregar(7)
        tree.borrar(2)
        self.assertEqual(tree.listar(), [5, 7])

    def test_listar(self):
        tree = BinaryTree()
        tree.agregar(5)
        tree.agregar(2)
        tree.agregar(7)
        self.assertEqual(tree.listar(), [ 2, 5, 7])

if __name__ == '__main__':
    unittest.main()