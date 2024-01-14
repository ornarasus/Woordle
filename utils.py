import os


def getenv(key: str, *, default: str | None = None, err_msg: str = "") -> str:
    res = os.getenv(key)
    if res is None:
        if default:
            return default
        else:
            print(err_msg)
            exit()
    else:
        return res