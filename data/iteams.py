from dataclasses import dataclass


@dataclass
class AdditionalServices:
    name: str
    description: str
    amount: int


@dataclass
class MainItem:
    name: str
    description: str
    amount: int


additional_services = [AdditionalServices('Excel', 'Подключить возможность формировать отчеты в excel', 1000),
                       AdditionalServices('Админ-панель', 'Подключить админ-панель на Django', 1500),
                       AdditionalServices('База данных', 'Подключить базу данных PostgreSQL', 500),
                       AdditionalServices('API', 'Интегрировать со сторонним сервисом', 1000)]
