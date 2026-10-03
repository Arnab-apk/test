def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def search(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    for val in values[1:]:
        insert(root, val)
    return root

def print_tree(root, level=0):
    indent = "  " * level
    if root:
        print(f"{indent}{root.val}")
        print_tree(root.left, level + 1)
        print_tree(root.right, level + 1)

def delete_min(root):
    if root:
        if root.left:
            root.val = delete_min(root.left)
        else:
            root.val = root.left.val
            root.left = None
    return root

def delete_max(root):
    if root:
        if root.right:
            root.val = delete_max(root.right)
        else:
            root.val = root.right.val
            root.right = None
    return root

def delete_val(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = delete_val(root.left, val)
    elif val > root.val:
        root.right = delete_val(root.right, val)
    else:
        if root.left and root.right:
            return None
        elif root.left:
            root.val = root.left.val
            root.left = delete_val(root.left, val)
        else:
            root.val = root.right.val
            root.right = delete_val(root.right, val)
    return root

def delete_all(root, values):
    if not values:
        return root
    if root is None:
        return None
    if root.val in values:
        root = delete_val(root, root.val)
    else:
        root.left = delete_all(root.left, values)
        root.right = delete_all(root.right, values)
    return root

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)

def is_sorted(root):
    if root is None:
        return True
    return is_sorted(root.left) and is_sorted(root.right) and root.val >= root.left.val and root.val <= root.right.val

def is_sorted_desc(root):
    if root is None:
        return True
    return is_sorted_desc(root.left) and is_sorted_desc(root.right) and root.val <= root.left.val and root.val >= root.right.val

def is_sorted_desc(root):
    if root is None:
        return True
    return is_sorted_desc(root.left) and is_sorted_desc(root.right) and root.val <= root.left.val and root.val >= root.right.val

def is_sorted_desc(root):
    if root is None:
        return True
    return is_sorted_desc(root.left) and is_sorted_desc(root.right) and root.val <= root.left.val and root.val >= root.right.val
