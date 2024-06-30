from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='daniel', email='daniel@dlc.com', password='senha')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'daniel@dlc.com'))

    assert result.id == 1
