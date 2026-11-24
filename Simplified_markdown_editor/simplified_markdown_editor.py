formatters = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line"
]
def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")
while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!done":
        break
    elif user_input == "!help":
        print_help()
    elif user_input in formatters:
        continue
    else:
        print("Unknown formatting type or command")

formatters = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "new-line"
]
def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")
def format_header():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            text = input("Text: ")
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6")
def format_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"
def format_text(formatter):
    text = input("Text: ")
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"{text}"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "inline-code":
        return f"{text}"
result_text = ""
while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!done":
        break
    elif user_input == "!help":
        print_help()
    elif user_input in formatters:
        if user_input == "header":
            result_text += format_header()
        elif user_input == "link":
            result_text += format_link()
        elif user_input == "new-line":
            result_text += "\n"
        else:
            result_text += format_text(user_input)
            print(result_text)
    else:
        print("Unknown formatting type or command")

formatters = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line"
]
def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")
def format_header():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            text = input("Text: ")
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6")
def format_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"
def format_list(formatter):
    while True:
        rows = int(input("Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")

    list_text = ""
    for i in range(1, rows + 1):
        row_text = input(f"Row #{i}: ")
        if formatter == "ordered-list":
            list_text += f"{i}. {row_text}\n"
        else:
            list_text += f"* {row_text}\n"
    return list_text
def format_text(formatter):
    text = input("Text: ")
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"{text}"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "inline-code":
        return f"{text}"
result_text = ""
while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!done":
        break
    elif user_input == "!help":
        print_help()
    elif user_input in formatters:
        if user_input == "header":
            result_text += format_header()
        elif user_input == "link":
            result_text += format_link()
        elif user_input in ("ordered-list", "unordered-list"):
            result_text += format_list(user_input)
        elif user_input == "new-line":
            result_text += "\n"
        else:
            result_text += format_text(user_input)

        print(result_text)
    else:
        print("Unknown formatting type or command")

