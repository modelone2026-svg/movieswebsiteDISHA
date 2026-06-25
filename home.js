// القائمه
let meun = document.getElementById("meun"); //صوره القائمه
let navgation = document.querySelector(".navgation");// قسم القائمه
let cloes = document.getElementById("cloes");// رمز الغلق

// الداله المسوله عن ظهور قسم القائمه
meun.addEventListener("click", ()=>{
    navgation.classList.add("in");
});
// الداله المسوله عن غلق قسم القائمه
cloes.addEventListener("click", ()=>{
    navgation.classList.remove("in");
});

// صوره المستخدم
let filein = document.getElementById("filein");// الحقل المسوله عن جلب الصوره
let view = document.getElementById("view");// المكان الى هيضف فيه الصوره

//الداله المسوله عن وضع الصوره فى مكانه
filein.addEventListener("change",uploadImage);
function uploadImage(){
    let imageLink = URL.createObjectURL(filein.files[0]);
    view.style.backgroundImage = `url(${imageLink})`;
}




// ازرار التحكم section1
let next = document.querySelector("#next");
let prev = document.querySelector("#prev");

// slider
next.onclick = function(){
    let widthItem = document.querySelector(".item").offsetWidth;
    document.getElementById("formlist").scrollLeft += widthItem;
}
prev.onclick = function(){
    let widthItem = document.querySelector(".item").offsetWidth;
    document.getElementById("formlist").scrollLeft -= widthItem;
}


// ازرار التحكم section2
let next2 = document.querySelector("#next2");
let prev2 = document.querySelector("#prev2");

next2.onclick = function(){
    let widthItem = document.querySelector(".item2").offsetWidth;
    document.getElementById("formlist2").scrollLeft += widthItem;
}
prev2.onclick = function(){
    let widthItem = document.querySelector(".item2").offsetWidth;
    document.getElementById("formlist2").scrollLeft -= widthItem;
}

// ازرار التحكم section3
let next3 = document.querySelector("#next3");
let prev3 = document.querySelector("#prev3");

next3.onclick = function(){
    let widthItem = document.querySelector(".item3").offsetWidth;
    document.getElementById("formlist3").scrollLeft += widthItem;
}
prev3.onclick = function(){
    let widthItem = document.querySelector(".item3").offsetWidth;
    document.getElementById("formlist3").scrollLeft -= widthItem;
}


// ازرار التحكم section4
let next4 = document.querySelector("#next4");
let prev4 = document.querySelector("#prev4");

next4.onclick = function(){
    let widthItem = document.querySelector(".item4").offsetWidth;
    document.getElementById("formlist4").scrollLeft += widthItem;
}
prev4.onclick = function(){
    let widthItem = document.querySelector(".item4").offsetWidth;
    document.getElementById("formlist4").scrollLeft -= widthItem;
}

// ازرار التحكم section5
let next5 = document.querySelector("#next5");
let prev5 = document.querySelector("#prev5");

next5.onclick = function(){
    let widthItem = document.querySelector(".item5").offsetWidth;
    document.getElementById("formlist5").scrollLeft += widthItem;
}
prev5.onclick = function(){
    let widthItem = document.querySelector(".item5").offsetWidth;
    document.getElementById("formlist5").scrollLeft -= widthItem;
}

// ازرار التحكم section6
let next6 = document.querySelector("#next6");
let prev6 = document.querySelector("#prev6");

next6.onclick = function(){
    let widthItem = document.querySelector(".item6").offsetWidth;
    document.getElementById("formlist6").scrollLeft += widthItem;
}
prev6.onclick = function(){
    let widthItem = document.querySelector(".item6").offsetWidth;
    document.getElementById("formlist6").scrollLeft -= widthItem;
}

// ازرار التحكم section7
let next7 = document.querySelector("#next7");
let prev7 = document.querySelector("#prev7");

next7.onclick = function(){
    let widthItem = document.querySelector(".item7").offsetWidth;
    document.getElementById("formlist7").scrollLeft += widthItem;
}
prev7.onclick = function(){
    let widthItem = document.querySelector(".item7").offsetWidth;
    document.getElementById("formlist7").scrollLeft -= widthItem;
}


// ازرار التحكم section8
let next8 = document.querySelector("#next8");
let prev8 = document.querySelector("#prev8");

next8.onclick = function(){
    let widthItem = document.querySelector(".item8").offsetWidth;
    document.getElementById("formlist8").scrollLeft += widthItem;
}
prev8.onclick = function(){
    let widthItem = document.querySelector(".item8").offsetWidth;
    document.getElementById("formlist8").scrollLeft -= widthItem;
}