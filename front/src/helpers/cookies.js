import Cookies from "js-cookie";

const setCookie = (cname, cvalue, exdays) => {
    Cookies.set(cname, cvalue, { expires: exdays })
}

const getCookie = (cname) => {
    return Cookies.get(cname);
}


const getProfile = () => {
    const profile = getCookie('profile');

    if (!profile) return false;

    return JSON.parse(profile);
}

export default { setCookie, getCookie, getProfile };
