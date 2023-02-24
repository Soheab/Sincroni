import enum


class ChatType(enum.IntEnum):
    public = 0
    developer = 1
    private = 2


class BlacklistType(enum.IntEnum):
    user = 0
    server = 1