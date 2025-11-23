class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
        else:
            pass

    def channel_up(self):
        if self.__status:
            if Television.MIN_CHANNEL <= self.__channel <= (Television.MAX_CHANNEL - 1):
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
        else:
            pass


    def channel_down(self):
        if self.__status:
            if (Television.MIN_CHANNEL + 1) <= self.__channel <= Television.MAX_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
        else:
            pass

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if Television.MIN_VOLUME <= self.__volume <= (Television.MAX_VOLUME - 1):
                self.__volume += 1
            elif self.__volume == Television.MAX_VOLUME:
                pass
        else:
            pass

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if (Television.MIN_VOLUME + 1) <= self.__volume <= Television.MAX_VOLUME:
                self.__volume -= 1
            elif self.__volume == Television.MIN_VOLUME:
                pass
        else:
            pass

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'