import matplotlib.pyplot as plt

def linegraph():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    plt.plot(x, x, label='x^2', color='pink', linestyle='--', linewidth=2, marker='.', markersize=10, markeredgecolor='purple')

    plt.plot(x, y, "b^--", label='x^2')

    plt.title("First graph!", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

    plt.xlabel('x')
    plt.ylabel('x^2')

    plt.xticks(x)
    plt.yticks(y)

    plt.legend()

    # plt.savefig('mygraph.png', dpi=1000)

    plt.show()


def bargraph():
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]

    bars = plt.bar(labels, values)

    patterns = ['/', 'o', '*']

    for bar in bars:
        bar.set_hatch(patterns.pop())
    
    # plt.savefig('mybargraph.png', dpi=1000)

    plt.show()


bargraph()