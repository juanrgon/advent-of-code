from pathlib import Path


def main():
    print("Part 1 Solution:", _part_1())
    print("Part 2 Solution:", _part_2())


def _expenses():
    return {
        int(amount)
        for index, amount in enumerate(
            (Path().absolute() / "assets/expenses").read_text().splitlines()
        )
    }


def _find_pairs_product(*, expenses, target_sum):
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
