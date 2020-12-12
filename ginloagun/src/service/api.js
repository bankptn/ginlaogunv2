import * as accountAPI from "../service/api_account"
import * as restaurant from "../service/api_restaurant"

export default {
    ...accountAPI,
    ...restaurant
};