import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

const Private = () => {
  const { store, actions } = useContext(Context);
  let navigate = useNavigate();

  const logout = () => {
    localStorage.clear();
    actions.deleteTokenLS();

    /*     navigate("/"); */
  };

  console.log(store.tokenLS);

  return (
    <div className="vh-100 bg-fondo color-texto">
      <h2>Esta página es privada, pero puedes acceder porque estás logeado</h2>
      <button className="btn btn-warning" onClick={logout}>
        Cerrar sesión
      </button>

      {store.tokenLS === null && navigate("/")}

      {/*       {localStorage.getItem("token") === null ? navigate("/") : null} */}
      {/*       {!localStorage.getItem("token") ? navigate("/") : null} */}
      {/*       {!localStorage.getItem("token") && navigate("/")} */}

      {/*       en la anterior linea le preguntamos si no tiene el token que vaya a la ruta '/' */}
    </div>
  );
};

export default Private;
