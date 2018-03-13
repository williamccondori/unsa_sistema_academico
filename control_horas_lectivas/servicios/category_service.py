from control_horas_lectivas.models import Category
from control_horas_lectivas.dtos.category_dto import CategoryDto


class CategoryService(object):

    def get(self):
        categories_dto = []
        categories = Category.objects.all()
        for category in categories:
            categories_dto.append(CategoryDto(
                category.id
                , category.name
            ))
        return categories_dto

    def save(self, category_dto):
        if (category_dto.Estado == 1):
            category = Category(
                name=category_dto.Name
            )
            category.save()
        elif (category_dto.Estado == 2):
            category = Category.objects.filter(pk=category_dto.Id)
            category.update(
                name=category_dto.Name
            )
        else:
            return

    def delete(self, category_dto):
        category = Category.objects.filter(pk=category_dto.Id)
        category.delete()
