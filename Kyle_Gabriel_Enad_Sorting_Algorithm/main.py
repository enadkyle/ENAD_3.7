"""
Assessment 3.7: Sorting Algorithms
Name: KYLE GABRIEL ENAD

This program removes spaces and duplicate letters from the full name,
then sorts the remaining letters alphabetically using Bubble Sort.
"""

def create_unique_letters(full_name):
    """Return unique letters in the order they first appear."""
    letters = []
    for character in full_name.upper():
        if character.isalpha() and character not in letters:
            letters.append(character)
    return letters


def bubble_sort(letters):
    """Sort letters alphabetically using the Bubble Sort algorithm."""
    sorted_letters = letters.copy()
    n = len(sorted_letters)

    for pass_number in range(n - 1):
        swapped = False

        for index in range(n - 1 - pass_number):
            if sorted_letters[index] > sorted_letters[index + 1]:
                sorted_letters[index], sorted_letters[index + 1] = (
                    sorted_letters[index + 1],
                    sorted_letters[index],
                )
                swapped = True

        if not swapped:
            break

    return sorted_letters


def main():
    full_name = "KYLE GABRIEL ENAD"

    # Array 1: unique letters in their original order (unsorted).
    unsorted_array = create_unique_letters(full_name)

    # Array 2: letters arranged alphabetically.
    sorted_array = bubble_sort(unsorted_array)

    print("Full Name:", full_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:", sorted_array)


if __name__ == "__main__":
    main()
