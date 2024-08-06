from flask import Blueprint, request, jsonify, make_response
from app.models.categories import Category
from app.schemas.categories import CategoryBase
from app.models import db
from pydantic import ValidationError

categories_bp = Blueprint("categories", __name__, url_prefix="/categories")


#Получение списка всех категорий
@categories_bp.get("/", methods=['GET'])
def get_categories():
    categories = Category.query.all()
    results = [CategoryBase.from_orm(category).dict() for category in categories]
    response = make_response(jsonify(results), 200)
    return response


#Создание новой категории
@categories_bp.post("/")
def create_category():
    data = request.get_json()
    try:
        category_data = CategoryBase(**data)
    except ValidationError as e:
        return make_response(jsonify(e.errors()), 400)
    category = Category(name=category_data.name)
    db.session.add(category)
    db.session.commit()
    return make_response(jsonify(CategoryBase.from_orm(category).dict()), 201)


# Обновление конкретной категории по её ID
@categories_bp.put("/<int:id>")
def update_category(id):
    category = Category.query.get(id)
    if category is None:
        return make_response(jsonify({"message": "Категория с таким ID не найдена"}), 404)
    data = request.get_json()
    if "name" in data:
        old_category_name, category.name = category.name, data["name"]
        db.session.commit()
        return make_response(jsonify({
            **CategoryBase.from_orm(category).dict(),
            **{"old_category_name": old_category_name}
        }), 201)
    else:
        return make_response(jsonify({"message": "Имя категории не предоставлено"}), 400)


# Удаление конкретной категории по её ID
@categories_bp.delete('/<int:id>')
def delete_category(id):
    category = Category.query.get(id)
    if category is None:
        return jsonify({"message": "Категория с таким ID не найдена"}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': f"Категория с ID {id} удалена"}), 200
