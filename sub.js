
// للاختيار مده الاشتراك
let cardPr = document.querySelectorAll(".card-pr");

function cardPrClick(){
    cardPr.forEach(back=>{
        back.classList.remove("back-color");
    });
    cardPr[num].classList.add("back-color");
};

cardPr.forEach((back,key) =>{
    back.addEventListener("click",()=>{
        num = key;
        cardPrClick();
    });
});


// للعوده للصفحه السابقه
let btnSkip =document.querySelector(".btn-skip");
btnSkip.addEventListener("click",()=>{
    history.back();
});


let dataform = document.querySelector("form");
dataform.addEventListener("submit",(e)=>{
    e.preventDefault();

    let valid = true;

    let full = document.getElementById("full");//رساله اسم المستخدم
    let exp = document.getElementById("exp");// رساله تاريخ الانتهاء
    let cv = document.getElementById("cv");// زساله cvv
    let coun = document.getElementById("coun");// رساله اسم الدوله
    let zip = document.getElementById("zip");// رساله zip code

    // التحقق من اسم المستخدم
    let fullName = document.getElementById("fullName");// حقل ادخل الاسم
    // الشرط الخاص به
    if(fullName.value.match(/^[A-Za-z]{3,10}$/)){
        full.innerHTML = "";
    }
    else{
        full.innerHTML = "The name must be 3 letters or more";
        valid = false;
    }
     
    //التحقق من تاريخ الانتهاء
    let expData = document.getElementById("expData");// حقل ادخل التاريخ
    // الشرط الخاص به
    if(expData.value.match(/^\d{2}\/\d{2}$/)){
        exp.innerHTML = "";
    }
    else{
        exp.innerHTML = "Enter the correct date";
        valid = false;
    }

    //التحقق من رقم cvv
    let cvv = document.getElementById("cvv");// حقل ادخل cvv
    // الشرط الخاص به
    if(cvv.value.match(/^[0-9]{3}$/)){
        cv.innerHTML = "";
    }
    else{
        cv.innerHTML = "It must consist of 3 numbers";
        valid = false;
    }

    // الحقق من اسم الدوله
    let Country = document.getElementById("Country");//حقل ادخل اسم الدوله
    // الشرط الخاص به 
    if(Country.value.match(/^[A-Z-a-z]{5,}$/)){
        coun.innerHTML = "";
    }
    else{
        coun.innerHTML = "It must be 5 characters or more";
        valid = false;
    }

    // الحقق من zip code
    let zipCode = document.getElementById("zipCode");//حقل ادخل zip code
    // الشرط الخاص به 
    if(zipCode.value.match(/^[0-9]{4,5}$/)){
        zip.innerHTML = "";
    }
    else{
        zip.innerHTML = "It must consist of 5 or 4 numbers";
        valid = false;
    }
    // الشرط الخاص ب اذا كانت البيانات صحيحه
    if(valid){
        e.target.submit();
    }


})


