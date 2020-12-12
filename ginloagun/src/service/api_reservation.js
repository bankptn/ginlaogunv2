import httpClient from "@/service/httpClient";
import { server } from "@/service/constants";

export const createReservation = async (values) => {
    var bodyFormData = new FormData();
    bodyFormData.append("ssn", values.ssn);
    bodyFormData.append("rid", values.rid);
    bodyFormData.append("createDate", values.createDate);
    bodyFormData.append("tableAmount", values.tableAmount);
    bodyFormData.append("detail", values.detail);
    var result = await httpClient.post(server.RESERVATION, bodyFormData);
    return result
};