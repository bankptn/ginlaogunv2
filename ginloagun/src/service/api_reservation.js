import httpClient from "@/service/httpClient";
import { apiUrl } from "@/service/constants";

export const getRemainTableByrid = async (rid) => {
    var result = await httpClient.get(apiUrl+ "/" + "getRemainTable" + "/" + rid);
    return result
};