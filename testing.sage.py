

# This file was *autogenerated* from the file testing.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_50 = Integer(50); _sage_const_11 = Integer(11); _sage_const_1 = Integer(1); _sage_const_1p1 = RealNumber('1.1'); _sage_const_35 = Integer(35); _sage_const_36 = Integer(36); _sage_const_0 = Integer(0); _sage_const_51 = Integer(51); _sage_const_4 = Integer(4)
from deuring import *
from special_extremal import *
from quaternions import *

def TestSpecialExtremal():
    p = _sage_const_2 **_sage_const_50 *_sage_const_11  - _sage_const_1 
    O0 = SpecialExtremalOrder(p, _sage_const_1 )
    N = randint(floor(p**_sage_const_1p1 ), ceil(_sage_const_2 *p**_sage_const_1p1 ))
    gamma = O0.FullRepresentInteger(N)
    assert gamma
    assert gamma.reduced_norm() == N
    print("TestSpecialExtremal passed!")

def TestFixedDegreeIsogeny():
    p = _sage_const_2 **_sage_const_50 *_sage_const_11  - _sage_const_1 
    ctx = Deuring2D(p)

    u = randint(_sage_const_2 **_sage_const_35 , _sage_const_2 **_sage_const_36 )
    while u%_sage_const_2  == _sage_const_0 :
        u = randint(_sage_const_2 **_sage_const_35 , _sage_const_2 **_sage_const_36 )
    Phi, imP, imQ = ctx.FixedDegreeIsogeny(u)
    print(Phi.codomain()[_sage_const_0 ])
    print(Phi.codomain()[_sage_const_0 ].j_invariant())
    print(Phi.codomain()[_sage_const_1 ])
    print(Phi.codomain()[_sage_const_1 ].j_invariant())

def TestIdealToIsogeny():
    p = _sage_const_2 **_sage_const_50 *_sage_const_11  - _sage_const_1 
    ctx = Deuring2D(p)
    l = next_prime(randint(_sage_const_2 **_sage_const_50 , _sage_const_2 **_sage_const_51 ))
    ll = next_prime(l)
    while not (ll % _sage_const_4  == l % _sage_const_4  == _sage_const_1 ):
        l = next_prime(randint(_sage_const_2 **_sage_const_50 , _sage_const_2 **_sage_const_51 ))
        ll = next_prime(l)
    alpha = ctx.O0.FullRepresentInteger(l*ll)
    I = ctx.O0.order * l + ctx.O0.order * alpha
    print(SuccessiveMinima(I.right_order()))
    print(SuccessiveMinima(I.left_order()))
    E_I, phi_IP, phi_IQ = ctx.IdealToIsogeny(I)

    print(E_I)
    print(E_I.j_invariant())

if __name__=="__main__":
    #TestSpecialExtremal()
    TestFixedDegreeIsogeny()
    TestIdealToIsogeny()

