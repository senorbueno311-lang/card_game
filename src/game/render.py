

def render_ascii_card(card):
    """Return a single card as a list of text lines."""
    rank = card.rank
    suit = card.suit

    top_left = f"{rank}{suit}"
    bottom_right = f"{suit}{rank}"

    # Pad to width 7
    top_left = top_left.ljust(7)
    bottom_right = bottom_right.rjust(7)

    return [
        "┌───────┐",
        f"│{top_left}│",
        "│       │",
        f"│{bottom_right}│",
        "└───────┘"
    ]


def render_ascii_table(cards, per_row=5):
    """Render multiple cards in a grid."""
    rows = []
    for i in range(0, len(cards), per_row):
        chunk = cards[i:i+per_row]

        # Convert each card to its ASCII block
        ascii_blocks = [render_ascii_card(c) for c in chunk]

        # Combine line-by-line
        for line_idx in range(len(ascii_blocks[0])):
            row_line = "  ".join(block[line_idx] for block in ascii_blocks)
            rows.append(row_line)

        rows.append("")  # blank line between rows

    print("\n".join(rows))
