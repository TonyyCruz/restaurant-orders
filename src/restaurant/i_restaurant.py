from abc import ABC, abstractmethod


class IRestaurant(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_client(self, client_name) -> bool:
        raise NotImplementedError

    @abstractmethod
    def _add_client_order(self, client, order, week_day) -> None:
        raise NotImplementedError

    @abstractmethod
    def _new_client(self, client, order, week_day) -> None:
        raise NotImplementedError

    @abstractmethod
    def new_order(self, client, order, week_day) -> None:
        raise NotImplementedError

    @abstractmethod
    def client_history(self, client) -> dict:
        raise NotImplementedError
