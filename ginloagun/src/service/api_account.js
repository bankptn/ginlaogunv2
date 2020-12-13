import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const login = async (values) => {
  var bodyFormData = new FormData();
  bodyFormData.append("username", values.username);
  bodyFormData.append("password", values.password);
  var result = await httpClient.post(server.LOGIN, bodyFormData);
  return result
};

export const isLoggedIn = () => {
    const token = localStorage.getItem(server.TOKEN_KEY);
    return token != null;
  };
  
export const logoff = () => {
    localStorage.removeItem(server.TOKEN_KEY);
    localStorage.removeItem(server.USER_TYPE);
    localStorage.removeItem(server.USERNAME);
  };

export const register = async (values) => {
  console.log(values)
  var bodyFormData = new FormData();
  bodyFormData.append("ssn", values.ssn);
  bodyFormData.append("fname", values.fname);
  bodyFormData.append("lname", values.lname);
  bodyFormData.append("username", values.username);
  bodyFormData.append("password", values.password);
  bodyFormData.append("address", values.address);
  bodyFormData.append("email", values.email);
  bodyFormData.append("phoneNumber", values.phoneNumber);
  bodyFormData.append("birthDay", values.birthDay);
  bodyFormData.append("pic", values.pic);
  var result = await httpClient.post(server.REGISTER, bodyFormData);
  return result
};

export const editprofile = async (values) => {
  var bodyFormData = new FormData();
  bodyFormData.append("ssn", values.ssn);
  bodyFormData.append("fname", values.fname);
  bodyFormData.append("lname", values.lname);
  bodyFormData.append("username", values.username);
  bodyFormData.append("password", values.password);
  bodyFormData.append("address", values.address);
  bodyFormData.append("email", values.email);
  bodyFormData.append("phoneNumber", values.phoneNumber);
  bodyFormData.append("birthDay", values.birthDay);
  bodyFormData.append("pic", values.pic);
  
  var result = await httpClient.put(server.ACCOUNT, bodyFormData);
  return result
};

export const reprofile = async (ssn) => {
  
  var result = await httpClient.get(server.ACCOUNT + "/" + ssn);
  return result
};