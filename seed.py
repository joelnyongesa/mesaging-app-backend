from app import app
from models import db, User, Agent, Message
from random import randint
from random import choice as rc

from faker import Faker

fake = Faker()

with app.app_context():

    print("Deleting all records...")
    User.query.delete()
    Agent.query.delete()
    Message.query.delete()


    print("Inserting users... ")
    users = []

    for i in range(10):
        user = User(
            first_name=fake.first_name(),
            last_name = fake.last_name(),
            phone_number=randint(10**9, 10**10 - 1),
            email_address=fake.email()
        )

        users.append(user)

    db.session.add_all(users)

    print("Inserting agents...")
    agents = []

    for i in range(10):
        agent = Agent(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            category = rc(["Loan Approvals", "Disbursement"])
        )

        agents.append(agent)

    db.session.add_all(agents)

    print("Inserting into messages")
    messages = []

    for i in range(20):
        message = Message(
            category = rc(["Loan Approval", "Disbursement"]),
            body = fake.sentence(10),
            user = rc(users),
            agent=rc(agents)
        )

        messages.append(message)

    db.session.add_all(messages)

    db.session.commit()

    print("Complete...")

