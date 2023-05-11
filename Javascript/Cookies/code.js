// document.cookie = "usuario=Patrick; expires=Fri, 31 Dec 2024 23:59:59 GMT; path=/; SameSite=None; Secure";
// document.cookie = "test=star;"

// console.log(document.cookie);

const firstText = document.querySelector("#firstText");
const lastText = document.querySelector("#lastText");
const submitBtn = document.querySelector("#submitBtn");
const cookieBtn = document.querySelector("#cookieBtn");

submitBtn.addEventListener("click", () => {
    setCookie("firstName", firstText.value, 365);
    setCookie("lastName", lastText.value, 365);
})

cookieBtn.addEventListener("click", () => {
    firstText.value = getCookie("firstName");
    lastText.value = getCookie("lastName");
})


function setCookie(name, value, daysToLive){
    const date = new Date();
    date.setTime(date.getTime() + daysToLive * 24 * 6 * 60 * 1000);
    let expires = "expires=" + date.toUTCString();
    document.cookie =`${name}=${value}; SameSite=None; ${expires}; path=/; `
}

function deleteCookie(name) {
    setCookie(name, null, null);
}

function getCookie(name) {
    const cDecoded = decodeURIComponent(document.cookie);
    console.log(cDecoded)
    const cArray = cDecoded.split("; ")
    console.log(cArray)
    let result = null;
    cArray.forEach(element => {
        if(element.indexOf(name) == 0) {
            result = element.substring(name.length + 1)
            console.log(element)
        } else {
            console.log(element.indexOf(name))
        }
    })
    return result;
}