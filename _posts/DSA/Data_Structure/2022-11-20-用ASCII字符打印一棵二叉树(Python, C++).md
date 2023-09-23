---
categories: [DSA]
tags: Python Tree DSA C++
---



# 可视化(层序)

其实力扣为我们提供了一个树节点的可视化, 但是这个可视化并不好用, 如果题目要求我们生成一棵树, 那么出来的结果并不能被打印出来, 于是我们来看看在本地(根据一棵树的根节点)打印出整棵树. 这里参考了力扣的一道题目[655. 输出二叉树 - 力扣（LeetCode）](https://leetcode.cn/problems/print-binary-tree/), 相应修改后即为本程序. 

```python
def print_Tree():
    # m:层数
    # n:列数
    q = deque([root])
    m = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            # if not (cur.left or cur.right): continue
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        m += 1
    n = (1 << m) - 1
    ans = [[" "] * n for _ in range(m)]
    branch = [[" "] * n for _ in range(m)]
    bq = deque([[0, (n - 1) // 2, root, ""]])
    while bq:
        for _ in range(len(bq)):
            r, c, cur, slash = bq.popleft()
            if cur.val is None:
                continue
            ans[r][c] = str(cur.val)
            # 叶结点不能对斜杠/反斜杠进行移动
            if r == m - 1:
                branch[r][c] = slash
            else:
                if slash == "/":
                    branch[r][c + 1] = slash
                else:
                    branch[r][c - 1] = slash
            if cur.left:
                bq.append([r + 1, c - 2 ** (m - r - 2), cur.left, "/"])
            if cur.right:
                bq.append([r + 1, c + 2 ** (m - r - 2), cur.right, "\\"])

    for i in range(m):
        print("".join(branch[i]))
        print("".join(ans[i]))
```

针对一棵完整的二叉树, 其实可以在类里面写出来, 加上`self`即可, 下面的类可以参考我之前关于二叉树的文章:

```python
from collections import deque

# 首先定义树的根节点


class Node(object):
    """docstring for Node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 定义一棵二叉树
class BinaryTree(object):
    """docstring for BinaryTree"""

    def __init__(self):
        # 根节点
        self.root = None

    def add(self, item):
        node = Node(item)
        # 向树中插入元素, 使用队列存储元素, 读取与弹出
        if not self.root:
            self.root = node
            return
        # 用顺序表实现队列, 先入先出FIFO
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.val is None:
                continue
            # 若当前节点的左孩子为空, 将节点赋给当前节点左孩子
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def print_Tree(self):
        # m:层数
        # n:列数
        q = deque([self.root])
        m = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                # if not (cur.left or cur.right): continue
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            m += 1
        n = (1 << m) - 1
        ans = [[" "] * n for _ in range(m)]
        branch = [[" "] * n for _ in range(m)]
        bq = deque([[0, (n - 1) // 2, self.root, ""]])
        while bq:
            for _ in range(len(bq)):
                r, c, cur, slash = bq.popleft()
                if cur.val is None:
                    continue
                ans[r][c] = str(cur.val)
                # 叶结点不能对斜杠/反斜杠进行移动
                if r == m - 1:
                    branch[r][c] = slash
                else:
                    if slash == "/":
                        branch[r][c + 1] = slash
                    else:
                        branch[r][c - 1] = slash
                if cur.left:
                    bq.append([r + 1, c - 2 ** (m - r - 2), cur.left, "/"])
                if cur.right:
                    bq.append([r + 1, c + 2 ** (m - r - 2), cur.right, "\\"])

        for i in range(m):
            print("".join(branch[i]))
            print("".join(ans[i]))


```

下面来测试一下:

```python
if __name__ == "__main__":
    tree = BinaryTree()
    for i in range(25):
        tree.add(chr(97 + i))

    tree.print_Tree()
```

得到的结果如下:

```lua
               a               
        /             \        
       b               c       
    /     \         /     \    
   d       e       f       g   
  / \     / \     / \     / \  
 h   i   j   k   l   m   n   o 
/ \ / \ / \ / \ / \            
p q r s t u v w x y            
```

换成数字也可以(并且可以有空节点):

>   用力扣支持的数据`null`也可:

```python
if __name__ == "__main__":
    tree = BinaryTree()
    null=None
    for i in [1, null, 2, null, 3, 4, 5]:
        tree.add(i)

    tree.print_Tree()
```

结果:

```lua
       1       
          \    
           2   
            \  
             3 
            / \
            4 5
```



# C++版

```cpp
void BinaryTree::print_tree() {
    queue<TreeNode*> q;
    q.push(root);
    int m = 0;
    while (!q.empty()) {
        for (int i = 0; i < q.size(); i++) {
            auto cur = q.front();
            q.pop();
            if (cur->left) q.push(cur->left);
            if (cur->right) q.push(cur->right);
        }
        m++;
    }
    int n = (1 << m) - 1;
    vector<vector<string>> ans(m, vector<string>(n, " "));
    vector<vector<string>> branch(m, vector<string>(n, " "));
    queue<tuple<int, int, TreeNode*, string>> bq;
    bq.push({0, (n - 1) / 2, root, ""s});
    while (!bq.empty()) {
        for (int i = 0; i < bq.size(); i++) {
            auto& [r, c, cur, slash] = bq.front();
            bq.pop();
            if (!cur->val) continue;
            ans[r][c] = to_string(cur->val);
            if (r == m - 1) {
                branch[r][c] = slash;
            } else {
                if (slash == "/"s)
                    branch[r][c + 1] = slash;
                else
                    branch[r][c - 1] = slash;
            }
            if (cur->left)
                bq.push({r + 1, c - pow(2, m - r - 2), cur->left, "/"s});
            if (cur->right)
                bq.push({r + 1, c + pow(2, m - r - 2), cur->right, "\\"s});
        }
    }
    for (int i = 0; i < m; i++) {
        for (auto& s : branch[i]) cout << s;
        cout << endl;
        for (auto& s : ans[i]) cout << s;
        cout << endl;
    }
}
```





# 一些缺点

1.   对于两位数支持的不够好, 原因就是没有针对节点的大小作处理, 这个可以后续完善. 
2.   反斜杠有时候会出现不对齐的情况. 
3.   树节点数太多时候的换行问题. 
