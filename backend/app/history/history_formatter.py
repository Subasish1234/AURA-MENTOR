def format_history(history):

    if not history:
        return ""

    text = ""

    for item in history:

        text += (
            f"{item.role}: {item.message}\n"
        )

    return text