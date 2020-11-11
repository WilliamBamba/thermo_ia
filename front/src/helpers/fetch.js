import { stringify } from "qs";
import cookie from "./cookies";



let headers = {
    "Content-Type": "application/json"
};


if (cookie.getCookie("Authorization")) {
    headers.Authorization = cookie.getCookie("Authorization");
    headers["Access-Control-Request-Headers"] = "Authorization";
}

const sendRequest = (url, data, method) => {
    return fetch(url, {
        method: method,
        mode: "cors",
        headers: headers,
        body: data
    });
};

const postData = (url, data) => sendRequest(url, stringify(data), "POST");

const getData = (url) => sendRequest(url, null, "GET");

const deleteData = (url) => sendRequest(url, {}, "DELETE");

const putData = (url, data) => sendRequest(url, stringify(data), "PUT");

export default {
    postData, deleteData, getData, putData, sendRequest
};
