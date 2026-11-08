/*
Петров Александр Сергеевич М26-555
Вариант №5

Вариант 5
Выберите станции (или их идентификаторы, если другой информации нет в таблице),
на которых поезда останавливаются в период с 14:00 до 15:00,
отсортировав их по комбинации полей: станция (идентификатор) по возрастанию, время прибытия по убыванию.
Выберите количество станций на каждом маршруте и отсортируйте по убыванию.
*/

BEGIN;

-- Удалим таблицы в порядке, обратном зависимостям внешних ключей,
-- чтобы скрипт можно было запускать повторно
DROP TABLE IF EXISTS train_stops;
DROP TABLE IF EXISTS train_days;
DROP TABLE IF EXISTS trains;
DROP TABLE IF EXISTS ticket_prices;
DROP TABLE IF EXISTS days;
DROP TABLE IF EXISTS stations;

-- 1. Станции направления
CREATE TABLE stations(
    id          serial PRIMARY KEY,
    name        varchar(64) NOT NULL UNIQUE,
    tariff_zone integer NOT NULL DEFAULT 1 CHECK(tariff_zone > 0),
    seq_number  integer NOT NULL UNIQUE CHECK(seq_number > 0)
);

-- 2. Справочник дней недели
CREATE TABLE days(
    id   serial PRIMARY KEY,
    name varchar(16) NOT NULL UNIQUE
    CHECK(name IN('Понедельник', 'Вторник', 'Среда', 'Четверг',
                  'Пятница', 'Суббота', 'Воскресенье'))
);

-- 3. Маршруты
CREATE TABLE trains(
    id               serial PRIMARY KEY,
    start_station_id integer NOT NULL REFERENCES stations(id),
    end_station_id   integer NOT NULL REFERENCES stations(id),
    CHECK(start_station_id <> end_station_id)
);

-- 4. Дни работы маршрутов
CREATE TABLE train_days(
    train_id integer NOT NULL REFERENCES trains(id),
    day_id   integer NOT NULL REFERENCES days(id),
    PRIMARY KEY(train_id, day_id)
);

-- 5. Остановки маршрутов
CREATE TABLE train_stops(
    train_id     integer NOT NULL REFERENCES trains(id),
    station_id   integer NOT NULL REFERENCES stations(id),
    arrival_time time NOT NULL,
    PRIMARY KEY(train_id, station_id)
);

-- 6. Тарифы на билеты
CREATE TABLE ticket_prices(
    zones_crossed integer PRIMARY KEY CHECK(zones_crossed > 0),
    price         numeric(8, 2) NOT NULL CHECK(price > 0)
);

-- Наполнение таблицы станций
-- seq_number задаёт единый порядок станций на прямом направлении
INSERT INTO stations (name, tariff_zone, seq_number) VALUES
    ('Москва-Курская',  1, 1),
    ('Царицыно',        2, 2),
    ('Подольск',        2, 3),
    ('Чехов',           3, 4),
    ('Серпухов',        4, 5),
    ('Тарусская',       5, 6),
    ('Ясногорск',       6, 7),
    ('Тула-1-Курская',  7, 8);

-- Наполнение справочника дней недели
INSERT INTO days (name) VALUES
    ('Понедельник'),
    ('Вторник'),
    ('Среда'),
    ('Четверг'),
    ('Пятница'),
    ('Суббота'),
    ('Воскресенье');

-- Наполнение таблицы маршрутов
-- Маршруты представлены в обоих направлениях; ответвлений нет
-- Идентификаторы станций соответствуют порядку seq_number выше
INSERT INTO trains (start_station_id, end_station_id) VALUES
    (1, 8), -- Москва-Курская -> Тула-1-Курская, полный маршрут
    (8, 1), -- Тула-1-Курская -> Москва-Курская, полный маршрут
    (3, 5), -- Подольск -> Серпухов, экспресс
    (5, 1), -- Серпухов -> Москва-Курская
    (1, 5), -- Москва-Курская -> Серпухов, экспресс
    (8, 3); -- Тула-1-Курская -> Подольск, экспресс

-- Дни курсирования маршрутов
-- Идентификаторы дней: 1 — понедельник, ..., 7 — воскресенье
INSERT INTO train_days (train_id, day_id) VALUES
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
    (3, 6), (3, 7),
    (4, 1), (4, 3), (4, 5),
    (5, 2), (5, 4), (5, 6),
    (6, 7);

-- Остановки и время прибытия
-- Отсутствие строки для пары train_id/station_id означает,
-- что данный поезд на этой станции не останавливается
INSERT INTO train_stops (train_id, station_id, arrival_time) VALUES
    -- Маршрут 1: Москва-Курская -> Тула-1-Курская
    (1, 1, TIME '13:35'),
    (1, 2, TIME '13:50'),
    (1, 3, TIME '14:02'),
    (1, 4, TIME '14:17'),
    (1, 5, TIME '14:31'),
    (1, 6, TIME '14:45'),
    (1, 7, TIME '14:58'),
    (1, 8, TIME '15:12'),

    -- Маршрут 2: Тула-1-Курская -> Москва-Курская
    (2, 8, TIME '13:40'),
    (2, 7, TIME '13:53'),
    (2, 6, TIME '14:07'),
    (2, 5, TIME '14:21'),
    (2, 4, TIME '14:36'),
    (2, 3, TIME '14:51'),
    (2, 2, TIME '15:05'),
    (2, 1, TIME '15:18'),

    -- Маршрут 3: Подольск -> Серпухов (без остановки в Чехове)
    (3, 3, TIME '14:10'),
    (3, 5, TIME '14:39'),

    -- Маршрут 4: Серпухов -> Москва-Курская (без остановки в Чехове)
    (4, 5, TIME '14:04'),
    (4, 3, TIME '14:36'),
    (4, 2, TIME '14:52'),
    (4, 1, TIME '15:08'),

    -- Маршрут 5: Москва-Курская -> Серпухов (остановки в Подольске и Серпухове)
    (5, 1, TIME '14:05'),
    (5, 3, TIME '14:37'),
    (5, 5, TIME '15:09'),

    -- Маршрут 6: Тула-1-Курская -> Подольск (экспресс)
    (6, 8, TIME '13:55'),
    (6, 6, TIME '14:25'),
    (6, 4, TIME '14:55'),
    (6, 3, TIME '15:10');

-- Шкала стоимости в зависимости от количества пересекаемых зон
INSERT INTO ticket_prices (zones_crossed, price) VALUES
    (1, 45.00),
    (2, 65.00),
    (3, 85.00),
    (4, 105.00),
    (5, 125.00),
    (6, 145.00),
    (7, 165.00);

COMMIT;

/*
ЗАДАНИЕ 1. Станции, на которых поезда останавливаются с 14:00 до 15:00.
BETWEEN включает обе границы интервала: 14:00:00 и 15:00:00.
В результате одна станция может встретиться несколько раз,
если на ней в этом интервале останавливаются разные поезда
*/
SELECT
    s.id AS station_id,
    s.name AS station_name,
    ts.arrival_time
FROM train_stops AS ts
JOIN stations AS s ON s.id = ts.station_id
WHERE ts.arrival_time BETWEEN TIME '14:00:00' AND TIME '15:00:00'
ORDER BY
    s.id ASC,
    ts.arrival_time DESC;

/*
ЗАДАНИЕ 2. Количество станций, на которых останавливается каждый маршрут
*/
SELECT
    t.id AS train_id,
    COUNT(ts.station_id) AS station_count
FROM trains AS t
LEFT JOIN train_stops AS ts
    ON ts.train_id = t.id
GROUP BY t.id
ORDER BY
    station_count DESC,
    t.id ASC;
