import matplotlib.pyplot as plt


def plot_category_counts(category_counts):
    categories = []
    counts = []
    for category, count in category_counts.items():
        if count >= 7:
            categories.append(category)
            counts.append(count)

    fig, ax = plt.subplots(figsize=(30, 6))  # Change the figsize parameter to adjust the width and height of the plot

    ax.bar(categories, counts)

    ax.set_xlabel('Categories')
    ax.set_ylabel('Counts')
    ax.set_title('Category Counts')

    plt.show()
