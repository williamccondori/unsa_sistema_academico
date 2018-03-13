$(document).ready(function () {
    $("#img_cargando").hide();

    $(document).ajaxStart(function () {
        $("#img_cargando").show();
    });

    $(document).ajaxSuccess(function () {
        $("#img_cargando").hide("normal");
    });

    $(document).ajaxError(function () {
        $("#img_cargando").hide("normal");
    });
});

var EnvioHttp = {
    Get: "GET",
    Post: "POST"
}

var MensajeConfirmacion = {
    Guardar: "¿Desea guardar los cambios?",
    Eliminar: "¿Desea eliminar este registro?",
    Cancelar: "¿Desea cancelar y deshacer los cambios?",
    Aceptar: "¿Desea aceptar el documento?",
    Devolver: "¿Desea devolver el documento?"
}

var MensajeRespuesta = {
    Exito: 'El proceso se ha completado correctamente',
    Error: 'Se ha encontrado un error al realizar el proceso.'
}

var Mensaje = {
    Correcto: {
        Titulo: "CORRECTO !",
        Descripcion: "Se han guardado los cambios."
    },
    Error: {
        Titulo: "ERROR !",
        Descripcion: "Se ha presentado un problema en la aplicación."
    }
}

var EstadoObjeto = {
    SinCambios: 0,
    Nuevo: 1,
    Modificado: 2,
    Borrado: 3
};

var EstadoFormulario = {
    Default: 0,
    Nuevo: 1,
    Editar: 2
}