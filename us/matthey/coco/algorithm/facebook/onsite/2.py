"""
The input is a string which contains open and close parentheses. Find a minimum amount of parentheses that you need to add in order to balance the input string.

Examples:
Input: ((( Output: 3
Input: ()) Output: 1
Input: (()) Output: 0
Input: )( Output: 2


((( - 3
) - 1
- 0
) - 2

Rules:
# open - put into the stack
# close - look for matching, found pop, if not found, insert to the atack
"""
def minAmountParentheses(parentheses):
    # if parentheses is None or len is 0 default st[]
    lookup = {')': '('}
    st = []
    for p in parentheses:
        if p in lookup: # p is is a close parenthese
            if len(st) == 0:
                st.append(p)
            else:
                if st[-1] == lookup[p]: # found matching
                    st.pop()
                else: # matching not found
                    st.append(p)
        else: # p is is a open parenthese
            st.append(p)
    return len(st)


"""
1 - ) st = [)]
2 - ( st = [)(]


None 

"""

"""
// Given a binary tree, find the maximum path sum.
// A path is defined as any sequence of nodes from some starting node to any node
// in the tree along the parent-child connections. 

// Example
// Given the below binary tree,
//     1
//    / \
//   2   6
//  /   / \
// 4  -3   5
// return 18

//     1
//    / \
//   2   6
//  /   / \
// 4  -3  -5
// return 13
"""

path = [1, 2, 4, 6, -3, 5]


def helper(node):
    if not node: return 0
    maxLSum = helper(node.left)
    maxRSum = helper(node.left)
    if max(maxLSum, maxLSum) > 0:
        return node.val + max(maxLSum, maxLSum)
    else:
        return node.val
