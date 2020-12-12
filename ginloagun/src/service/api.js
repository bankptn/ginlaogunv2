import * as accountAPI from "../service/api_account"
import * as restaurantAPI from "../service/api_restaurant"
import * as reservationAPI from "../service/api_reservation"

export default {
    ...accountAPI,
    ...restaurantAPI,
    ...reservationAPI
};