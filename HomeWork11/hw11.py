def clean_string(writen_string: str) -> str:
    """
    Функція, яка отримує стрічку та повертає цю стрічку, очищену від малих літер та обмежену до 25 символів.

    Аргументи:
    writen_string (str): Вхідна стрічка.

    Повертає:
    str: Очищена стрічка, обмежена до 25 символів.
    """

    cleaned = "".join(filter(str.isupper, writen_string))
    return cleaned[:25]
