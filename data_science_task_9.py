def sort_dict_by_keys(dict_):
    sorted_keys = list(dict_.keys())
    sorted_keys.sort()
    return {i: dict_[i] for i in sorted_keys}


def calc_distribution(queries):
    queries_count = len(queries)

    counts = {}
    for query in queries:
        key = len(query.split(' '))
        if key not in counts:
            counts[key] = 0
        counts[key] += 1

    queries_distributions = {}
    for i, (key, value) in enumerate(counts.items()):
        queries_distributions[f"{key} words"] = int((value/queries_count)*100)

    queries_distributions = sort_dict_by_keys(queries_distributions)

    for i, (key, value) in enumerate(queries_distributions.items()):
        print(f"{key}: {value}%")

    return queries_distributions


search_queries = [
    "watch new movies",
    "coffee near me",
    "how to find the determinant",
    "python",
    "data science jobs in UK",
    "courses for data science",
    "taxi",
    "google",
    "yandex",
    "bing",
    "foreign exchange rates USD/BYN",
    "Netflix movies watch online free",
    "Statistics courses online from top universities"
]

calc_distribution(search_queries)
