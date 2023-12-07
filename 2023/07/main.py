import aoc
from collections import Counter

playing_card_ranks_1 = "".join(("23456789TJQKA"))
playing_card_ranks_2 = "".join(("J23456789TQKA"))


@aoc.solution(1)
def part_1(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    hand_sets_to_bids = {}

    scores = {}
    for play in strs:
        hand, bid = play.split(" ")
        hand_sets_to_bids[hand] = int(bid)
        scores.setdefault(key(hand)[0], []).append(hand)

    best_hands = []
    for r in sorted(scores.keys()):
        for hand in sorted(scores[r], key=key):
            best_hands.append(hand)

    sum = 0
    for i, hand in enumerate(best_hands):
        bid = hand_sets_to_bids[hand]
        sum = sum + bid * (i + 1)

    return sum


@aoc.solution(2)
def part_2(
    raw: aoc.String,
    ints: aoc.Integers,
    strs: list[aoc.String],
    paragraphs: list[aoc.Paragraph],
):
    hand_sets_to_bids = {}

    scores = {}
    for play in strs:
        hand, bid = play.split(" ")
        hand_sets_to_bids[hand] = int(bid)
        scores.setdefault(key_2(hand)[0], []).append(hand)

    best_hands = []
    for r in sorted(scores.keys()):
        for hand in sorted(scores[r], key=key_2):
            best_hands.append(hand)

    sum = 0
    for i, hand in enumerate(best_hands):
        bid = hand_sets_to_bids[hand]
        sum = sum + bid * (i + 1)

    return sum


def key(hand: str):
    counts = Counter(card[0] for card in hand)

    # five of a kind
    if 5 in counts.values():
        return 6, [playing_card_ranks_1.index(c) for c in hand]

    # four of a kind
    if 4 in counts.values():
        return 5, [playing_card_ranks_1.index(c) for c in hand]

    # full house
    if 3 in counts.values() and 2 in counts.values():
        return 4, [playing_card_ranks_1.index(c) for c in hand]

    # three of a kind
    if 3 in counts.values():
        return 3, [playing_card_ranks_1.index(c) for c in hand]

    # two pair
    if len(counts) == 3:
        return 2, [playing_card_ranks_1.index(c) for c in hand]

    # one pair
    if len(counts) == 4:
        return 1, [playing_card_ranks_1.index(c) for c in hand]

    # high card
    if len(counts) == 5:
        return 0, [playing_card_ranks_1.index(c) for c in hand]

    return 0, 0


def key_2(hand: str):
    counts = Counter(card[0] for card in hand)

    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

    # five of a kind
    if 5 in counts.values():
        return FIVE_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

    # four of a kind
    if 4 in counts.values():
        if (counts["J"] == 4):
            return FIVE_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        if (counts["J"] == 1):
            return FIVE_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        return FOUR_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

    # full house
    if 3 in counts.values() and 2 in counts.values():
        if (counts["J"] == 3):
            return FIVE_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        if (counts["J"] == 2):
            return FIVE_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        return FULL_HOUSE, [playing_card_ranks_2.index(c) for c in hand]

    # three of a kind
    if 3 in counts.values():
        if (counts["J"] == 3):
            return FOUR_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        if (counts["J"] == 1):
            return FOUR_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        return 3, [playing_card_ranks_2.index(c) for c in hand]

    # two pair
    if len(counts) == 3:
        if (counts["J"] == 2):
            return FOUR_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        if (counts["J"] == 1):
            return FULL_HOUSE, [playing_card_ranks_2.index(c) for c in hand]

        return TWO_PAIR, [playing_card_ranks_2.index(c) for c in hand]

    # one pair
    if len(counts) == 4:
        if (counts["J"] == 2):
            return THREE_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        if (counts["J"] == 1):
            return THREE_OF_A_KIND, [playing_card_ranks_2.index(c) for c in hand]

        return ONE_PAIR, [playing_card_ranks_2.index(c) for c in hand]

    # high card
    if len(counts) == 5:
        if (counts["J"] == 1):
            return ONE_PAIR, [playing_card_ranks_2.index(c) for c in hand]

        return HIGH_CARD, [playing_card_ranks_2.index(c) for c in hand]

    return HIGH_CARD, 0


if __name__ == "__main__":
    print("Part 1:", part_1(__file__))
    print("Part 2:", part_2(__file__))
