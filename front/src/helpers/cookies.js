import Cookies from "js-cookie";

const setCookie = (cname, cvalue, exdays) => {
    Cookies.set(cname, cvalue, { expires: exdays })
}

const getCookie = (cname) => {
    return Cookies.get(cname);
}

export default { setCookie, getCookie };
