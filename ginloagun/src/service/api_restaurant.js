import httpClient from "@/service/httpClient";
import { server, apiUrl } from "@/service/constants";

export const getRemainTableByrid = async (rid) => {
    var result = await httpClient.get(apiUrl+ "/" + "getRemainTable" + "/" + rid);
    return result
};

export const getAllRestarunt = async () => {
    var result = await httpClient.get(server.RESTAURANT)
    return result
}

export const getRestarunt = async (id) => {
    var result = await httpClient.get(server.RESTAURANT + "/" + id)
    return result
}