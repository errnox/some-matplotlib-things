import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker


def bezier_point(x0, y0, x1, y1, x2, y2, x3, y3, t):
    x01 = x0 + t*(x1 - x0);
    y01 = y0 + t*(y1 - y0);
    x12 = x1 + t*(x2 - x1);
    y12 = y1 + t*(y2 - y1);
    x23 = x2 + t*(x3 - x2);
    y23 = y2 + t*(y3 - y2);

    x012 = x01 + t*(x12 - x01);
    y012 = y01 + t*(y12 - y01);
    x123 = x12 + t*(x23 - x12);
    y123 = y12 + t*(y23 - y12);

    return (x012 + t*(x123 - x012), y012 + t*(y123 - y012))


def bezier(x0, y0, x1, y1, x2, y2, x3, y3, t):
    points = []
    for i in range(t):
        points.append(bezier_point(x0, y0, x1, y1, x2, y2, x3, y3, i))
    return points


def plot(data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([point[0] for point in data] , [point[1] for point in data], 'o-')
    fig.autofmt_xdate()
    plt.show()


if __name__ == '__main__':
    def test_single():
        data = bezier(100, 100,
                      10, 20,
                      500, 5,
                      600, 50,
                      50)
        plot(data)

    def test_multiple():
        for i in range(10):
            data = bezier(100 + i * 100, 100,
                          10, 20,
                          500, 5,
                          600, 50,
                          50)
            plot(data)

    # Toggle
    #
    # test_single()
    # test_multiple()

    data = []
    for i in range(100):
        data.append((i * i, i * i / 2 - i ** 3))
    plot(data)
