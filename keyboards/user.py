from aiogram.types import ReplyKeyboardMarkup


def main_keyb() -> ReplyKeyboardMarkup:
    """Get main keyboard"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(("Income"), ("Expense"))
    markup.add(("Transfer"))
    markup.add(("Available"))

    return markup


def no_description_keyb() -> ReplyKeyboardMarkup:
    """Get keyboard with 'No description' button"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(("No description"))

    return markup


def same_amount_keyb() -> ReplyKeyboardMarkup:
    """Get keyboard with 'Same amount' button"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(("Same amount"))

    return markup


def two_row_keyb(buttons: list) -> ReplyKeyboardMarkup:
    """Get keyboard with two row buttons from list"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in range(0, len(buttons), 2):
        # If there is only one item left...
        if len(buttons) - i == 1:
            # Adding last item as big button
            markup.add(buttons[-1])
            break
        # Adding items as two buttons in a row
        markup.add(buttons[i], buttons[i + 1])

    return markup
