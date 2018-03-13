(function (module) {

    TeacherController.$inject = ["$scope", "toastr"
        , "CategoryFactory"
        , "DepartamentFactory"
        , "RegimeFactory"
        , "TeacherFactory"
    ];

    function TeacherController($scope, toastr
        , CategoryFactory
        , DepartamentFactory
        , RegimeFactory
        , TeacherFactory
    ) {

        $scope.ListaCategory = [];
        $scope.ListaDepartament = [];
        $scope.ListaRegime = [];
        $scope.ListaTeacher = [];

        $scope.ResetTeacher = function () {
            $scope.Teacher = {
                Id: 0,
                Name: '',
                IndicadorHabilitado: 'S',
                Estado: EstadoObjeto.SinCambios
            };
        }

        $scope.Iniciar = function () {
            $scope.ResetTeacher();
            $scope.ObtenerTeacher();
            $scope.ObtenerCategory();
            $scope.ObtenerDepartament();
            $scope.ObtenerRegime();
        };

        $scope.CrearTeacher = function () {
            $scope.ResetTeacher();
            $scope.Teacher.Estado = EstadoObjeto.Nuevo;
            Bootstrap.AbrirModal('#app-modal-teacher');
        };

        $scope.ModificarTeacher = function (modelo) {
            $scope.ResetTeacher();
            $scope.Teacher = modelo;
            $scope.Teacher.Estado = EstadoObjeto.Modificado;
            Bootstrap.AbrirModal('#app-modal-teacher');
        };

        $scope.CancelarTeacher = function () {
            Bootstrap.CerrarModal('#app-modal-teacher');
        };

        $scope.GuardarTeacher = function () {
            TeacherFactory.GuardarTeacher($scope.Teacher).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerTeacher();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
            Bootstrap.CerrarModal('#app-modal-teacher');
        };

        $scope.EliminarTeacher = function (modelo) {
            $scope.Teacher = modelo;
            TeacherFactory.EliminarTeacher($scope.Teacher).then(function (response) {
                if (response.Estado) {
                    toastr.success(Mensaje.Correcto.Descripcion, Mensaje.Correcto.Titulo);
                    $scope.ObtenerTeacher();
                } else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            });
        }

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

        $scope.ObtenerCategory = function () {
            CategoryFactory.ObtenerCategory().then(function (response) {
                if (response.Estado)
                    $scope.ListaCategory = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

        $scope.ObtenerDepartament = function () {
            DepartamentFactory.ObtenerDepartament().then(function (response) {
                if (response.Estado)
                    $scope.ListaDepartament = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };

        $scope.ObtenerRegime = function () {
            RegimeFactory.ObtenerRegime().then(function (response) {
                if (response.Estado)
                    $scope.ListaRegime = response.Datos;
                else
                    toastr.error(response.Mensaje, Mensaje.Error.Titulo);
            }).catch(function (error) {
                toastr.error(MensajeRespuesta.Error, Mensaje.Error.Titulo);
            });
        };
    }

    module.controller('TeacherController', TeacherController);

})(angular.module('app-unsa'));