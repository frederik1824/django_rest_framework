const listarCentros = async (idciudad) => {
    try {
        const response =await fetch(`./centros/${idciudad}`);
        const data= await response.json();
      
        if(data.message="Success"){
            let opciones= ``;
            data.centros.forEach((centros)=>{
     opciones += `<option value='${centros.id}'>${centros.nombre}</option>`;
            });
            cbocentros.innerHTML = opciones;
       }else{
        alert("Ciudades no encontradas...")
       }
    } catch (error) {
        console.log(error);
    }
}




const listarCiudad=async()=>{
    try {
        const response =await fetch("./ciudad");
        const data= await response.json();
      
        if(data.message="Success"){
            let opciones= ``;
            data.ciudad.forEach((ciudad)=>{
     opciones += `<option value='${ciudad.id}'>${ciudad.nombre}</option>`;
            });
            cbociudad.innerHTML = opciones;
            listarCentros(data.ciudad[0].id);
       }else{
        alert("Ciudades no encontradas...")
       }
    } catch (error) {
        console.log(error);
    }

};

const cargaInicial=async()=>{
    await listarCiudad();

    cbociudad.addEventListener("change", (event) => {
        listarCentros(event.target.value);
    });
};

window.addEventListener("load", async() => {
await cargaInicial();
});