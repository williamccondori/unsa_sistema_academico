(function (module) {
    TeacherFactory.$inject = [
        'BaseFactory'
    ];
    function TeacherFactory(BaseFactory) {
        var teacher = [];
        teacher.ObtenerTeacher = function () {
            return BaseFactory.Obtener('/administracion/control_horas_lectivas/api/teacher');
        };
        teacher.GuardarTeacher = function (modelo) {
            return BaseFactory.Guardar('/administracion/control_horas_lectivas/api/teacher', modelo);
        };
        teacher.EliminarTeacher = function (modelo) {
            return BaseFactory.Eliminar('/administracion/control_horas_lectivas/api/teacher', modelo);
        };
        return teacher;
    }
    module.factory('TeacherFactory', TeacherFactory);
})(angular.module("app-unsa"));