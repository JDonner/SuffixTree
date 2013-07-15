# This file was created automatically by SWIG.
import SuffixTreec
class SuffixTree:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,SuffixTree):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = SuffixTree.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = SuffixTree.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["tree"] = SuffixTreec.SuffixTree_tree_set
    __getmethods__["tree"] = SuffixTreec.SuffixTree_tree_get
    def __init__(self,*args):
        self.this = apply(SuffixTreec.new_SuffixTree,args)
        self.thisown = 1
    def __del__(self,SuffixTreec=SuffixTreec):
        if getattr(self,'thisown',0):
            SuffixTreec.delete_SuffixTree(self)
    def add(*args): return apply(SuffixTreec.SuffixTree_add,args)
    def num_nodes(*args): return apply(SuffixTreec.SuffixTree_num_nodes,args)
    def root(*args): return apply(SuffixTreec.SuffixTree_root,args)
    def match(*args): return apply(SuffixTreec.SuffixTree_match,args)
    def __repr__(self):
        return "<C SuffixTree instance at %s>" % (self.this,)

class SuffixTreePtr(SuffixTree):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = SuffixTree
SuffixTreec.SuffixTree_swigregister(SuffixTreePtr)
class SuffixNode:
    __setmethods__ = {}
    for _s in []: __setmethods__.update(_s.__setmethods__)
    def __setattr__(self,name,value):
        if (name == "this"):
            if isinstance(value,SuffixNode):
                self.__dict__[name] = value.this
                if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
                del value.thisown
                return
        method = SuffixNode.__setmethods__.get(name,None)
        if method: return method(self,value)
        self.__dict__[name] = value

    __getmethods__ = {}
    for _s in []: __getmethods__.update(_s.__getmethods__)
    def __getattr__(self,name):
        method = SuffixNode.__getmethods__.get(name,None)
        if method: return method(self)
        raise AttributeError,name

    __setmethods__["tree"] = SuffixTreec.SuffixNode_tree_set
    __getmethods__["tree"] = SuffixTreec.SuffixNode_tree_get
    __setmethods__["node"] = SuffixTreec.SuffixNode_node_set
    __getmethods__["node"] = SuffixTreec.SuffixNode_node_get
    def __del__(self,SuffixTreec=SuffixTreec):
        if getattr(self,'thisown',0):
            SuffixTreec.delete_SuffixNode(self)
    def num_children(*args): return apply(SuffixTreec.SuffixNode_num_children,args)
    def find_child(*args): return apply(SuffixTreec.SuffixNode_find_child,args)
    def children(*args): return apply(SuffixTreec.SuffixNode_children,args)
    def next(*args): return apply(SuffixTreec.SuffixNode_next,args)
    def parent(*args): return apply(SuffixTreec.SuffixNode_parent,args)
    def suffix_link(*args): return apply(SuffixTreec.SuffixNode_suffix_link,args)
    def edgelen(*args): return apply(SuffixTreec.SuffixNode_edgelen,args)
    def edgestr(*args): return apply(SuffixTreec.SuffixNode_edgestr,args)
    def getch(*args): return apply(SuffixTreec.SuffixNode_getch,args)
    def labellen(*args): return apply(SuffixTreec.SuffixNode_labellen,args)
    def labelstr(*args): return apply(SuffixTreec.SuffixNode_labelstr,args)
    def ident(*args): return apply(SuffixTreec.SuffixNode_ident,args)
    def num_leaves(*args): return apply(SuffixTreec.SuffixNode_num_leaves,args)
    def leaf(*args): return apply(SuffixTreec.SuffixNode_leaf,args)
    def __init__(self,*args):
        self.this = apply(SuffixTreec.new_SuffixNode,args)
        self.thisown = 1
    def __repr__(self):
        return "<C SuffixNode instance at %s>" % (self.this,)

class SuffixNodePtr(SuffixNode):
    def __init__(self,this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = SuffixNode
SuffixTreec.SuffixNode_swigregister(SuffixNodePtr)
MAXNUMNODES = SuffixTreec.MAXNUMNODES
MAXALPHA = SuffixTreec.MAXALPHA
STREE_DNA = SuffixTreec.STREE_DNA
STREE_RNA = SuffixTreec.STREE_RNA
STREE_PROTEIN = SuffixTreec.STREE_PROTEIN
STREE_ASCII = SuffixTreec.STREE_ASCII

