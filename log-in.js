let passwordAdmin = document.getElementById("passwordAdmin");
let showAd = document.getElementById("showAd");


showAd.addEventListener("click",()=>{
    if(passwordAdmin.type === "password"){
        passwordAdmin.setAttribute("type","text");
        showAd.classList.remove("fa-solid","fa-eye-slash");
        showAd.classList.add("fa-solid","fa-eye");
    }else{
        passwordAdmin.setAttribute("type","password");
        showAd.classList.remove("fa-solid","fa-eye");
        showAd.classList.add("fa-solid","fa-eye-slash");
    }
})