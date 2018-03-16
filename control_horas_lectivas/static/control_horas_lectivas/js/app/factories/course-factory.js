(function (module) {
    CourseFactory.$inject = [
        'BaseFactory'
    ];
    function CourseFactory(BaseFactory) {
        var Course = [];
        Course.ObtenerCourse = function (modelo) {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/course', modelo);
        };
        Course.GuardarCourse = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/course', modelo);
        };
        Course.EliminarCourse = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/course', modelo);
        };
        return Course;
    }
    module.factory('CourseFactory', CourseFactory);
})(angular.module("app-unsa"));