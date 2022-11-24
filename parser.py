parsed_lines = []

# read dialogue file as input
# parse lines to make them match template structure
# add to list
with open("dialogue.txt", "r", encoding="utf-8") as input_file:
    for line in input_file:
        parsed_line = line.split(":", 1)
        parsed_line.reverse()
        parsed_line[0] = parsed_line[0][1:]
        parsed_line[0] = parsed_line[0].replace("\n", "")
        tuple_line = tuple(parsed_line)
        converted_line = f"scr_conversation{tuple_line}"
        parsed_lines.append(converted_line)

# write list of parsed dialogue lines to output file
with open("output.txt", "a+", encoding="utf-8") as output_file:
    for parsed_line in parsed_lines:
        output_file.write(parsed_line)
        output_file.write("\n")
