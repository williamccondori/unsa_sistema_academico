(function (module) {

    StudyPlanController.$inject = [
        "$scope", 
        "toastr", 
        "StudyPlanFactory",
        "SchoolFactory",
        "TeacherFactory",
        "CourseFactory"
    ];

    function StudyPlanController($scope, toastr, StudyPlanFactory, SchoolFactory
        , TeacherFactory, CourseFactory) {

        $scope.ListaStudyPlan = [];
        $scope.ListaSchool = [];
        $scope.ListaTeacher = [];
        $scope.ListaCourse = [];

        $scope.ResetStudyPlan = function () {
            $scope.StudyPlan = {
                Id: 0,
                Year: 0,
                CoursesDto: [],
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.ResetCourse = function () {
            $scope.Course = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            }
        }

        $scope.Iniciar = function () {
            $scope.ResetStudyPlan();
            $scope.ObtenerStudyPlan();
            $scope.ObtenerSchool();
            $scope.ObtenerTeacher();
        };

        $scope.CrearStudyPlan = function () {
            $scope.ResetStudyPlan();
            $scope.StudyPlan.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-study-plan');
        };

        $scope.ModificarStudyPlan = function (modelo) {
            $scope.ResetStudyPlan();
            $scope.StudyPlan = modelo;
            $scope.StudyPlan.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-study-plan');
        };

        $scope.CancelarStudyPlan = function () {
            Bootstrap.CerrarModal('#app-modal-study-plan');
        };

        $scope.GuardarStudyPlan = function () {
            StudyPlanFactory.GuardarStudyPlan($scope.StudyPlan).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerStudyPlan();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-study-plan');
        };

        $scope.EliminarStudyPlan = function (modelo) {
            $scope.StudyPlan = modelo;
            StudyPlanFactory.EliminarStudyPlan($scope.StudyPlan).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerStudyPlan();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

        $scope.ObtenerStudyPlan = function () {
            StudyPlanFactory.ObtenerStudyPlan().then(function (response) {
                if (response.Estado)
                    $scope.ListaStudyPlan = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

        $scope.ObtenerSchool = function () {
            SchoolFactory.ObtenerSchool().then(function (response) {
                if (response.Estado)
                    $scope.ListaSchool = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

        $scope.ObtenerTeacher = function () {
            TeacherFactory.ObtenerTeacher().then(function (response) {
                if (response.Estado)
                    $scope.ListaTeacher = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

        $scope.ObtenerCourse = function (idStudyPlan) {
            CourseFactory.ObtenerCourse({
                IdStudyPlan: idStudyPlan
            }).then(function (response) {
                if (response.Estado)
                    $scope.ListaCourse = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

        $scope.MostrarCourse = function(modelo){
            $scope.ResetStudyPlan();
            $scope.StudyPlan = modelo;
            $scope.ObtenerCourse($scope.StudyPlan.Id);
            Bootstrap.AbrirModal('#app-modal-courses');
        }

        $scope.CerrarCourse = function(modelo){
            Bootstrap.CerrarModal('#app-modal-courses');
        }

        $scope.CrearCourse = function () {
            $scope.ResetCourse();
            $scope.Course.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-course');
        };

        $scope.ModificarCourse = function (modelo) {
            $scope.ResetCourse();
            $scope.Course = modelo;
            $scope.Course.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-course');
        }

        $scope.GuardarCourse = function () {
            $scope.Course.IdStudyPlan = $scope.StudyPlan.Id;
            CourseFactory.GuardarCourse($scope.Course).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerCourse($scope.StudyPlan.Id);
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-course');
        };

        $scope.EliminarCourse = function () {

        }

        $scope.CancelarCourse = function () {
            Bootstrap.CerrarModal('#app-modal-course');
        };
    }

    module.controller('StudyPlanController', StudyPlanController);

})(angular.module('app-unsa'));