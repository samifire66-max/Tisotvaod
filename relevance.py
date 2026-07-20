ALLOWED_ORIGINS = [

    "tel aviv",
    "tlv",

    "israel",
    "eilat",

    "haifa",
    "hfa"

]


def is_relevant(title):

    text = title.lower()

    for origin in ALLOWED_ORIGINS:

        if origin in text:
            return True

    return False
