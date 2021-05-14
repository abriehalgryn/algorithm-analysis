def right_pad_string(string, width):
    padding = (width - len(string)) * " "
    return padding + " " + string + " "

def left_pad_string(string, width):
    padding = (width - len(string)) * " "
    return " " + string + " " + padding

def print_table(data, alignments=None, separator_char="|",
                row_separator_char="-", corner_char="+"):

    headings = data[0].keys()

    # convert the values of each field to strings in
    # respective lists based on the key
    content_arrays = []
    for i, heading in enumerate(headings):
        content_arrays.append([])
        for row in data:
            content_arrays[i].append(str(row[heading]))

    if not alignments:
        alignments = ["l" for key in range(len(headings))]

    column_widths = []
    row_separator = corner_char
    current_row = separator_char

    for array, heading in zip(content_arrays, headings):

        # calculate column size
        largest_element = max(array, key=lambda x: len(x))
        column_width = max(len(largest_element), len(heading))
        column_widths.append(column_width)

        # generate heading row and row separator with newly found width
        row_separator += (column_width + 2) * row_separator_char + corner_char
        current_row += left_pad_string(heading, column_width) + separator_char

    # print headings/separators
    print(row_separator)
    print(current_row)
    print(row_separator)

    # print each row of contents
    for row in zip(*content_arrays):
        current_row = separator_char
        for val, alignment, width in zip(row, alignments, column_widths):
            if alignment == "l":
                current_row += left_pad_string(val, width)
            else:
                current_row += right_pad_string(val, width)

            current_row += separator_char
        print(current_row)

    # print final row separator
    print(row_separator)
