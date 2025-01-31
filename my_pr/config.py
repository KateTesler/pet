# config.py

TOKEN = '7284013293:AAG5b9TmZw3u8zdQB3BmNHHXe0TkzeBo_QE'

# ID чата, на который будет реагировать бот
AUTHORIZED_CHAT_ID = 902584287  # Замените на ID вашей группы
# Список стикеров
STICKERS = [
    'CAACAgIAAxkBAAOqZ3qxQlIr9IIxqgHsNPxwvFEP32oAAjYXAAIGf6BIc_I6FjK0bGc2BA',  # Пример стикера
    'CAACAgUAAxkBAAOlZ3qvmFwzo_HuX9TkoaJjlbheupkAAmYAA8ZRxhVnYiPuJlhRBTYE',
    'CAACAgIAAxkBAAOpZ3qxQUKNAqQJEYT_HMH3b6jdqWMAAg4LAALyg0FK0urAuKMu8SM2BA',
    'CAACAgEAAxkBAAIBamd7yTEEfRPp2Tfa638mxm1yrznNAALqAgACF2CYIVGZFB-cayOeNgQ',
    'CAACAgIAAxkBAAIBa2d7yTEbxSlFVss8a7kEiB0VJEsdAAIhVAACns4LAAFIUvUEIZ98lDYE',
    'CAACAgIAAxkBAAIBbGd7yTF1BnHTwDISVWBTKRTRdKMhAAKPAQACK15TC1JZlsxRJSLCNgQ',
    'CAACAgIAAxkBAAIBbWd7yTEdOr29sPCJUslfC7kVvdmSAAI9AgACRxVoCX8vWpNxeo5uNgQ',
    'CAACAgIAAxkBAAIBbmd7yTGc6ngoy_4Jie8lJ-pfbD6WAAInAANY3LMK-rIqFL8UIDo2BA',
    'CAACAgEAAxkBAAIBb2d7yTFaefi3czYR3kBjut1yktHkAAL7CQACv4yQBAwndSWTBrDuNgQ',
    'CAACAgIAAxkBAAIBcGd7yTEd1MigaZ9WyBoT80W9v6M0AAI6BQACP5XMCsR-TkKuQD9cNgQ',
    'CCAACAgIAAxkBAAIBcWd7yTGyN0nPWF064QsYRHNCMTIEAAIjAANZu_wlkbzSYEBl88c2BA',
    'CAACAgIAAxkBAAIBcmd7yTFUeJuPp7Wz7kFaIsXyGaZ1AAITAAM7YCQUe9seBQTGXtw2BA',
    'CAACAgIAAxkBAAIBc2d7yTEKGcbsDbIqmI3mAzuoQWKPAAKSVQACns4LAAH0kjhY58nTXDYE',
    'CAACAgIAAxkBAAIBdmd7yTFIX_Qq8gcXIN0RoQ2tjbPiAAIZAAOb4JcZRV_EW7I2cAo2BA',
    'CAACAgIAAxkBAAIBd2d7yTEpMWKt8e1I2a9aoSZt50mFAAJwFAACQq9pAAE39SyJGUg2ITYE',
    'CAACAgIAAxkBAAIBcGd7yTEd1MigaZ9WyBoT80W9v6M0AAI6BQACP5XMCsR-TkKuQD9cNgQ',
    'CAACAgIAAxkBAAIBeWd7yTEiUNtQZRXm6ql1IlpOUudrAALuHgACKHPZSN5nXdvhFG5xNgQ',
    'CAACAgIAAxkBAAIBemd7yTGSbmhGTi9vW6mdg8y2PwOPAAKSFwACE2nZSOcvuytedNQkNgQ',
    'CAACAgIAAxkBAAIBe2d7yTH5YkTtlAL1dDGP_yXgggq1AAKFHgAC6lOASNFCJPN-CLvRNgQ',
    'CAACAgIAAxkBAAIBfGd7yTH8Cov3TQnfjJruVg3h1TQFAAKsJAAC77MoSv_TUoLa9bmANgQ',
    'CAACAgIAAxkBAAIBfWd7yTF7YhutkXENcp1E95h4Wz8pAALXHgACcoaQSOZOZWtHbL4VNgQ',
    'CAACAgIAAxkBAAIBfmd7yTHcGcEAAd6kXyFK2bSpRCjLQgAC4iMAAs98yEmZA1yr5RDhETYE',
    'CAACAgIAAxkBAAIBf2d7yTGXWzH5oETaWMSUpgtkTyXfAAJQIgAC1q_ISSBD8eb_FHmvNgQ',
    'CAACAgIAAxkBAAIBgWd7yTG3Sqx7dO_WUSYAAVky35F3fAACphwAApWpOUjG8CfVuWfGfzYE',
    'CAACAgIAAxkBAAIBgGd7yTFXeNPavITpqbE8z3A6X1REAALSGwAC5qs4SGcDTQ4I18w0NgQ',
    'CAACAgIAAxkBAAIBgmd7yTEzkO1n1TquRNXBMlb4K5AqAALYIAACkUF5SIXr02Y3wDazNgQ',
    'CAACAgIAAxkBAAIBg2d7yTH_M8_fKxrS1x6szwzEWAWeAAKqGQACSLBAS6hXzZuppBPsNgQ',
    'CAACAgIAAxkBAAIBhGd7yTF-_lwhUTgmb-3EyozO3h1WAAIwJgACtoHwSyQtkZb9qw0ZNgQ',
    'CAACAgIAAxkBAAIBhWd7yTHZf9trhCYIEzJqcma81l-rAALlJwACqQKRSVT0VBQCAnGQNgQ',
    'CAACAgIAAxkBAAIBhmd7yTFsyTb8ZhtDeBZdNmUhGDlLAAJtKwACYbSZSRRglBQrfTtDNgQ',
    'CAACAgIAAxkBAAIBh2d7yTHSmHDyomAIdxNl8t1kONkAA1YkAAKj4ZlJ55PpgnqPZqg2BA',
    'CAACAgIAAxkBAAIBiGd7yTFTeosV3p2nT2SZIathrT89AALAKAACIayRSbgaEl_1Cr43NgQ',
    'CAACAgIAAxkBAAIBiWd7yTHhX-1NnO-dXzpSkbPiFtkMAAJkKwACFDiQSXkZ9z0NSFdRNgQ',

]



