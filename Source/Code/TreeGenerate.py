import nltk as nltk
from nltk.draw.tree import draw_trees
from nltk import tree, treetransforms
from copy import deepcopy

s="if"
s="("+s+")"
print(s)

treeS = nltk.Tree.fromstring(s)

treeFactor = nltk.Tree.fromstring("(factor number)")
treeAssign = nltk.Tree.fromstring("(assign-stmt ID := number)")
treeStatement= nltk.Tree.fromstring("(statement)")
treeStmtseq=nltk.Tree.fromstring("(stmt-seq)")
treeIf = nltk.Tree.fromstring("(if-stmt if number then end)")
treeStatement1 = nltk.Tree.fromstring("(statement)")
treeStmtseq1=nltk.Tree.fromstring("(stmt-seq)")

treeAssign.insert(2,treeFactor)
treeStatement.insert(0,treeAssign)
treeStmtseq.insert(0,treeStatement)
treeIf.insert(3,treeStmtseq)
treeStatement1.insert(0,treeIf)
treeStmtseq1.insert(0,treeStatement1)


draw_trees(treeS)
