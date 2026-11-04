-- Петров Александр Сергеевич
--Вариант 5
--Описание предметной области
--Описание расписания пригородных электропоездов одного направления. Включает в себя: станции, график движения электропоездов, стоимости билетов.
--Станции описываются: названием, тарифной зоной, порядковым номером на направлении.
--График движения электропоездов описывается: указанием станции начала маршрута, указанием станции, завершающей маршрут, списком станций, на которых поезд не останавливается, временем прибытия на каждую станцию, на которой поезд останавливается, списком дней недели, по которым данный маршрут работает.
--Стоимости билетов описываются: количеством пересекаемых зон и, непосредственно, самой стоимостью.
--Поезда ходят в обе стороны, но направление не содержит ответвлений (одна прямая ветка).
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
