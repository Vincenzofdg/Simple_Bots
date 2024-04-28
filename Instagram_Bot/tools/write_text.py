
def write_text(input_start, input_end, description):
    first_letter = description[0]
    rest = description[1:]

    input_start.send_keys(first_letter)

    for l in rest:
        input_end.send_keys(l)

