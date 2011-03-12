# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_peer', [dirname(__file__)])
        except ImportError:
            import _peer
            return _peer
        if fp is not None:
            try:
                _mod = imp.load_module('_peer', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _peer = swig_import_helper()
    del swig_import_helper
else:
    import _peer
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def getVerbose():
  return _peer.getVerbose()
getVerbose = _peer.getVerbose

def setVerbose(*args):
  return _peer.setVerbose(*args)
setVerbose = _peer.setVerbose

def logdet(*args):
  return _peer.logdet(*args)
logdet = _peer.logdet
class cWNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cWNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cWNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["E2S"] = _peer.cWNode_E2S_set
    __swig_getmethods__["E2S"] = _peer.cWNode_E2S_get
    if _newclass:E2S = _swig_property(_peer.cWNode_E2S_get, _peer.cWNode_E2S_set)
    __swig_setmethods__["Xprec"] = _peer.cWNode_Xprec_set
    __swig_getmethods__["Xprec"] = _peer.cWNode_Xprec_get
    if _newclass:Xprec = _swig_property(_peer.cWNode_Xprec_get, _peer.cWNode_Xprec_set)
    __swig_setmethods__["A_last"] = _peer.cWNode_A_last_set
    __swig_getmethods__["A_last"] = _peer.cWNode_A_last_get
    if _newclass:A_last = _swig_property(_peer.cWNode_A_last_get, _peer.cWNode_A_last_set)
    __swig_setmethods__["E_last"] = _peer.cWNode_E_last_set
    __swig_getmethods__["E_last"] = _peer.cWNode_E_last_get
    if _newclass:E_last = _swig_property(_peer.cWNode_E_last_get, _peer.cWNode_E_last_set)
    __swig_setmethods__["XE2S_last"] = _peer.cWNode_XE2S_last_set
    __swig_getmethods__["XE2S_last"] = _peer.cWNode_XE2S_last_get
    if _newclass:XE2S_last = _swig_property(_peer.cWNode_XE2S_last_get, _peer.cWNode_XE2S_last_set)
    __swig_setmethods__["lndetcovS"] = _peer.cWNode_lndetcovS_set
    __swig_getmethods__["lndetcovS"] = _peer.cWNode_lndetcovS_get
    if _newclass:lndetcovS = _swig_property(_peer.cWNode_lndetcovS_get, _peer.cWNode_lndetcovS_set)
    def __init__(self, *args): 
        this = _peer.new_cWNode(*args)
        try: self.this.append(this)
        except: self.this = this
    def update(self, *args): return _peer.cWNode_update(self, *args)
    def calcBound(self, *args): return _peer.cWNode_calcBound(self, *args)
    def entropy(self): return _peer.cWNode_entropy(self)
    def getE1(self): return _peer.cWNode_getE1(self)
    __swig_destroy__ = _peer.delete_cWNode
    __del__ = lambda self : None;
cWNode_swigregister = _peer.cWNode_swigregister
cWNode_swigregister(cWNode)

class cXNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cXNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cXNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["E2S"] = _peer.cXNode_E2S_set
    __swig_getmethods__["E2S"] = _peer.cXNode_E2S_get
    if _newclass:E2S = _swig_property(_peer.cXNode_E2S_get, _peer.cXNode_E2S_set)
    __swig_setmethods__["cov"] = _peer.cXNode_cov_set
    __swig_getmethods__["cov"] = _peer.cXNode_cov_get
    if _newclass:cov = _swig_property(_peer.cXNode_cov_get, _peer.cXNode_cov_set)
    __swig_setmethods__["prior_offset"] = _peer.cXNode_prior_offset_set
    __swig_getmethods__["prior_offset"] = _peer.cXNode_prior_offset_get
    if _newclass:prior_offset = _swig_property(_peer.cXNode_prior_offset_get, _peer.cXNode_prior_offset_set)
    __swig_setmethods__["prior_prec"] = _peer.cXNode_prior_prec_set
    __swig_getmethods__["prior_prec"] = _peer.cXNode_prior_prec_get
    if _newclass:prior_prec = _swig_property(_peer.cXNode_prior_prec_get, _peer.cXNode_prior_prec_set)
    def __init__(self, *args): 
        this = _peer.new_cXNode(*args)
        try: self.this.append(this)
        except: self.this = this
    def update(self, *args): return _peer.cXNode_update(self, *args)
    def calcBound(self, *args): return _peer.cXNode_calcBound(self, *args)
    def entropy(self): return _peer.cXNode_entropy(self)
    def getE1(self): return _peer.cXNode_getE1(self)
    __swig_destroy__ = _peer.delete_cXNode
    __del__ = lambda self : None;
cXNode_swigregister = _peer.cXNode_swigregister
cXNode_swigregister(cXNode)

class cAlphaNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cAlphaNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cAlphaNode, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _peer.new_cAlphaNode(*args)
        try: self.this.append(this)
        except: self.this = this
    def update(self, *args): return _peer.cAlphaNode_update(self, *args)
    def getE1(self): return _peer.cAlphaNode_getE1(self)
    __swig_destroy__ = _peer.delete_cAlphaNode
    __del__ = lambda self : None;
cAlphaNode_swigregister = _peer.cAlphaNode_swigregister
cAlphaNode_swigregister(cAlphaNode)

class cEpsNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cEpsNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cEpsNode, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _peer.new_cEpsNode(*args)
        try: self.this.append(this)
        except: self.this = this
    def update(self, *args): return _peer.cEpsNode_update(self, *args)
    def getE1(self): return _peer.cEpsNode_getE1(self)
    __swig_destroy__ = _peer.delete_cEpsNode
    __del__ = lambda self : None;
cEpsNode_swigregister = _peer.cEpsNode_swigregister
cEpsNode_swigregister(cEpsNode)

class cPhenoNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cPhenoNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cPhenoNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["E1"] = _peer.cPhenoNode_E1_set
    __swig_getmethods__["E1"] = _peer.cPhenoNode_E1_get
    if _newclass:E1 = _swig_property(_peer.cPhenoNode_E1_get, _peer.cPhenoNode_E1_set)
    __swig_setmethods__["E2"] = _peer.cPhenoNode_E2_set
    __swig_getmethods__["E2"] = _peer.cPhenoNode_E2_get
    if _newclass:E2 = _swig_property(_peer.cPhenoNode_E2_get, _peer.cPhenoNode_E2_set)
    def __init__(self, *args): 
        this = _peer.new_cPhenoNode(*args)
        try: self.this.append(this)
        except: self.this = this
    def getE1(self): return _peer.cPhenoNode_getE1(self)
    __swig_destroy__ = _peer.delete_cPhenoNode
    __del__ = lambda self : None;
cPhenoNode_swigregister = _peer.cPhenoNode_swigregister
cPhenoNode_swigregister(cPhenoNode)

PCA = _peer.PCA
class VBFA(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VBFA, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VBFA, name)
    __repr__ = _swig_repr
    __swig_setmethods__["W"] = _peer.VBFA_W_set
    __swig_getmethods__["W"] = _peer.VBFA_W_get
    if _newclass:W = _swig_property(_peer.VBFA_W_get, _peer.VBFA_W_set)
    __swig_setmethods__["X"] = _peer.VBFA_X_set
    __swig_getmethods__["X"] = _peer.VBFA_X_get
    if _newclass:X = _swig_property(_peer.VBFA_X_get, _peer.VBFA_X_set)
    __swig_setmethods__["Eps"] = _peer.VBFA_Eps_set
    __swig_getmethods__["Eps"] = _peer.VBFA_Eps_get
    if _newclass:Eps = _swig_property(_peer.VBFA_Eps_get, _peer.VBFA_Eps_set)
    __swig_setmethods__["Alpha"] = _peer.VBFA_Alpha_set
    __swig_getmethods__["Alpha"] = _peer.VBFA_Alpha_get
    if _newclass:Alpha = _swig_property(_peer.VBFA_Alpha_get, _peer.VBFA_Alpha_set)
    __swig_setmethods__["pheno"] = _peer.VBFA_pheno_set
    __swig_getmethods__["pheno"] = _peer.VBFA_pheno_get
    if _newclass:pheno = _swig_property(_peer.VBFA_pheno_get, _peer.VBFA_pheno_set)
    def __init__(self): 
        this = _peer.new_VBFA()
        try: self.this.append(this)
        except: self.this = this
    def getNj(self): return _peer.VBFA_getNj(self)
    def getNp(self): return _peer.VBFA_getNp(self)
    def getNk(self): return _peer.VBFA_getNk(self)
    def getNc(self): return _peer.VBFA_getNc(self)
    def getNmax_iterations(self): return _peer.VBFA_getNmax_iterations(self)
    def getTolerance(self): return _peer.VBFA_getTolerance(self)
    def getAdd_mean(self): return _peer.VBFA_getAdd_mean(self)
    def setNk(self, *args): return _peer.VBFA_setNk(self, *args)
    def setAdd_mean(self, *args): return _peer.VBFA_setAdd_mean(self, *args)
    def setNmax_iterations(self, *args): return _peer.VBFA_setNmax_iterations(self, *args)
    def setTolerance(self, *args): return _peer.VBFA_setTolerance(self, *args)
    def setPriorAlpha(self, *args): return _peer.VBFA_setPriorAlpha(self, *args)
    def setPriorEps(self, *args): return _peer.VBFA_setPriorEps(self, *args)
    def init_net(self): return _peer.VBFA_init_net(self)
    def calcBound(self): return _peer.VBFA_calcBound(self)
    def logprob(self): return _peer.VBFA_logprob(self)
    def update(self): return _peer.VBFA_update(self)
    def setPhenoMean(self, *args): return _peer.VBFA_setPhenoMean(self, *args)
    def setPhenoVar(self, *args): return _peer.VBFA_setPhenoVar(self, *args)
    def setCovariates(self, *args): return _peer.VBFA_setCovariates(self, *args)
    def getPhenoMean(self): return _peer.VBFA_getPhenoMean(self)
    def getPhenoVar(self): return _peer.VBFA_getPhenoVar(self)
    def getCovariates(self): return _peer.VBFA_getCovariates(self)
    def getX(self): return _peer.VBFA_getX(self)
    def getW(self): return _peer.VBFA_getW(self)
    def getEps(self): return _peer.VBFA_getEps(self)
    def getAlpha(self): return _peer.VBFA_getAlpha(self)
    def getResiduals(self): return _peer.VBFA_getResiduals(self)
    __swig_destroy__ = _peer.delete_VBFA
    __del__ = lambda self : None;
VBFA_swigregister = _peer.VBFA_swigregister
VBFA_swigregister(VBFA)



