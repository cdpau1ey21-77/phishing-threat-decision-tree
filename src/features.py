import re


URGENT_WORDS = [
    "act now",
    "verify immediately",
    "urgent",
    "limited time",
    "account suspended",
    "password expired",
    "confirm your identity",
    "security alert",
]


KNOWN_BRANDS = [
    "paypal",
    "microsoft",
    "apple",
    "google",
    "amazon",
    "netflix",
    "bank of america",
    "chase",
]


EXECUTABLE_EXTENSIONS = [
    ".exe",
    ".js",
    ".vbs",
    ".scr",
    ".bat",
    ".cmd",
]


def has_urgent_language(email_body):
    body = email_body.lower()

    for phrase in URGENT_WORDS:
        if phrase in body:
            return True

    return False


def count_links(email_body):
    links = re.findall(r"https?://[^\s]+", email_body)
    return len(links)


def impersonates_known_brand(sender_name, email_body):
    text = f"{sender_name} {email_body}".lower()

    for brand in KNOWN_BRANDS:
        if brand in text:
            return True

    return False


def attachment_is_executable(attachment_names):
    for attachment in attachment_names:
        attachment = attachment.lower()

        for extension in EXECUTABLE_EXTENSIONS:
            if attachment.endswith(extension):
                return True

    return False
