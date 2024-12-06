import aoc


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    page_rules, pages_updates = raw.split("\n\n")

    # Parse rules into a set of tuples for easier lookup
    rules = set()
    for line in page_rules.splitlines():
        before, after = line.split("|")
        rules.add((before, after))

    # Parse updates
    updates = [line.split(",") for line in pages_updates.splitlines()]

    total = 0
    for update in updates:
        valid = True
        # Check each pair of pages in the current order
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                page1, page2 = update[i], update[j]
                # If there's a rule saying page2 should come before page1, the order is invalid
                if (page2, page1) in rules:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            # Get middle page number for valid updates
            middle_index = len(update) // 2
            total += int(update[middle_index])

    return total


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    page_rules, pages_updates = raw.split("\n\n")

    # Parse updates
    updates = [line.split(",") for line in pages_updates.splitlines()]

    # Parse rules into a dict for graph representation
    graph = {}
    in_degree = {}

    def add_to_graph(page):
        if page not in graph:
            graph[page] = set()
            in_degree[page] = 0

    # Build graph from rules
    for line in page_rules.splitlines():
        before, after = line.split("|")
        add_to_graph(before)
        add_to_graph(after)
        graph[before].add(after)
        in_degree[after] = in_degree.get(after, 0) + 1



    def topological_sort(pages):
        # Create local copy of in-degree for these specific pages
        local_in_degree = {page: 0 for page in pages}
        local_graph = {page: set() for page in pages}

        # Build local graph with only the pages we care about
        for page1 in pages:
            for page2 in graph[page1]:
                if page2 in pages:
                    local_graph[page1].add(page2)
                    local_in_degree[page2] += 1

        # Find all vertices with 0 in-degree
        queue = [page for page in pages if local_in_degree[page] == 0]
        result = []

        while queue:
            page = queue.pop(0)
            result.append(page)

            for neighbor in local_graph[page]:
                local_in_degree[neighbor] -= 1
                if local_in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result

    def is_valid_order(update):
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                page1, page2 = update[i], update[j]
                if (page2, page1) in rules:
                    return False
        return True

    # Process only invalid updates
    total = 0
    rules = set((before, after) for line in page_rules.splitlines() for before, after in [line.split("|")])

    for update in updates:
        if not is_valid_order(update):
            # Sort the pages and get the middle number
            sorted_update = topological_sort(update)
            middle_index = len(sorted_update) // 2
            total += int(sorted_update[middle_index])

    return total


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
