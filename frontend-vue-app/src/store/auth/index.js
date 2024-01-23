import mutations from "@/store/auth/mutations";
import getters from "@/store/auth/getters";

export default {
    namespaced: true,
    state() {
        return {
            authenticated: false,
            username: ""
        }
    },
    mutations,
    getters
}