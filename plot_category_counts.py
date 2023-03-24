import matplotlib.pyplot as plt


def plot_category_counts(category_counts):
    sorted_counts = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    categories = []
    counts = []
    for category, count in sorted_counts:
        if count >= 7:
            categories.append(category)
            counts.append(count)

    fig, ax = plt.subplots(figsize=(30, 6))  # Change the figsize parameter to adjust the width and height of the plot

    ax.bar(categories, counts)

    ax.set_xlabel('Categories')
    ax.set_ylabel('Counts')
    ax.set_title('Category Counts')

    plt.show()
