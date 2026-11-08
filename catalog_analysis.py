import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# --- Этап 1. Разминка: переменные, числа, math ---


def average_rating(movies: list[dict]) -> float:
    """Возвращает среднюю оценку по каталогу, округленную до одного знака."""
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(
    movies: list[dict], current_year: int = 2026
) -> tuple[int, int, int]:
    """Возвращает (самый старый возраст, самый новый возраст, среднее вверх)."""
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes: int) -> str:
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# --- Этап 2. Условия и match ---


def rating_tier(rating: float) -> str:
    """Возвращает категорию фильма по оценке."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    """Возвращает метку периода выпуска фильма через match."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# --- Этап 3. Циклы ---


def print_non_comedy_movies(movies: list[dict]) -> None:
    """Выводит названия всех фильмов, которые НЕ относятся к жанру 'comedy'."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(
    movies: list[dict], threshold: float = 9.0
) -> dict | None:
    """Ищет первый по порядку фильм с рейтингом выше threshold."""
    index = 0
    found_movie = None
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > threshold:
            found_movie = movie
            print(f'Первый шедевр: {movie["title"]} ({movie["rating"]})')
            break
        index += 1
    else:
        print("Шедевров не найдено")
    return found_movie


def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    """Считает количество фильмов длиннее threshold минут через накопитель."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# --- Этап 4. Строки ---


def normalize_title(title: str) -> str:
    """Приводит строку к формату Title Case вручную через срезы."""
    words = title.split(" ")
    normalized = [word[0].upper() + word[1:] if word else "" for word in words]
    return " ".join(normalized)


def make_slug(title: str) -> str:
    """Превращает название в слаг вида 'the-quiet-algorithm'."""
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie: dict) -> str:
    """Возвращает форматированную строку с описанием фильма."""
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


# --- Этап 5. Списки ---


def titles_sorted_by_rating(movies: list[dict]) -> list[str]:
    """Возвращает список названий фильмов по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(
    movies: list[dict], n: int = 3
) -> list[tuple[str, float]]:
    """Возвращает топ-n фильмов в виде списка кортежей (title, rating)."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# --- Этап 6. Словари ---


def count_by_genre(movies: list[dict]) -> dict[str, int]:
    """Возвращает словарь {жанр: количество фильмов} через dict.get()."""
    counts: dict[str, int] = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies: list[dict]) -> dict[str, list[str]]:
    """Возвращает словарь {актер: [список названий фильмов]}."""
    filmography: dict[str, list[str]] = {}
    for movie in movies:
        for actor in movie["actors"]:
            current_list = filmography.get(actor, [])
            filmography[actor] = current_list + [movie["title"]]
    return filmography


def movies_above_average(movies: list[dict]) -> dict[str, float]:
    """Строит словарь {title: rating} для фильмов с оценкой выше средней."""
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


above_average_ratings = {
    m["title"]: m["rating"]
    for m in movies
    if m["rating"] > average_rating(movies)
}


# --- Этап 7. Множества ---


def all_genres(movies: list[dict]) -> set[str]:
    """Возвращает множество всех уникальных жанров каталога."""
    genres: set[str] = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1: dict, movie2: dict) -> set[str]:
    """Возвращает множество актеров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(
    movies_a: list[dict], movies_b: list[dict]
) -> set[str]:
    """Возвращает жанры из movies_a, которых нет в movies_b."""
    return all_genres(movies_a) - all_genres(movies_b)


# --- Этап 8. Итераторы и генераторы ---


def iter_high_rated(movies: list[dict], min_rating: float = 8.0):
    """Лениво отдает фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated(movies: list[dict], min_rating: float = 8.0) -> None:
    """Демонстрирует работу генератора iter_high_rated циклом for."""
    for movie in iter_high_rated(movies, min_rating=min_rating):
        print(format_report_line(movie))


high_rated_duration_sum = sum(
    m["duration_min"] for m in movies if m["rating"] > 7
)


# --- Этап 9. Итоговый отчет ---


def build_report(movies: list[dict]) -> None:
    """Формирует и выводит итоговый консольный отчет по каталогу."""
    avg_rat = average_rating(movies)
    _, _, avg_age = catalog_age_stats(movies)

    print("ОТЧеТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {avg_rat}")
    print(f"Средний возраст фильмов: {avg_age} лет")
    print()

    print("Топ-3 фильма:")
    top_3_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    for movie in top_3_movies:
        print(f"  {format_report_line(movie)}")
    print()

    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(
        genre_counts.items(), key=lambda item: (-item[1], item[0])
    )
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    print()

    unique_genres = ", ".join(sorted(all_genres(movies)))
    print(f"Все жанры каталога: {unique_genres}")


if __name__ == "__main__":
    build_report(movies)
