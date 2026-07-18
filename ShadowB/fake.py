from faker import Faker
import csv
from ShadowB.Console.error import err

faker = Faker()

def username():
    return faker.name()

def age(mn,mx):
    if mn and mx:
        return faker.random_int(mn,mx)
    else:
        return faker.random_int(18,45)

def email():
    return faker.free_email()


def phone():
    return faker.phone_number()


def random_country():
    return faker.country()


def random_job():
    return faker.job()


def salary(mn,mx):
    if mn and mx:
        return faker.random_int(mn, mx)
    else:
        return faker.random_int(1000,6000)


def fake_csv(filename, rows, keys):
    file = f"{filename}.csv"

    generators = {
        "username": faker.name,
        "random_job": faker.job,
        "phone": faker.phone_number,
        "email": faker.free_email,
        "random_country": faker.country,
        "salary": lambda: faker.random_int(min=3000, max=5000),
        "age": lambda: faker.random_int(min=18, max=60),
    }

    rename = {
        "username": "name",
        "random_job": "job",
        "random_country": "country",
    }

    for key in keys:
        if key not in generators:
            err(
                f"Unknown key '{key}'. Available keys: {', '.join(generators.keys())}"
            )
            return ""

    fieldnames = [rename.get(key, key) for key in keys]

    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        data = []

        for _ in range(rows):
            row = {}

            for key in keys:
                column = rename.get(key, key)
                row[column] = generators[key]()

            data.append(row)

        writer.writerows(data)

    return file