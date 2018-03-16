
(function (module) {
    CategoryFactory.$inject = [
        'BaseFactory'
    ];
    function CategoryFactory(BaseFactory) {
        var category = [];
        category.ObtenerCategory = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/category');
        };
        category.GuardarCategory = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/category', modelo);
        };
        category.EliminarCategory = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/category', modelo);
        };
        return category;
    }
    module.factory('CategoryFactory', CategoryFactory);
})(angular.module("app-unsa"));