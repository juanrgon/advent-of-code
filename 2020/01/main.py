import os.path


def main():
    print("Part 1 Solution: " + str(_part_1()))
    print("Part 2 Solution: " + str(_part_2()))


def _expenses():
    with open(os.path.join(os.path.abspath("."), "assets/expenses")) as f:
        return {int(amount) for amount in f.read().splitlines()}


def _find_pairs_product(expenses, target_sum):
    while expenses:
        expense = expenses.pop()
        matching_expense = target_sum - expense
        if matching_expense in expenses or (matching_expense == expense):
            return expense * matching_expense


def _part_1():
    return _find_pairs_product(expenses=_expenses(), target_sum=2020)


def _part_2():
    expenses = _expenses()
    while expenses:
        expense = expenses.pop()
        matching_expense = 2020 - expense

        product = _find_pairs_product(
            expenses=expenses.copy(), target_sum=matching_expense
        )
        if product is not None:
            return expense * product


if __name__ == "__main__":
    main()
