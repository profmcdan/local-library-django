from faker import Faker
from catalog.models import Author, Book, Language, Genre


def populate_author(N=2):
    fake_gen = Faker()
    for i in range(N):
        first_name = fake_gen.first_name()
        last_name = fake_gen.last_name()
        date_of_birth = fake_gen.date_time()
        author = Author(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
        author.save()


if __name__ == '__main__':
    populate_author()
    print("Database Populated!")
