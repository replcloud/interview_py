"""
let tree =
{
"value": "a",
"left": {
"value": "g",
"left": {
"value": "m",
"left": {
"value": "f",
"left": null,
"right": null
},
"right": {
"value": "c",
"left": null,
"right": null
}
},
"right": {
"value": "p",
"left": {
"value": "s",
"left": null,
"right": null
},
"right": {
"value": "r",
"left": null,
"right": null
}
}
},
"right": {
"value": "w",
"left": {
"value": "u",
"left": {
"value": "t",
"left": null,
"right": null
},
"right": {
"value": "o",
"left": null,
"right": null
}
},
"right": {
"value": "z",
"left": {
"value": "k",
"left": null,
"right": null
},
"right": {
"value": "x",
"left": null,
"right": null
}
}
}
}

/*

For this task, you will be given the elements of a perfect binary tree of characters,
 stored within a simple tree data structure.

Your goal is to write a function that starts at the root of the tree and
returns a counter clockwise traversal of the nodes at the edge of the tree.

1. Undrestanding
- i/outco
- constrains

2. Diagraming
-

3. psudocode
-
4. code



input:

            a
           /   \
         g       w
        / \     / \
       m   p   u    z
      / \ / \ / \  / \
     f  c s r t  o k  x

output: [a, g, m , f,  c, s, r, t,  o, k,  x, z, w ]

Input:
  a
 / \
c   b

Output: [a, c, b]


contrians:
- the edges of the tree
- characters (lowercase)
- pefect BT: A perfect binary tree is a tree where every non-leaf node has exactly two children,
 and all leaf nodes are at the same level


            a
           /   \
         g       w
        / \     / \
       m   p   u    z
      / \ / \ / \  / \
     f  c s r t  o k  x

Leftside;
add current value to the result | action
traverse to left | traverse


children:
If value is a child add it to result | action
traverse the tree | traverse


rightside
traverse to right | traverse
add current value to the result | action


*/

function traverseLeft(cur, res){
  // base case
  if(!cur.left){
    return res
  }
  // traversal
  res.push(cur.value)
  return traverseLeft(cur.left, res)
}

function traverseChildren(cur, res){
  if(!cur.left){
    res.push(cur.value)
    return res
  }
  traverseChildren(cur.left, res)
  traverseChildren(cur.right, res)
  return res
}


function traverseRight(cur, res){
    // base case
  if(!cur.right){
    return res
  }
  // traversal
  traverseRight(cur.right, res)
  res.push(cur.value)
  return res
}

function counterClockwise(tree){
  let result = []
  // result.push(...traverseLeft(tree.left, []))
  // result.push(...traverseChildren(tree, []))
  // result.push(...traverseRight(tree.right, []))
  function traverse(cur, leftMost, rightMost){
    // base case
    if(leftMost){
     result.push(cur.value)
    }

    if(!cur.left){
      result.push(cur.value)
      return
    }

    traverse(cur.left, leftMost, false)
    traverse(cur.right, false, rightMost)

    if(rightMost && !leftMost){
      result.push(cur.value)
    }
  }

  traverse(tree, true, true)

  return result

}

console.log(counterClockwise(tree))
"""