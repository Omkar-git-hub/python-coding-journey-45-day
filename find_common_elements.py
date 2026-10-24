def find_common_elements(list1, list2):
    """
    Return a list containing the common elements between list1 and list2.

    The order of elements in the returned list follows their first occurrence
    in list1. Duplicate common elements are omitted; each common element appears
    at most once in the result.

    Parameters
    ----------
    list1 : list
        First list of elements.
    list2 : list
        Second list of elements.

    Returns
    -------
    list
        List of common elements.
    """
    # Convert the second list to a set for O(1) look‑ups.
    set2 = set(list2)
    seen = set()
    common = []
    for item in list1:
        if item in set2 and item not in seen:
            common.append(item)
            seen.add(item)
    return common


if __name__ == "__main__":
    # Expect two lines of input, each representing a list.
    # Elements are space‑separated. They are parsed as integers if possible,
    # otherwise left as strings.
    import sys

    def parse_line(line):
        parts = line.strip().split()
        parsed = []
        for p in parts:
            try:
                parsed.append(int(p))
            except ValueError:
                try:
                    parsed.append(float(p))
                except ValueError:
                    parsed.append(p)
        return parsed

    if sys.stdin.isatty():
        # Interactive mode: prompt the user.
        line1 = input("Enter elements of the first list (space separated): ")
        line2 = input("Enter elements of the second list (space separated): ")
    else:
        # Non‑interactive: read two lines from stdin.
        lines = sys.stdin.read().splitlines()
        if len(lines) < 2:
            raise ValueError("Two lines of input are required.")
        line1, line2 = lines[0], lines[1]

    list_a = parse_line(line1)
    list_b = parse_line(line2)

    result = find_common_elements(list_a, list_b)
    print(result)