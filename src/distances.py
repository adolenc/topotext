import dionysus

def bottleneck_distance(dia1, dia2):
    return dionysus.bottleneck_distance(dia1, dia2)

def wasserstein_distance(dia1, dia2, p=1):
    return dionysus.wasserstein_distance(dia1, dia2, p)

if __name__ == '__main__':
    d1 = dionysus.PersistenceDiagram(1)
    d1.append((1,4))
    d1.append((2,5))
    d1.append((1,6))
    d1.append((4,5))
    d1.append((3,7))

    d2 = dionysus.PersistenceDiagram(1)
    d2.append((1,3))
    d2.append((1,5))
    d2.append((2,6))
    d2.append((4,5))
    d2.append((6,7))

    print bottleneck_distance(d1, d2)
    print wasserstein_distance(d1,d2)