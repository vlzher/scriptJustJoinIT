from count_div_occurrences import count_div_occurrences
from plot_category_counts import plot_category_counts
from scrape_urls import scrape_urls

if __name__ == '__main__':
    my_tuple = tuple(scrape_urls())
    counts = count_div_occurrences(my_tuple)
    plot_category_counts(counts)




