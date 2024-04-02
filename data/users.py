import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    year: str
    month: str
    day: str
    subjects: str
    hobbies: str
    file: str
    address: str
    state: str
    city: str
    birthday: str


admin = User(
    first_name='admin',
    last_name='admin',
    email='blabla@bla.bla',
    gender='Female',
    phone='9999999999',
    year='1992',
    month='December',
    day='1',
    subjects='Maths',
    hobbies='Reading',
    file='img.jpg',
    address='Moscow Leninskiy av. 120',
    state='NCR',
    city='Delhi',
    birthday='01 December,1992',
)

simple_user = User(
    first_name="Марина",
    last_name="Темирханова",
    email='blabla@bla.bla',
    gender='Female',
    phone='9999999999',
    year='1992',
    month='December',
    day='1',
    subjects='Maths',
    hobbies='Reading',
    file='img.jpg',
    address='Moscow Leninskiy av. 120',
    state='NCR',
    city='Delhi',
    birthday='01 December,1992',
)
