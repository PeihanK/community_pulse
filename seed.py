# seed.py
from app import create_app
from app.models import db, Question, Category

app = create_app()

with app.app_context():
    db.create_all()  # Убедитесь, что таблицы созданы

    # Создание категорий
    category1 = Category(name="Общая")
    category2 = Category(name="Технологии")
    db.session.add(category1)
    db.session.add(category2)

    # Создание вопросов
    question1 = Question(text="Ваш любимый цвет?", category_id=category1.id)
    question2 = Question(text="Какой ваш любимый язык программирования?", category_id=category2.id)
    db.session.add(question1)
    db.session.add(question2)

    db.session.commit()
    print("Начальные данные добавлены")
