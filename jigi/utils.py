def strmax(string, max_len):
    if len(string) > max_len:
        string = string[: max_len - 3] + "..."
    return string
