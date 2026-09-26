from check import legal_source, solve_source, valid_source, legal_target, solve_target, valid_target


def test_hand_cases():
    k4 = {"vertices":4,"edges":[[u,v] for u in range(4) for v in range(u+1,4)]}
    assert valid_source(k4,{"side":[False,False,True,True]})
    k5 = {"vertices":5,"edges":[[u,v] for u in range(5) for v in range(u+1,5)]}
    assert solve_source(k5) == {"status":"NO-SOLUTION"}
    assert not valid_source(k5,{"side":[False]*4+[True]})
    path6 = {"vertices":6,"edges":[[i,i+1] for i in range(5)]}
    assert legal_source(path6)
    assert not legal_target(path6)
    assert not legal_source({"vertices":2,"edges":[]})
    assert "side" in solve_target(k4)
    assert not valid_target(k4,{"side":[False]*4})


if __name__ == "__main__":
    test_hand_cases()
