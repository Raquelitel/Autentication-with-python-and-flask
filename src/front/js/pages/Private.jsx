import React from "react";
import { Navigate } from "react-router-dom";

const Private = () => {
  return (
    <>
      <h2 className="vh-100 bg-fondo color-texto">
        Esta página es privada, pero puedes acceder porque estás logeado
      </h2>
      {localStorage.getItem("token") == "null" && <Navigate to="/" replace />}
      {/*       en la anterior linea le preguntamos si no tiene el token que vaya a la ruta / */}
    </>
  );
};

export default Private;
