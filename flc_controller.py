# flc_controller.py
# Simple fuzzy logic controller demo

def tri(x):
    return max(0, 1 - abs(x))

def flc_control(e, de):
    NL = lambda x: max(0, -x)
    PL = lambda x: max(0, x)
    ZE = lambda x: tri(x)

    e_set = {"NL": NL(e), "ZE": ZE(e), "PL": PL(e)}
    de_set = {"NL": NL(de), "ZE": ZE(de), "PL": PL(de)}

    rules = {
        ("NL","NL"):-1.0, ("NL","ZE"):-0.5,
        ("ZE","ZE"):0.0,
        ("PL","ZE"):0.5, ("PL","PL"):1.0
    }

    num, den = 0.0, 0.0
    for i in e_set:
        for j in de_set:
            w = e_set[i] * de_set[j]
            if (i,j) in rules:
                num += w * rules[(i,j)]
                den += w
    return num/den if den > 0 else 0.0

if __name__ == "__main__":
    print("FLC:", flc_control(-0.2, 0.1))
