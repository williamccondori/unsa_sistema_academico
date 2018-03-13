(function (module) {
    CourseFactory.$inject = [
        'BaseFactory'
    ];
    function CourseFactory(BaseFactory) {
        var Course = [];
        Course.ObtenerCourse = function (modelo) {
            debugger;
            return BaseFactory.Obtener('/control_horas_lectivas/api/course', modelo);
        };
        Course.GuardarCourse = function (modelo) {
            return BaseFactory.Guardar('/control_horas_lectivas/api/course', modelo);
        };
        Course.EliminarCourse = function (modelo) {
            return BaseFactory.Eliminar('/control_horas_lectivas/api/course', modelo);
        };
        return Course;
    }
    module.factory('CourseFactory', CourseFactory);
})(angular.module("app-unsa"));